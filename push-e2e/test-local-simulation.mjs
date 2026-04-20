// Simulation end-to-end offline : Supabase mock + web-push mock.
// Reproduit le flow complet (cron → read plans → select sessions J+1 → send)
// pour valider la logique cote Edge Function sans reseau ni VAPID.
//
// Cas couverts :
//   - happy path : 2 plans × 3 sessions, 3 subscribers, 1 session matche J+1
//   - cleanup : endpoint 410 → ligne push_subscriptions supprimee
//   - no-sessions : reponse { sent: 0, reason: 'no sessions' }
//   - no-subs : reponse { sent: 0, reason: 'no subscribers' }

import { sessionsForDate } from './derivation.mjs';

let passed = 0, failed = 0;
function it(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n    ${e.message}`); failed++; }
}
function eq(a, b, msg) {
  const aj = JSON.stringify(a), bj = JSON.stringify(b);
  if (aj !== bj) throw new Error(`${msg || ''} got=${aj} expected=${bj}`);
}

// --- Mock Supabase (interface minimale : from().select() / delete().eq())
function makeSbMock(tables) {
  const deleted = [];
  return {
    from: (table) => ({
      select: async () => ({ data: tables[table] || [], error: null }),
      delete: () => ({
        eq: async (col, val) => {
          tables[table] = (tables[table] || []).filter((r) => r[col] !== val);
          deleted.push({ table, col, val });
          return { error: null };
        },
      }),
    }),
    _deleted: deleted,
    _tables: tables,
  };
}

// --- Mock web-push (enregistre les envois, simule 410 pour un endpoint cible)
function makeWebpushMock({ expireEndpoint }) {
  const sent = [];
  return {
    setVapidDetails: () => {},
    sendNotification: async (sub, payload) => {
      if (sub.endpoint === expireEndpoint) {
        const err = new Error('Gone');
        err.statusCode = 410;
        throw err;
      }
      sent.push({ sub, payload });
      return { ok: true };
    },
    _sent: sent,
  };
}

// --- Reproduction du flow Edge Fn (extrait de index.ts, allege, synchrone)
async function runCron(sb, webpush, { now }) {
  const pad2 = (n) => String(n).padStart(2, '0');
  const target = new Date(now.getTime() + 24 * 3600 * 1000);
  const iso = `${target.getUTCFullYear()}-${pad2(target.getUTCMonth()+1)}-${pad2(target.getUTCDate())}`;

  const plans = (await sb.from('training_plans').select()).data;
  const matches = (await sb.from('matches').select()).data;
  const matchDateById = {};
  for (const m of matches) if (m?.id && m?.match_date) matchDateById[m.id] = String(m.match_date).slice(0,10);

  const sessionsOfDay = sessionsForDate(plans, matchDateById, iso);

  if (!sessionsOfDay.length) {
    return { ok: true, date: iso, sent: 0, reason: 'no sessions' };
  }

  const subs = (await sb.from('push_subscriptions').select()).data;
  if (!subs.length) {
    return { ok: true, date: iso, sent: 0, reason: 'no subscribers' };
  }

  const s0 = sessionsOfDay[0].session;
  const payload = JSON.stringify({
    title: 'Rappel seance demain',
    body:  [s0.title || s0.type, s0.time && 'a '+s0.time, s0.location && '· '+s0.location].filter(Boolean).join(' ').trim(),
    url:   '/realdev-vfc-app/?page=planning',
    tag:   `rdv-session-${iso}`,
  });

  let sent = 0, cleanedUp = 0;
  await Promise.all(subs.map(async (row) => {
    try {
      await webpush.sendNotification({ endpoint: row.endpoint, keys: { p256dh: row.p256dh, auth: row.auth } }, payload);
      sent += 1;
    } catch (e) {
      if (e.statusCode === 404 || e.statusCode === 410) {
        await sb.from('push_subscriptions').delete().eq('endpoint', row.endpoint);
        cleanedUp += 1;
      }
    }
  }));

  return { ok: true, date: iso, sessions: sessionsOfDay.length, subs: subs.length, sent, cleanedUp };
}

// ==== TESTS ====

console.log('\n▶ Happy path — 1 session mardi, 3 subscribers');
await (async () => {
  // now = dimanche 19/04/2026 → J+1 = lundi 20/04/2026
  // match samedi 25/04 + mardi → mardi 21/04 (PAS J+1, 20/04=lundi)
  // match samedi 25/04 + lundi → lundi 20/04 (J+1 ✓)
  const now = new Date('2026-04-19T18:00:00Z');

  const sb = makeSbMock({
    matches: [{ id: 'm1', match_date: '2026-04-25' }],
    training_plans: [{ match_id: 'm1', sessions: [
      { type: 'lundi',    title: 'Strength', time: '18:30', location: 'Gym B' },
      { type: 'mardi',    title: 'Activation' },
      { type: 'mercredi', title: 'Tactical' },
    ]}],
    push_subscriptions: [
      { endpoint: 'https://fcm/1', p256dh: 'k1', auth: 'a1' },
      { endpoint: 'https://fcm/2', p256dh: 'k2', auth: 'a2' },
      { endpoint: 'https://fcm/3', p256dh: 'k3', auth: 'a3' },
    ],
  });
  const wp = makeWebpushMock({ expireEndpoint: null });

  const r = await runCron(sb, wp, { now });

  it('date cible = 2026-04-20', () => eq(r.date, '2026-04-20'));
  it('1 session matche (lundi)',   () => eq(r.sessions, 1));
  it('3 subs → 3 sent',            () => eq(r.sent, 3));
  it('0 cleaned up',               () => eq(r.cleanedUp, 0));
  it('payload contient le titre',  () => {
    if (!wp._sent.length) throw new Error('aucun envoi');
    const p = JSON.parse(wp._sent[0].payload);
    if (p.title !== 'Rappel seance demain') throw new Error('title=' + p.title);
    if (!p.body.includes('Strength')) throw new Error('body=' + p.body);
    if (p.tag !== 'rdv-session-2026-04-20') throw new Error('tag=' + p.tag);
  });
})();

console.log('\n▶ Cleanup — endpoint 410');
await (async () => {
  const now = new Date('2026-04-19T18:00:00Z');
  const sb = makeSbMock({
    matches: [{ id: 'm1', match_date: '2026-04-25' }],
    training_plans: [{ match_id: 'm1', sessions: [{ type: 'lundi', title: 'Strength' }] }],
    push_subscriptions: [
      { endpoint: 'https://dead/1', p256dh: 'k1', auth: 'a1' },
      { endpoint: 'https://alive/2', p256dh: 'k2', auth: 'a2' },
    ],
  });
  const wp = makeWebpushMock({ expireEndpoint: 'https://dead/1' });

  const r = await runCron(sb, wp, { now });

  it('1 sent (alive), 1 cleaned (dead)', () => { eq(r.sent, 1); eq(r.cleanedUp, 1); });
  it('ligne dead supprimee de push_subscriptions', () => {
    const left = sb._tables.push_subscriptions.map((r) => r.endpoint);
    eq(left, ['https://alive/2']);
  });
  it('1 delete() recu par le mock sb', () => eq(sb._deleted.length, 1));
})();

console.log('\n▶ No sessions matching J+1');
await (async () => {
  const now = new Date('2026-04-22T18:00:00Z'); // J+1 = 23/04 jeudi
  const sb = makeSbMock({
    matches: [{ id: 'm1', match_date: '2026-04-25' }],
    training_plans: [{ match_id: 'm1', sessions: [{ type: 'lundi', title: 'S' }] }], // 20/04 pas 23/04
    push_subscriptions: [{ endpoint: 'x', p256dh: 'k', auth: 'a' }],
  });
  const wp = makeWebpushMock({});
  const r = await runCron(sb, wp, { now });
  it('reason = no sessions', () => eq(r.reason, 'no sessions'));
  it('sent = 0',              () => eq(r.sent, 0));
  it('aucun envoi webpush',   () => eq(wp._sent.length, 0));
})();

console.log('\n▶ No subscribers');
await (async () => {
  const now = new Date('2026-04-19T18:00:00Z');
  const sb = makeSbMock({
    matches: [{ id: 'm1', match_date: '2026-04-25' }],
    training_plans: [{ match_id: 'm1', sessions: [{ type: 'lundi', title: 'S' }] }],
    push_subscriptions: [],
  });
  const wp = makeWebpushMock({});
  const r = await runCron(sb, wp, { now });
  it('reason = no subscribers', () => eq(r.reason, 'no subscribers'));
  it('sent = 0',                () => eq(r.sent, 0));
})();

console.log('\n─────────────────────');
console.log(`  ${passed} passed, ${failed} failed`);
console.log('─────────────────────');
process.exit(failed ? 1 : 0);
