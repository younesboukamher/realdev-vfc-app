// =====================================================================
// Supabase Edge Function (Deno) — send-pre-session-notifications
// Sprint 5 / P3 — RealDev VFC
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
// Variables auto-injectées par Supabase (pas besoin de les set) :
//   SUPABASE_URL
//   SUPABASE_SERVICE_ROLE_KEY (bypass RLS)
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

    // --- 2) Lire training_plans + matches puis extraire les séances du jour J+1
    //
    // Les sessions dans training_plans.sessions n'ont PAS de champ `date` explicite.
    // Elles ont un `type` (lundi/mardi/mercredi/...) et appartiennent à un match via match_id.
    // La date de chaque séance est DÉRIVÉE côté app depuis match_date en reculant du bon
    // nombre de jours selon le day-of-week du type vs celui du match (cf. index.html L4081).
    // On reproduit ici cette logique pour rester cohérent.
    const { data: plans, error: planErr } = await sb
      .from("training_plans")
      .select("match_id, sessions");
    if (planErr) throw planErr;

    const { data: matches, error: matchErr } = await sb
      .from("matches")
      .select("id, match_date");
    if (matchErr) throw matchErr;

    const matchDateById: Record<string, string> = {};
    (matches || []).forEach((m: any) => {
      if (m && m.id && m.match_date) matchDateById[m.id] = String(m.match_date).slice(0, 10);
    });

    // lundi=1 ... dimanche=0 (JS getDay())
    const dayIdxOfType: Record<string, number> = {
      dimanche: 0, lundi: 1, mardi: 2, mercredi: 3, jeudi: 4, vendredi: 5, samedi: 6,
    };

    type SessionRow = { match_id: string; session: Record<string, unknown> };
    const sessionsOfDay: SessionRow[] = [];

    (plans || []).forEach((pl: { match_id: string; sessions: unknown[] }) => {
      const mdate = matchDateById[pl.match_id];
      if (!mdate) return;
      // Utiliser midi UTC pour éviter les effets de bord DST/timezone
      const matchD = new Date(mdate + "T12:00:00Z");
      const matchDow = matchD.getUTCDay();

      (pl.sessions || []).forEach((s: any) => {
        if (!s) return;

        // 1) Priorité au champ date explicite s'il existe (compat future)
        const explicit = s.date || s.session_date;
        if (explicit && String(explicit).slice(0, 10) === iso) {
          sessionsOfDay.push({ match_id: pl.match_id, session: s });
          return;
        }

        // 2) Sinon, calculer depuis match_date + type
        const tp = String(s.type || "").toLowerCase();
        const trainDow = dayIdxOfType[tp];
        if (trainDow == null) return;

        let diff = matchDow - trainDow;
        if (diff <= 0) diff += 7; // séance toujours AVANT le match
        const sessD = new Date(matchD);
        sessD.setUTCDate(sessD.getUTCDate() - diff);
        const sIso = `${sessD.getUTCFullYear()}-${pad2(sessD.getUTCMonth() + 1)}-${pad2(sessD.getUTCDate())}`;

        if (sIso === iso) {
          sessionsOfDay.push({ match_id: pl.match_id, session: s });
        }
      });
    });

    if (!sessionsOfDay.length) {
      return new Response(
        JSON.stringify({ ok: true, date: iso, sent: 0, reason: "no sessions" }),
        { headers: { "content-type": "application/json" } },
      );
    }

    // --- 3) Lire toutes les subscriptions (service_role bypass RLS)
    const { data: subs, error: subErr } = await sb
      .from("push_subscriptions")
      .select("*");
    if (subErr) throw subErr;
    if (!subs || !subs.length) {
      return new Response(
        JSON.stringify({ ok: true, date: iso, sent: 0, reason: "no subscribers" }),
        { headers: { "content-type": "application/json" } },
      );
    }

    // --- 4) Construire le payload (1 push par subscriber, 1ère séance du jour)
    const s0: any = sessionsOfDay[0].session;
    const title = "Rappel seance demain";
    const bodyParts: string[] = [];
    bodyParts.push(String(s0.title || s0.type || "Seance"));
    if (s0.time)     bodyParts.push("a " + s0.time);
    if (s0.location) bodyParts.push("\u00b7 " + s0.location);
    const body = bodyParts.join(" ").trim();

    const payload = JSON.stringify({
      title,
      body,
      url: "/realdev-vfc-app/?page=planning",
      tag: `rdv-session-${iso}`,
    });

    // --- 5) Envoyer en parallele + cleanup des endpoints expires
    let sent      = 0;
    let cleanedUp = 0;

    await Promise.all(
      (subs as any[]).map(async (row) => {
        try {
          await webpush.sendNotification(
            {
              endpoint: row.endpoint,
              keys: { p256dh: row.p256dh, auth: row.auth },
            },
            payload,
          );
          sent += 1;
        } catch (e: any) {
          const sc = e?.statusCode;
          if (sc === 404 || sc === 410) {
            // Subscription expiree : supprimer la ligne
            await sb
              .from("push_subscriptions")
              .delete()
              .eq("endpoint", row.endpoint);
            cleanedUp += 1;
          } else {
            console.error("webpush send failed", sc, e?.body || e?.message);
          }
        }
      }),
    );

    return new Response(
      JSON.stringify({
        ok:         true,
        date:       iso,
        sessions:   sessionsOfDay.length,
        subs:       subs.length,
        sent,
        cleanedUp,
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

