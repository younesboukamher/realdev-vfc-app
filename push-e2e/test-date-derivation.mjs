// Test unitaire offline — verifie que la logique de derivation de date :
//   (1) retourne le bon ISO pour chaque combinaison match_date x session type
//   (2) recule toujours AVANT le match
//   (3) recule de 7 jours si coincidence du day-of-week
//   (4) preserve la priorite au champ date explicite
//   (5) selectionne correctement les sessions de J+1 pour le cron
//
// Invariant de parite : la logique Edge Function (TS) et la logique frontend
// (pl2BuildMonthData dans index.html) doivent avoir le MEME dayIdxOfType.
// Un test statique verifie que le mapping code est identique.

import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import {
  DAY_IDX_OF_TYPE, deriveSessionDate, sessionsForDate,
} from './derivation.mjs';

let passed = 0, failed = 0;
function it(name, fn) {
  try { fn(); console.log(`  ✓ ${name}`); passed++; }
  catch (e) { console.log(`  ✗ ${name}\n    ${e.message}`); failed++; }
}
function eq(a, b, msg) {
  const aj = JSON.stringify(a), bj = JSON.stringify(b);
  if (aj !== bj) throw new Error(`${msg || ''}\n     got: ${aj}\n     expected: ${bj}`);
}

console.log('\n▶ deriveSessionDate — cas nominal');

// Saison 2025-2026, match samedi 25 avril 2026, seances en semaine :
// 25/04/2026 = samedi (dow=6)
it('samedi 25/04 + mardi → mardi 21/04', () => {
  eq(deriveSessionDate('2026-04-25', 'mardi'), '2026-04-21');
});
it('samedi 25/04 + jeudi → jeudi 23/04', () => {
  eq(deriveSessionDate('2026-04-25', 'jeudi'), '2026-04-23');
});
it('samedi 25/04 + lundi → lundi 20/04', () => {
  eq(deriveSessionDate('2026-04-25', 'lundi'), '2026-04-20');
});
it('samedi 25/04 + vendredi → vendredi 24/04', () => {
  eq(deriveSessionDate('2026-04-25', 'vendredi'), '2026-04-24');
});

console.log('\n▶ deriveSessionDate — coincidence day-of-week (-7j)');

it('samedi 25/04 + samedi → samedi 18/04 (recule de 7j, session AVANT match)', () => {
  eq(deriveSessionDate('2026-04-25', 'samedi'), '2026-04-18');
});
it('dimanche 26/04 + dimanche → dimanche 19/04', () => {
  eq(deriveSessionDate('2026-04-26', 'dimanche'), '2026-04-19');
});

console.log('\n▶ deriveSessionDate — traversee de mois');

it('dimanche 03/05 + vendredi → vendredi 01/05', () => {
  eq(deriveSessionDate('2026-05-03', 'vendredi'), '2026-05-01');
});
it('dimanche 03/05 + samedi → samedi 02/05', () => {
  eq(deriveSessionDate('2026-05-03', 'samedi'), '2026-05-02');
});
it('dimanche 03/05 + lundi → lundi 27/04', () => {
  eq(deriveSessionDate('2026-05-03', 'lundi'), '2026-04-27');
});

console.log('\n▶ deriveSessionDate — cas invalides');

it('type inconnu → null', () => eq(deriveSessionDate('2026-04-25', 'holiday'), null));
it('type vide → null', () => eq(deriveSessionDate('2026-04-25', ''), null));
it('match_date vide → null', () => eq(deriveSessionDate('', 'mardi'), null));
it('match_date invalide → null', () => eq(deriveSessionDate('not-a-date', 'mardi'), null));

console.log('\n▶ deriveSessionDate — invariant metier');

it('la seance est TOUJOURS avant le match (tous types)', () => {
  const matchISO = '2026-04-25';
  for (const type of Object.keys(DAY_IDX_OF_TYPE)) {
    const d = deriveSessionDate(matchISO, type);
    if (!d) throw new Error('null for ' + type);
    if (d >= matchISO) throw new Error(`${type}: derived ${d} >= match ${matchISO}`);
  }
});

console.log('\n▶ sessionsForDate — selection des sessions de J+1');

const plans = [
  { match_id: 'm1', sessions: [
    { type: 'mardi',  title: 'Activation',     time: '19:00', location: 'Gym A' },
    { type: 'jeudi',  title: 'Tactical',       time: '19:00', location: 'Gym A' },
    { type: 'samedi', title: 'Activation J-1', time: '18:00', location: 'Gym A' }, // coincide → -7j → 18/04
  ]},
  { match_id: 'm2', sessions: [
    { type: 'lundi',    title: 'Strength',       time: '18:30', location: 'Gym B' },
    { type: 'mercredi', title: 'Recovery',       time: '18:00', location: 'Field' },
  ]},
];
const matchDateById = { m1: '2026-04-25', m2: '2026-05-02' };

it('J+1 = 2026-04-21 → retourne la seance mardi de m1', () => {
  const hits = sessionsForDate(plans, matchDateById, '2026-04-21');
  eq(hits.length, 1);
  eq(hits[0].match_id, 'm1');
  eq(hits[0].session.type, 'mardi');
});

it('J+1 = 2026-04-23 → retourne la seance jeudi de m1', () => {
  const hits = sessionsForDate(plans, matchDateById, '2026-04-23');
  eq(hits.length, 1);
  eq(hits[0].session.type, 'jeudi');
});

it('J+1 = 2026-04-18 → retourne la seance samedi de m1 (coincidence -7j)', () => {
  const hits = sessionsForDate(plans, matchDateById, '2026-04-18');
  eq(hits.length, 1);
  eq(hits[0].session.type, 'samedi');
  eq(hits[0].session.title, 'Activation J-1');
});

it('J+1 = 2026-04-27 → retourne la seance lundi de m2', () => {
  const hits = sessionsForDate(plans, matchDateById, '2026-04-27');
  eq(hits.length, 1);
  eq(hits[0].match_id, 'm2');
});

it('J+1 sans seance → []', () => {
  eq(sessionsForDate(plans, matchDateById, '2026-04-22'), []);
});

console.log('\n▶ sessionsForDate — date explicite prioritaire');

const plansExplicit = [
  { match_id: 'm3', sessions: [
    { type: 'mardi', date: '2026-04-30', title: 'Adhoc' }, // date explicite — non derivee
  ]},
];
it('date explicite prime sur la derivation', () => {
  const hits = sessionsForDate(plansExplicit, { m3: '2026-05-02' }, '2026-04-30');
  eq(hits.length, 1);
  eq(hits[0].session.title, 'Adhoc');
});
it('date explicite non-matching → non retournee (evite double compte)', () => {
  // m3 samedi 02/05 + mardi → derive 2026-04-28. Mais la session a date=2026-04-30.
  // Donc pour 2026-04-28, la session ne doit PAS remonter.
  const hits = sessionsForDate(plansExplicit, { m3: '2026-05-02' }, '2026-04-28');
  eq(hits.length, 0);
});

console.log('\n▶ Parite — mapping dayIdxOfType entre Edge Fn et frontend');

const repoRoot = resolve(process.env.REPO_ROOT || '../../realdev-vfc-app');
function loadOrSkip(p, label) {
  try { return readFileSync(p, 'utf8'); }
  catch (e) { return null; }
}

const edgeSrc = loadOrSkip(`${repoRoot}/supabase/functions/send-pre-session-notifications/index.ts`);
const frontSrc = loadOrSkip(`${repoRoot}/index.html`);

it('mapping dayIdxOfType identique dans Edge Fn (TS) et frontend (pl2BuildMonthData)', () => {
  if (!edgeSrc || !frontSrc) {
    console.log('    (skip — REPO_ROOT non trouve : set REPO_ROOT=chemin/vers/realdev-vfc-app)');
    return;
  }
  // Extraire les objets dayIdxOfType ... { ... }
  const extract = (src) => {
    const re = /dayIdxOfType[^{]*\{([^}]+)\}/m;
    const m = src.match(re);
    if (!m) throw new Error('dayIdxOfType pas trouve');
    // Normaliser : supprimer types TS, espaces, commentaires
    const body = m[1]
      .replace(/\/\/[^\n]*/g, '')
      .replace(/\s+/g, '')
      .replace(/:\s*number/g, '')
      .replace(/,$/, '');
    const kv = {};
    body.split(',').filter(Boolean).forEach((pair) => {
      const [k, v] = pair.split(':');
      kv[k.trim()] = Number(v);
    });
    return kv;
  };
  const a = extract(edgeSrc);
  const b = extract(frontSrc);
  // Doit etre identique au mapping cote derivation.mjs
  eq(a, Object.fromEntries(Object.entries(DAY_IDX_OF_TYPE)));
  eq(b, Object.fromEntries(Object.entries(DAY_IDX_OF_TYPE)));
});

console.log('\n─────────────────────');
console.log(`  ${passed} passed, ${failed} failed`);
console.log('─────────────────────');
process.exit(failed ? 1 : 0);
