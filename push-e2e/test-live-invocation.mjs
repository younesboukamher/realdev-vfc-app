// Test d'invocation live de l'Edge Function send-pre-session-notifications.
// Requiert :
//   SUPABASE_URL            ex: https://jgytwvtdqpotdaleotok.supabase.co
//   SUPABASE_SERVICE_ROLE_KEY  (Project Settings > API > service_role)
//
// Lecture seule : N'ECRIT rien, n'envoie PAS de notifications vers les
// subscribers reels — la fonction Edge elle-meme envoie les webpush, donc
// a defaut de pouvoir "dry-run" cote serveur, ce harness :
//   1. verifie que l'Edge Function repond (auth + deploy OK)
//   2. verifie le shape de la reponse (clefs attendues)
//   3. si sent>0 / sessions>0 en prod, log les volumes pour diag
//
// IMPORTANT : pour un vrai test fonctionnel end-to-end, il faut
//   (a) deployer une copie de la fonction sous un nom temporaire
//       (`send-pre-session-notifications-test`) qui ecrit dans une table
//       `push_notifications_log` au lieu d'appeler webpush,
//   (b) ou faire tourner la fonction en local via `supabase functions serve`
//       avec des secrets VAPID de test.
// Ces approches sont documentees dans README.md section "Deploy test Fn".

const URL = process.env.SUPABASE_URL;
const KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!URL || !KEY) {
  console.error('❌ SUPABASE_URL et SUPABASE_SERVICE_ROLE_KEY requis.');
  console.error('   Exemple :');
  console.error('     SUPABASE_URL=https://xxx.supabase.co \\');
  console.error('     SUPABASE_SERVICE_ROLE_KEY=eyJ... \\');
  console.error('     node test-live-invocation.mjs');
  process.exit(2);
}

const endpoint = `${URL.replace(/\/$/, '')}/functions/v1/send-pre-session-notifications`;

let passed = 0, failed = 0;
function it(name, cond, detail = '') {
  if (cond) { console.log(`  ✓ ${name}`); passed++; }
  else      { console.log(`  ✗ ${name}${detail ? '\n    ' + detail : ''}`); failed++; }
}

(async () => {
  console.log(`\n▶ POST ${endpoint}`);
  let res, json, rawText;
  try {
    res = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${KEY}`,
        'content-type': 'application/json',
      },
      body: '{}',
    });
    rawText = await res.text();
    try { json = JSON.parse(rawText); } catch (_) { json = null; }
  } catch (e) {
    console.log(`  ✗ fetch a plante : ${e.message}`);
    process.exit(1);
  }

  it('response code 2xx', res.status >= 200 && res.status < 300, `got ${res.status} — body: ${rawText.slice(0, 200)}`);
  it('response est du JSON', !!json, `body: ${rawText.slice(0, 200)}`);

  if (json) {
    it('payload contient ok:true', json.ok === true, `ok=${json.ok}  error=${json.error || ''}`);
    it('payload contient date: ISO YYYY-MM-DD', typeof json.date === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(json.date), `date=${json.date}`);
    it('payload contient sent: number', typeof json.sent === 'number', `sent=${json.sent}`);
    // Les 2 champs suivants sont optionnels selon l'etat (no-sessions / no-subs)
    if ('sessions' in json) {
      it('sessions est un nombre ≥ 0', typeof json.sessions === 'number' && json.sessions >= 0);
    }
    if ('subs' in json) {
      it('subs est un nombre ≥ 0', typeof json.subs === 'number' && json.subs >= 0);
    }
    if ('cleanedUp' in json) {
      it('cleanedUp est un nombre ≥ 0', typeof json.cleanedUp === 'number' && json.cleanedUp >= 0);
    }

    console.log('\n▶ Diagnostic runtime');
    console.log(`  date cible    : ${json.date}`);
    console.log(`  sessions J+1  : ${json.sessions ?? '(pas de cle — reason: ' + json.reason + ')'}`);
    console.log(`  subscribers   : ${json.subs ?? '(pas de cle)'}`);
    console.log(`  notifications : ${json.sent} envoyees, ${json.cleanedUp ?? 0} purgees`);
  }

  console.log('\n─────────────────────');
  console.log(`  ${passed} passed, ${failed} failed`);
  console.log('─────────────────────');
  process.exit(failed ? 1 : 0);
})();
