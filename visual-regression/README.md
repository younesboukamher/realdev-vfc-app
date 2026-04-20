# Visual Regression — RealDev VFC

Playwright (Chromium + WebKit) avec Supabase 100% stubbé, dates gelées au `2026-04-20`, et 3 suites couvrant précisément les 5 bugs du rapport `QA_2026-04-20.md`.

## Install

```bash
cd visual-regression
npm install
npx playwright install chromium         # ~180 MB une fois
# (optionnel multi-browser) : npx playwright install
```

## Run

```bash
# 1. Premiere fois — genere les baselines
INDEX_PATH=../../realdev-vfc-app npm run test:update

# 2. Ensuite, a chaque changement d'index.html
INDEX_PATH=../../realdev-vfc-app npm test

# 3. Debug interactif
INDEX_PATH=../../realdev-vfc-app npm run test:ui
```

`INDEX_PATH` pointe vers le dossier contenant `index.html` (celui de ton clone `realdev-vfc-app`). Le serveur statique `serve.mjs` le servira sur `http://127.0.0.1:4173`.

## Structure

```
visual-regression/
├── package.json
├── playwright.config.mjs     # 1 projet iPhone 17 Pro 402×874 (extensible)
├── serve.mjs                 # static server — sert INDEX_PATH sur :4173
├── fixtures/
│   ├── fixtures.mjs          # donnees figees (joueurs, matchs, presences…)
│   ├── supabase-mock.mjs     # page.route() pour /auth, /rest, /functions, /realtime
│   └── helpers.mjs           # setupPage + loginAsCoach + gotoTab
└── tests/
    ├── home.spec.mjs         # Bug #1 (modal leak) + Bug #2 (next match)
    ├── planning.spec.mjs     # Bug #3 (open on past) + Bug #4 (calendar sessions)
    └── presences.spec.mjs    # Bug #5 (nom ecrase le btn Present)
```

## Couverture — chaque test mappe un bug du rapport

| Test | Bug cible | Assertion |
|------|-----------|-----------|
| `home.spec.mjs::no stray modal leak below the fold` | #1 modal Pd2 | `.modal:not(.on):visible` → 0 |
| `home.spec.mjs::next match widget points to future date` | #2 nextMatch | body contient `J17`, pas `J16` |
| `home.spec.mjs::screenshot full page (baseline)` | regression visuelle generale | diff < 120 px |
| `planning.spec.mjs::opens on the next match, not a past one` | #3 | titre ≠ `J16` |
| `planning.spec.mjs::calendar month view shows sessions` | #4 | `.cal-session-dot` > 0 |
| `presences.spec.mjs::long player names never overlap btn Present` | #5 | `nameRight ≤ btnLeft` + ellipsis |

Les assertions visuelles (`toHaveScreenshot`) sont complementaires des assertions DOM/CSS — si l'UI change legitimement, on met à jour le baseline via `npm run test:update`.

## Gestion des baselines

Les screenshots sont stockes dans `tests/__screenshots__/` et commites. Quand l'UI change intentionnellement :

```bash
npm run test:update
git add tests/__screenshots__
git commit -m "chore(vr): update visual baseline after feature X"
```

## Integration CI

À ajouter dans `.github/workflows/qa.yml` :

```yaml
name: QA
on: [pull_request, push]
jobs:
  visual-regression:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: cd visual-regression && npm ci && npx playwright install --with-deps chromium
      - run: cd visual-regression && INDEX_PATH=.. npm test
      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: visual-regression/playwright-report/
```

## Pourquoi ces choix

- **Supabase stubbe** → 100% offline, zero dependance reseau, tests deterministes.
- **Dates gelees** → `2026-04-20` permet d'avoir un "J17" futur et un "J16" passe stables.
- **Animations desactivees** → `animation-duration: 0s` + `threshold: 0.15` evite la flakyness due aux transitions CSS.
- **viewport 402×874** → reproduit exactement le bug iPhone 17 Pro signale dans le rapport.
- **1 worker** → screenshots deterministes (pas de race entre tests).

## Limites connues

- Les tests ne valident pas les flows multi-etapes (saisie match, ajout joueur…) — ce scope appartient a des tests E2E fonctionnels (suite separee à batir plus tard).
- Le service worker n'est pas teste (le stub bypass). Pour tester le SW, ajouter un test `sw.spec.mjs` qui n'active pas le mock.
- WebKit (Safari) n'est pas dans la config par defaut — ajouter le project si on veut couvrir iOS reel.
