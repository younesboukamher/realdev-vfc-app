// Contract test for generateMicrocycle() sessions.
// ------------------------------------------------
// The Pl2 calendar bug (2026-04-20) happened because sessions produced by
// generateMicrocycle() have only a `type` (lundi/mardi/...) but NO `date`,
// and pl2BuildMonthData naively looked for `s.date || s.session_date`. All
// sessions were dropped from the calendar.
//
// This test freezes two invariants:
//   1. Every session from generateMicrocycle() must have a `type` in the
//      ALLOWED set OR a valid `date` string. No session should be
//      silently malformed (empty type, typo day name, etc.).
//   2. pl2BuildMonthData() in index.html must contain a dayIdxOfType fallback
//      so that it can place type-only sessions on the calendar. This is a
//      static check — it freezes the fix and prevents regressions from a
//      future 'cleanup' that accidentally removes the fallback.
//
// Run: node tests/generate-microcycle.test.mjs

import { readFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import assert from 'node:assert/strict';

const __dirname = dirname(fileURLToPath(import.meta.url));
const indexPath = resolve(__dirname, '..', 'index.html');
const src = readFileSync(indexPath, 'utf8');

// ─── 1. Extract generateMicrocycle + dependencies from index.html ───
function extractFn(name) {
  // Accept: function NAME(...), window.NAME = function(...),
  // const/let/var NAME = function(...).
  const patterns = [
    new RegExp('function\\s+' + name + '\\s*\\('),
    new RegExp('window\\.' + name + '\\s*=\\s*function\\s*\\('),
    new RegExp('(?:const|let|var)\\s+' + name + '\\s*=\\s*function\\s*\\('),
  ];
  let m = null;
  for (const re of patterns) { m = src.match(re); if (m) break; }
  if (!m) throw new Error('function not found: ' + name);
  const start = m.index;
  // Find the first '{' after the signature
  let i = src.indexOf('{', start);
  if (i < 0) throw new Error('missing body for ' + name);
  let depth = 0;
  for (; i < src.length; i++) {
    const c = src[i];
    if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) { i++; break; } }
    else if (c === "'" || c === '"' || c === '`') {
      const q = c; i++;
      while (i < src.length && src[i] !== q) {
        if (src[i] === '\\') i++;
        i++;
      }
    }
  }
  return src.slice(start, i);
}

// Build a minimal sandbox: we need EXERCISE_LIBRARY and analyzeOpponent.
// Grab them the same way and evaluate the bundle.
const src_lib   = src.match(/const\s+EXERCISE_LIBRARY\s*=\s*\{[\s\S]*?\n\};/);
assert(src_lib, 'EXERCISE_LIBRARY const not found in index.html');
const src_anal  = extractFn('analyzeOpponent');
const src_gen   = extractFn('generateMicrocycle');

// Evaluate into a local scope. eval + new Function avoids any global leak.
const bundle = src_lib[0] + '\n' + src_anal + '\n' + src_gen + '\nreturn { generateMicrocycle, analyzeOpponent, EXERCISE_LIBRARY };';
const { generateMicrocycle } = new Function(bundle)();

// ─── 2. Runtime contract ───
console.log('▶ Contract test — generateMicrocycle()');

const ALLOWED_TYPES = new Set(['lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche']);
function isValidDate(s) {
  if (typeof s !== 'string' || !s) return false;
  const d = new Date(s);
  return Number.isFinite(d.getTime());
}

const cases = [
  { label: 'empty scouting',         scouting: null },
  { label: 'scouting without opponent', scouting: { } },
  { label: 'full scouting',          scouting: { opponent_name: 'FC Test', style: 'counter', strengths: 'pressing haut et transitions rapides' } },
];

let pass = 0, fail = 0;
function check(desc, fn) {
  try { fn(); pass++; console.log('  \u2713 ' + desc); }
  catch (e) { fail++; console.error('  \u2717 ' + desc + '\n      ' + e.message); }
}

for (const c of cases) {
  const out = generateMicrocycle(c.scouting);
  check('[' + c.label + '] returns { sessions, analysis }', () => {
    assert(out && Array.isArray(out.sessions), 'no sessions array');
    assert(out.sessions.length >= 1, 'empty sessions');
  });
  check('[' + c.label + '] every session has type in ALLOWED or a valid date', () => {
    for (const s of out.sessions) {
      const hasType = typeof s.type === 'string' && ALLOWED_TYPES.has(s.type);
      const hasDate = isValidDate(s.date) || isValidDate(s.session_date);
      assert(hasType || hasDate, 'session missing type AND date: ' + JSON.stringify(s));
    }
  });
  check('[' + c.label + '] every session has label, duration, rpe_target', () => {
    for (const s of out.sessions) {
      assert(typeof s.label === 'string' && s.label, 'no label: ' + JSON.stringify(s));
      assert(Number.isFinite(s.duration) && s.duration > 0, 'bad duration: ' + JSON.stringify(s));
      assert(typeof s.rpe_target === 'string' && s.rpe_target, 'no rpe_target');
    }
  });
  check('[' + c.label + '] no duplicate session types', () => {
    const seen = new Set();
    for (const s of out.sessions) {
      assert(!seen.has(s.type), 'duplicate type: ' + s.type);
      seen.add(s.type);
    }
  });
}

// ─── 3. Static regression check on pl2BuildMonthData ───
console.log('\n\u25b6 Regression — pl2BuildMonthData dayIdxOfType fallback');
const pl2Fn = extractFn('pl2BuildMonthData');
check('pl2BuildMonthData uses dayIdxOfType mapping', () => {
  assert(/dayIdxOfType\s*=\s*\{\s*dimanche/.test(pl2Fn) || /dayIdxOfType\[/.test(pl2Fn),
    'pl2BuildMonthData lost its dayIdxOfType fallback — calendar will drop type-only sessions');
});
check('pl2BuildMonthData references match_date for date derivation', () => {
  assert(/match_date/.test(pl2Fn), 'pl2BuildMonthData no longer references match_date — date derivation broken');
});

// ─── Summary ───
console.log('\n' + (fail ? ('\u274c ' + fail + ' failure(s) / ' + pass + ' pass') : ('\u2705 ' + pass + ' checks passed')));
process.exit(fail ? 1 : 0);
