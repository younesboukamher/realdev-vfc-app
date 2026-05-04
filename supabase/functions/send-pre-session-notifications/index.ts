// =====================================================================
// Supabase Edge Function (Deno) — send-pre-session-notifications
// Sprint 5 / P3 — RealDev VFC
// Multi-team patch (Sprint multi-team 2026-05) — scope par team_id
//
// Déploiement :
//   supabase functions deploy send-pre-session-notifications
//
// Déclenchement : pg_cron quotidien à 18h UTC (T-24h pour séance J+1)
// Voir P3_SETUP_README.md section 4.
//
// Secrets requis (Supabase Dashboard > Project Settings > Edge Functions > Secrets
// OU via CLI : supabase secrets set KEY=value) :
//   VAPID_PUBLIC_KEY    — identique à window.VAPID_PUBLIC_KEY dans index.html
//   VAPID_PRIVATE_KEY   — à NE JAMAIS committer, généré via `npx web-push generate-vapid-keys`
//   VAPID_SUBJECT       — ex: "mailto:admin@realdev-vfc.be"
//
// Variables auto-injectées par Supabase :
//   SUPABASE_URL
//   SUPABASE_SERVICE_ROLE_KEY (bypass RLS — nécessaire pour lire user_teams + push_subscriptions)
// =====================================================================

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";
import * as webpush from "https://esm.sh/web-push@3.6.7";

const SUPA_URL      = Deno.env.get("SUPABASE_URL")!;
const SUPA_SERVICE  = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const VAPID_PUBLIC  = Deno.env.get("VAPID_PUBLIC_KEY")!;
const VAPID_PRIVATE = Deno.env.get("VAPID_PRIVATE_KEY")!;
const VAPID_SUBJECT = Deno.env.get("VAPID_SUBJECT") || "mailto:admin@realdev-vfc.be";

webpush.setVapidDetails(VAPID_SUBJECT, VAPID_PUBLIC, VAPID_PRIVATE);

const sb = createClient(SUPA_URL, SUPA_SERVICE, {
  auth: { persistSession: false },
});

function pad2(n: number): string {
  return String(n).padStart(2, "0");
}

Deno.serve(async (_req) => {
  try {
    // --- 1) Calculer la date cible (T+24h, format YYYY-MM-DD)
    const now    = new Date();
    const target = new Date(now.getTime() + 24 * 3600 * 1000);
    const iso    = `${target.getFullYear()}-${pad2(target.getMonth() + 1)}-${pad2(target.getDate())}`;

    // --- 2) Lire training_plans + matches (avec team_id) puis extraire les séances du J+1
    const { data: plans, error: planErr } = await sb
      .from("training_plans")
      .select("match_id, sessions, team_id");
    if (planErr) throw planErr;

    const { data: matches, error: matchErr } = await sb
      .from("matches")
      .select("id, match_date, team_id");
    if (matchErr) throw matchErr;

    const matchDateById: Record<string, string> = {};
    (matches || []).forEach((m: any) => {
      if (m && m.id && m.match_date) matchDateById[m.id] = String(m.match_date).slice(0, 10);
    });

    const dayIdxOfType: Record<string, number> = {
      dimanche: 0, lundi: 1, mardi: 2, mercredi: 3, jeudi: 4, vendredi: 5, samedi: 6,
    };

    type SessionRow = { match_id: string; team_id: string; session: Record<string, unknown> };
    const sessionsOfDay: SessionRow[] = [];

    (plans || []).forEach((pl: { match_id: string; sessions: unknown[]; team_id: string }) => {
      const mdate = matchDateById[pl.match_id];
      if (!mdate) return;
      const tid = pl.team_id || "a-team";
      const matchD = new Date(mdate + "T12:00:00Z");
      const matchDow = matchD.getUTCDay();

      (pl.sessions || []).forEach((s: any) => {
        if (!s) return;
        const explicit = s.date || s.session_date;
        if (explicit && String(explicit).slice(0, 10) === iso) {
          sessionsOfDay.push({ match_id: pl.match_id, team_id: tid, session: s });
          return;
        }
        const tp = String(s.type || "").toLowerCase();
        const trainDow = dayIdxOfType[tp];
        if (trainDow == null) return;
        let diff = matchDow - trainDow;
        if (diff <= 0) diff += 7;
        const sessD = new Date(matchD);
        sessD.setUTCDate(sessD.getUTCDate() - diff);
        const sIso = `${sessD.getUTCFullYear()}-${pad2(sessD.getUTCMonth() + 1)}-${pad2(sessD.getUTCDate())}`;
        if (sIso === iso) {
          sessionsOfDay.push({ match_id: pl.match_id, team_id: tid, session: s });
        }
      });
    });

    if (!sessionsOfDay.length) {
      return new Response(
        JSON.stringify({ ok: true, date: iso, sent: 0, reason: "no sessions" }),
        { headers: { "content-type": "application/json" } },
      );
    }

    const sessionByTeam: Record<string, any> = {};
    for (const s of sessionsOfDay) {
      if (!sessionByTeam[s.team_id]) sessionByTeam[s.team_id] = s.session;
    }
    const teamIds = Object.keys(sessionByTeam);

    const { data: teamsRows } = await sb
      .from("teams")
      .select("id, display_name, short_label")
      .in("id", teamIds);
    const teamLabel: Record<string, string> = {};
    (teamsRows || []).forEach((t: any) => { teamLabel[t.id] = t.display_name || t.short_label || t.id; });

    let totalSent = 0;
    let totalCleaned = 0;
    const perTeamStats: Record<string, { sent: number; cleaned: number; subs: number }> = {};

    for (const tid of teamIds) {
      const sess: any = sessionByTeam[tid];

      const { data: ut, error: utErr } = await sb
        .from("user_teams")
        .select("user_id")
        .eq("team_id", tid);
      if (utErr) { console.error("[multi-team] user_teams read failed", tid, utErr); continue; }
      const userIds = (ut || []).map((r: any) => r.user_id).filter(Boolean);
      if (!userIds.length) {
        perTeamStats[tid] = { sent: 0, cleaned: 0, subs: 0 };
        continue;
      }

      const { data: subs, error: subErr } = await sb
        .from("push_subscriptions")
        .select("*")
        .in("user_id", userIds);
      if (subErr) { console.error("[multi-team] push_subs read failed", tid, subErr); continue; }
      if (!subs || !subs.length) {
        perTeamStats[tid] = { sent: 0, cleaned: 0, subs: 0 };
        continue;
      }

      const teamName = teamLabel[tid] || tid;
      const title = "Rappel seance demain";
      const bodyParts: string[] = [];
      bodyParts.push(`[${teamName}]`);
      bodyParts.push(String(sess.title || sess.type || "Seance"));
      if (sess.time)     bodyParts.push("a " + sess.time);
      if (sess.location) bodyParts.push("· " + sess.location);
      const body = bodyParts.join(" ").trim();

      const payload = JSON.stringify({
        title,
        body,
        url: "/realdev-vfc-app/?page=planning",
        tag: `rdv-session-${tid}-${iso}`,
      });

      let sent = 0;
      let cleanedUp = 0;
      await Promise.all((subs as any[]).map(async (row) => {
        try {
          await webpush.sendNotification(
            { endpoint: row.endpoint, keys: { p256dh: row.p256dh, auth: row.auth } },
            payload,
          );
          sent += 1;
        } catch (e: any) {
          const sc = e?.statusCode;
          if (sc === 404 || sc === 410) {
            await sb.from("push_subscriptions").delete().eq("endpoint", row.endpoint);
            cleanedUp += 1;
          } else {
            console.error("webpush send failed", tid, sc, e?.body || e?.message);
          }
        }
      }));
      totalSent += sent;
      totalCleaned += cleanedUp;
      perTeamStats[tid] = { sent, cleaned: cleanedUp, subs: subs.length };
    }

    return new Response(
      JSON.stringify({
        ok:         true,
        date:       iso,
        teams:      teamIds,
        sessions:   sessionsOfDay.length,
        sent:       totalSent,
        cleanedUp:  totalCleaned,
        perTeam:    perTeamStats,
      }),
      { headers: { "content-type": "application/json" } },
    );
  } catch (e: any) {
    console.error("send-pre-session-notifications failed", e);
    return new Response(
      JSON.stringify({ ok: false, error: e?.message || String(e) }),
      { status: 500, headers: { "content-type": "application/json" } },
    );
  }
});
