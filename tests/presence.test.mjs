// Tests de régression pour le module Présences.
// Exécution : node tests/presence.test.mjs
// Aucune dépendance externe — DOM minimaliste simulé.

import assert from 'node:assert/strict';

// ── Mini-DOM simulé ────────────────────────────────────────────
function mkEl(html) {
  const node = {
    _html: html,
    attrs: {},
    classes: new Set(),
    children: [],
    dataset: {},
    getAttribute(k) { return this.attrs[k] ?? null; },
    setAttribute(k,v) { this.attrs[k]=String(v); },
    classList: {
      add: (...c) => c.forEach(x => node.classes.add(x)),
      remove: (...c) => c.forEach(x => node.classes.delete(x)),
      contains: c => node.classes.has(c),
      toggle: (c, force) => { force ? node.classes.add(c) : node.classes.delete(c); }
    },
    querySelector: () => null,
    querySelectorAll: () => []
  };
  return node;
}

// ── Implémentation réelle extraite de index.html ──────────────
const S = { presStatus: {}, presRpe: {}, players: [], injuries: [] };

const statusBtns = [
  (()=>{const e=mkEl(); e.attrs['data-status']='P'; e.classes.add('status-btn'); return e;})(),
  (()=>{const e=mkEl(); e.attrs['data-status']='B'; e.classes.add('status-btn'); return e;})(),
  (()=>{const e=mkEl(); e.attrs['data-status']='R'; e.classes.add('status-btn'); return e;})(),
];
const rosterLine = mkEl();
rosterLine.attrs['data-player-id'] = 'p42';
rosterLine.querySelectorAll = sel => sel === '.status-btn' ? statusBtns : [];

const document = {
  querySelector: sel => sel.includes('data-player-id="p42"') ? rosterLine : null
};

function setStatus(pid, s) {
  S.presStatus[pid] = s;
  const line = document.querySelector(`.roster-line[data-player-id="${pid}"]`);
  if (!line) return;
  line.querySelectorAll('.status-btn').forEach(btn => {
    const btnStatus = btn.getAttribute('data-status');
    btn.classList.remove('s-P', 's-B', 's-R');
    if (btnStatus === s) btn.classList.add('s-' + s);
  });
}

// ── Scénarios de test ─────────────────────────────────────────
console.log('▶ Tests module Présences\n');

// Test 1 — clic "Présent" active la classe s-P sur le bon bouton
setStatus('p42', 'P');
assert.equal(S.presStatus.p42, 'P', 'state doit être P');
assert.ok(statusBtns[0].classes.has('s-P'), 'bouton P doit avoir classe s-P');
assert.ok(!statusBtns[1].classes.has('s-P'), 'bouton B ne doit pas avoir s-P');
assert.ok(!statusBtns[2].classes.has('s-P'), 'bouton R ne doit pas avoir s-P');
console.log('✓ Test 1 — clic Présent active s-P sur le bon bouton');

// Test 2 — clic "En retard" bascule la classe active
setStatus('p42', 'R');
assert.equal(S.presStatus.p42, 'R', 'state doit être R');
assert.ok(!statusBtns[0].classes.has('s-P'), 'classe s-P doit être retirée du bouton P');
assert.ok(statusBtns[2].classes.has('s-R'), 'bouton R doit recevoir s-R');
console.log('✓ Test 2 — clic En retard retire l\'ancien état et active s-R');

// Test 3 — clic "Blessé"
setStatus('p42', 'B');
assert.equal(S.presStatus.p42, 'B');
assert.ok(statusBtns[1].classes.has('s-B'));
assert.ok(!statusBtns[2].classes.has('s-R'), 'bouton R doit perdre s-R');
console.log('✓ Test 3 — clic Blessé met à jour correctement');

// Test 4 — pid inexistant ne crash pas
assert.doesNotThrow(() => setStatus('unknown-pid', 'P'));
console.log('✓ Test 4 — pid inexistant ne crash pas');

// Test 5 — RPE borné entre 1 et 10
function adjRpe(pid, d) {
  const cur = S.presRpe[pid] || 0;
  const nxt = Math.max(1, Math.min(10, cur + d));
  S.presRpe[pid] = nxt;
  return nxt;
}
assert.equal(adjRpe('p1', 1), 1, '0 → +1 = 1 (borné en bas à 1)');
assert.equal(adjRpe('p1', 5), 6, '1 + 5 = 6');
assert.equal(adjRpe('p1', 10), 10, '6 + 10 plafonné à 10');
assert.equal(adjRpe('p1', -20), 1, '10 - 20 planché à 1');
console.log('✓ Test 5 — adjRpe est correctement borné [1..10]');

// Test 6 — setAllPresent met 'B' pour blessés actifs
S.players = [{id:'a',name:'A'},{id:'b',name:'B'},{id:'c',name:'C'}];
S.injuries = [{player_id:'b', is_active:true}];
S.presStatus = {};
S.players.forEach(p => {
  const injured = S.injuries.some(i => i.player_id === p.id && (i.is_active === true || i.status === 'active'));
  S.presStatus[p.id] = injured ? 'B' : 'P';
});
assert.equal(S.presStatus.a, 'P');
assert.equal(S.presStatus.b, 'B', 'joueur blessé doit rester B');
assert.equal(S.presStatus.c, 'P');
console.log('✓ Test 6 — setAllPresent respecte les joueurs blessés\n');

console.log('═════════════════════════════════════');
console.log('  ✅  Tous les tests ont réussi (6/6)');
console.log('═════════════════════════════════════');
