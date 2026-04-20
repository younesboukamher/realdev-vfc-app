// Minimal test runner — exit non-zero if any test fails.
// Run: node tests/run-all.mjs
import { spawnSync } from 'node:child_process';
import { readdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const tests = readdirSync(__dirname)
  .filter(f => (f.endsWith('.test.mjs') || f.startsWith('lint-')) && f !== 'run-all.mjs')
  .sort();

let failed = 0;
for (const t of tests) {
  const p = resolve(__dirname, t);
  console.log('\n=== ' + t + ' ===');
  const r = spawnSync('node', [p], { stdio: 'inherit' });
  if (r.status !== 0) { failed++; console.error('FAILED: ' + t); }
}

console.log('\n' + (failed ? ('[run-all] ' + failed + ' failure(s)') : '[run-all] all tests passed'));
process.exit(failed ? 1 : 0);
