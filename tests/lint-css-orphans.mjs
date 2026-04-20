// CSS orphan-class linter
// -----------------------
// Scans index.html for class tokens used in HTML attributes and JS, then
// compares them against CSS class selectors defined in <style> blocks AND
// in JS template literals (e.g. the PDF export cssPopup).
// Any class used without any matching rule is flagged as an orphan.
// Exits 0 if no orphans (or only whitelisted ones), 1 otherwise.
// Run: node tests/lint-css-orphans.mjs [path/to/file.html]

import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

const FILE = process.argv[2] || resolve(process.cwd(), 'index.html');

// Classes intentionally not styled (JS hooks, transient states).
const WHITELIST = new Set([
  'hidden',   // HTML global attribute styling
  'js-hook',  // Convention: JS-only selector prefix
  'pending',  // Transient state
  'loading',  // Transient state
]);

let src;
try { src = readFileSync(FILE, 'utf8'); }
catch (e) { console.error('[lint-css] cannot read ' + FILE + ': ' + e.message); process.exit(2); }

// ── Regexes ──
const HTML_CLASS_RE     = /\bclass\s*=\s*(?:"([^"]*)"|'([^']*)')/g;
const CLIST_HEAD_RE     = /\bclassList\s*\.\s*(add|remove|toggle|contains|replace)\s*\(/g;
const CNAME_RE          = /\.className\s*(?:\+?=)\s*(['"`])([^'"`]*?)\1/g;
const TEMPLATE_CLASS_RE = /\bclass\s*=\s*(?:"[^"]*\$\{[^}]*\}[^"]*"|'[^']*\$\{[^}]*\}[^']*')/g;
const QS_RE             = /\b(?:querySelector|querySelectorAll|closest|matches)\s*\(\s*(['"`])([^'"`]+?)\1/g;
const IDENT_RE          = /^[-A-Za-z_][\w-]*$/;

// Balanced-paren scan — returns the substring between matching parens given
// the index of the opening '('.
function scanBalanced(text, openIdx) {
  let depth = 0;
  for (let i = openIdx; i < text.length; i++) {
    const c = text[i];
    if (c === '(') depth++;
    else if (c === ')') {
      depth--;
      if (depth === 0) return text.slice(openIdx + 1, i);
    } else if (c === "'" || c === '"' || c === '`') {
      // Skip over quoted strings
      const quote = c;
      i++;
      while (i < text.length && text[i] !== quote) {
        if (text[i] === '\\') i++; // skip escape
        i++;
      }
    }
  }
  return '';
}

// Extract only the TOP-LEVEL quoted string args from an arg list (depth 0,
// not inside nested parens). This filters out things like getAttribute('x').
function topLevelQuotedArgs(text) {
  const out = [];
  let depth = 0;
  let i = 0;
  while (i < text.length) {
    const c = text[i];
    if (c === '(') depth++;
    else if (c === ')') depth--;
    else if ((c === "'" || c === '"' || c === '`') && depth === 0) {
      const quote = c;
      const start = i + 1;
      i++;
      while (i < text.length && text[i] !== quote) {
        if (text[i] === '\\') i++;
        i++;
      }
      // Concat heuristic — skip if adjacent to '+' in original
      const prev = start >= 2 ? text[start - 2] : '';
      const next = text[i + 1] || '';
      const isConcat = prev === '+' || next === '+';
      if (!isConcat) out.push(text.slice(start, i));
    }
    i++;
  }
  return out;
}

// ── Step 1: collect CSS class selectors ──
// 1a — from <style> blocks (handles both real HTML and JS template-literal
// <style> blocks since we match the raw source).
const styleBlocks = [...src.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)].map(m => m[1]);
const cssText = styleBlocks.join('\n').replace(/\/\*[\s\S]*?\*\//g, '');
const CSS_CLASS_RE = /(?<![\w-])\.(-?[A-Za-z_][\w-]*)/g;
const definedClasses = new Set();
for (const m of cssText.matchAll(CSS_CLASS_RE)) definedClasses.add(m[1]);

// 1b — CSS rules embedded anywhere in source (e.g. PDF cssPopup template
// literal). Forward lookahead for CSS-selector-context chars; no lookbehind
// so compound selectors (.foo.bar) resolve both sides.
const EMBEDDED_CSS_RE = /\.(-?[A-Za-z_][\w-]*)(?=\s*(?:\{|,|\.|:[a-zA-Z:]|::|\[|>|\+|~|\s+[.#:a-zA-Z]))/g;
for (const m of src.matchAll(EMBEDDED_CSS_RE)) definedClasses.add(m[1]);

// ── Step 2: collect class usages ──
const usedClasses = new Map();
function record(cls, source, line, snippet) {
  if (!usedClasses.has(cls)) usedClasses.set(cls, []);
  if (usedClasses.get(cls).length < 3) usedClasses.get(cls).push({ source, line, snippet });
}
function lineOf(idx) {
  let n = 1;
  for (let i = 0; i < idx && i < src.length; i++) if (src[i] === '\n') n++;
  return n;
}
function snippetAt(idx, len = 80) {
  const start = Math.max(0, idx - 10);
  const s = src.slice(start, idx + len).replace(/\s+/g, ' ').trim();
  return s.length > 120 ? s.slice(0, 120) + '...' : s;
}
function isIdent(tok) {
  if (!IDENT_RE.test(tok)) return false;
  // Reject tokens ending with '-' (concat fragments like 's-' in 's-'+s)
  if (tok.endsWith('-')) return false;
  return true;
}

// 2a — class="..." straight strings
for (const m of src.matchAll(HTML_CLASS_RE)) {
  const value = m[1] ?? m[2] ?? '';
  if (value.includes('${')) continue;
  for (const tok of value.split(/\s+/)) {
    if (!tok || !isIdent(tok)) continue;
    record(tok, 'html', lineOf(m.index), snippetAt(m.index));
  }
}

// 2b — classList.add/remove/toggle/contains/replace (balanced-paren)
for (const m of src.matchAll(CLIST_HEAD_RE)) {
  const method = m[1];
  const openIdx = m.index + m[0].length - 1; // position of '('
  const args = scanBalanced(src, openIdx);
  if (!args) continue;
  const quoted = topLevelQuotedArgs(args);
  // For toggle(cls, cond) only the first arg is a class. Same for contains.
  // For add/remove/replace, all quoted args are classes (replace swaps two).
  const argsToConsider = (method === 'toggle' || method === 'contains')
    ? quoted.slice(0, 1) : quoted;
  for (const raw of argsToConsider) {
    if (raw.includes('${')) continue;
    for (const t of raw.split(/\s+/)) {
      if (!t || !isIdent(t)) continue;
      record(t, 'js:classList', lineOf(m.index), snippetAt(m.index));
    }
  }
}

// 2c — .className = ...
for (const m of src.matchAll(CNAME_RE)) {
  const value = m[2];
  if (value.includes('${')) continue;
  for (const t of value.split(/\s+/)) {
    if (!t || !isIdent(t)) continue;
    record(t, 'js:className', lineOf(m.index), snippetAt(m.index));
  }
}

// 2d — class="..." inside template literals with ${...}
for (const m of src.matchAll(TEMPLATE_CLASS_RE)) {
  const chunk = m[0];
  const stripped = chunk.replace(/\$\{[^}]*\}/g, ' ');
  const inner = stripped.match(/class\s*=\s*(?:"([^"]*)"|'([^']*)')/);
  if (!inner) continue;
  const value = inner[1] ?? inner[2] ?? '';
  for (const tok of value.split(/\s+/)) {
    if (!tok || !isIdent(tok)) continue;
    record(tok, 'js:template', lineOf(m.index), snippetAt(m.index));
  }
}

// 2e — querySelector('.foo') → treat as defined
for (const m of src.matchAll(QS_RE)) {
  for (const c of m[2].matchAll(EMBEDDED_CSS_RE)) definedClasses.add(c[1]);
  for (const c of m[2].matchAll(CSS_CLASS_RE)) definedClasses.add(c[1]);
}

// ── Step 3: diff ──
const orphans = [];
for (const [cls, refs] of usedClasses) {
  if (definedClasses.has(cls)) continue;
  if (WHITELIST.has(cls)) continue;
  orphans.push({ cls, count: refs.length, refs });
}
orphans.sort((a, b) => a.cls.localeCompare(b.cls));

const used = usedClasses.size;
const defined = definedClasses.size;

if (orphans.length === 0) {
  console.log('[lint-css] OK - ' + used + ' classes used, ' + defined + ' selectors defined, 0 orphans.');
  process.exit(0);
}

console.error('[lint-css] FAIL - ' + orphans.length + ' orphan class(es) used without any CSS rule.');
console.error('           (' + used + ' classes used, ' + defined + ' selectors defined)');
console.error('');
for (const o of orphans) {
  console.error('  * .' + o.cls + '   (' + o.count + ' occurrence' + (o.count > 1 ? 's' : '') + ')');
  for (const r of o.refs) {
    console.error('      ' + r.source + ' L' + r.line + ': ' + r.snippet);
  }
}
console.error('');
console.error('Fix options:');
console.error('  1. Add a CSS rule for the class in an existing <style> block.');
console.error('  2. Remove the class usage if it was a typo or dead code.');
console.error('  3. If intentionally unstyled (JS hook), add to WHITELIST with a comment.');

process.exit(1);
