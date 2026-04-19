// Supabase Edge Function (Deno) — send-pre-session-notifications
// Trigger: pg_cron nightly (T-24h avant seances)
// Sprint 5 / P3
//
// Deploy: supabase functions deploy send-pre-session-notifications
// Schedule: via pg_cron (see SPRINT5_RAPPORT.md setup section)
//
// Required secrets (set via Supabase Dashboard > Edge Functions > Secrets):
//   VAPID_PUBLIC_KEY    (same as window.VAPID_PUBLIC_KEY in index.html)
//   VAPID_PRIVATE_KEY   (never commit; generate via `npx web-push generate-vapid-keys`)
//   VAPID_SUBJECT       (mailto:admin@realdev-vfc.be)
//
// Uses service_role key via Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') (auto-injected).

import { createClient } from "https://esm.sh/@supabase/supabase-js@2";
import * as webpush from "https://esm.sh/web-push@3.6.7";

const SUPA_URL = Deno.env.get("SUPABASE_URL")\!;
const SUPA_SERVICE = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")\!;
const VAPID_PUBLIC = Deno.env.get("VAPID_PUBLIC_KEY")\!;
const VAPID_PRIVATE = Deno.env.get("VAPID_PRIVATE_KEY")\!;
const VAPID_SUBJECT = Deno.env.get("VAPID_SUBJECT") || "mailto:admin@realdev-vfc.be";

webpush.setVapidDetails(VAPID_SUBJECT, VAPID_PUBLIC, VAPID_PRIVATE);

const sb = createClient(SUPA_URL, SUPA_SERVICE, { auth: { persistSession: false } });

function pad2(n: number){ return String(n).padStart(2, "0"); }

Deno.serve(async (req) => {
  try {
    const now = new Date();
    const target = new Date(now.getTime() + 24 * 3600 * 1000); // T+24h
    const iso = `${target.getFullYear()}-${pad2(target.getMonth()+1)}-${pad2(target.getDate())}`;

    // 1) Fetch all training_plans and find sessions matching target date
    const { data: plans, error: planErr } = await sb.from("training_plans").select("match_id, sessions");
    if (planErr) throw planErr;

    const sessionsOfDay: Array<{ match_id: string; session: any }> = [];
    (plans || []).forEach((pl: any) => {
      (pl.sessions || []).forEach((s: any) => {
        if (\!s) return;
        const d = s.date || s.session_date;
        if (d && String(d).slice(0, 10) === iso) {
          sessionsOfDay.push({ match_id: pl.match_id, session: s });
        }
      });
    });

    if (\!sessionsOfDay.length) {
      return new Response(JSON.stringify({ ok: true, sent: 0, reason: "no sessions" }), { headers: { "content-type": "application/json" } });
    }

    // 2) Fetch all subscriptions
    const { data: subs, error: subErr } = await sb.from("push_subscriptions").select("*");
    if (subErr) throw subErr;
    if (\!subs || \!subs.length) {
      return new Response(JSON.stringify({ ok: true, sent: 0, reason: "no subscribers" }), { headers: { "content-type": "application/json" } });
    }

    // 3) Craft notification for first session (simplest MVP: one push per subscriber per day)
    const s0 = sessionsOfDay[0].session;
    const title = `Rappel seance demain`;
    const body = `${s0.title || s0.type || "Seance"} ${s0.time ? "a " + s0.time : ""} ${s0.location ? "\u00b7 " + s0.location : ""}`.trim();

    const payload = JSON.stringify({
      title,
      body,
      url: "/realdev-vfc-app/?page=planning",
      tag: `rdv-session-${iso}`,
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
        // 404/410: subscription expired, remove row
        if (e && (e.statusCode === 404 || e.statusCode === 410)) {
          await sb.from("push_subscriptions").delete().eq("endpoint", row.endpoint);
          cleanedUp += 1;
        } else {
          console.error("webpush send failed", e?.statusCode, e?.body);
        }
      }
    }));

    return new Response(JSON.stringify({ ok: true, date: iso, sessions: sessionsOfDay.length, subs: subs.length, sent, cleanedUp }), { headers: { "content-type": "application/json" } });
  } catch (e: any) {
    console.error("send-pre-session-notifications failed", e);
    return new Response(JSON.stringify({ ok: false, error: e?.message || String(e) }), { status: 500, headers: { "content-type": "application/json" } });
  }
});
