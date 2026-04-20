## Push E2E — send-pre-session-notifications

Trois tests complementaires pour l'Edge Function des notifications pre-seance (#132 backlog). Tous ne necessitent aucune dependance npm (zero-install, Node 20+).

### Architecture — 3 niveaux

| Niveau | Fichier | Reseau ? | Quoi |
|---|---|---|---|
| **Unit** | `test-date-derivation.mjs` | non | Logique pure de derivation de date (port TS → JS). 22 assertions. |
| **Simulation** | `test-local-simulation.mjs` | non | Flow Edge Fn complet avec Supabase + web-push mockes en memoire. 13 assertions. |
| **Live** | `test-live-invocation.mjs` | oui | POST vers la fonction deployee. Verifie auth + shape de la reponse. |

`derivation.mjs` est la **source unique de verite** de la logique metier (reproduisant a l'identique `index.ts` de l'Edge Fn). Un des tests verifie statiquement que le mapping `dayIdxOfType` de `derivation.mjs` colle avec celui de `index.ts` ET celui de `pl2BuildMonthData` dans `index.html` → si l'un des trois derive, le test casse.

### Run

```bash
cd push-e2e

# Unit + simulation (offline, deterministe, < 1s)
REPO_ROOT=../../realdev-vfc-app npm test

# Unit seul
REPO_ROOT=../../realdev-vfc-app npm run test:unit

# Simulation seule
npm run test:sim

# Live (requiert acces Supabase)
SUPABASE_URL=https://jgytwvtdqpotdaleotok.supabase.co \
SUPABASE_SERVICE_ROLE_KEY=eyJ... \
npm run test:live

# Tout
REPO_ROOT=../../realdev-vfc-app \
SUPABASE_URL=... \
SUPABASE_SERVICE_ROLE_KEY=... \
npm run test:all
```

### Ce qui est teste

**derivation** (22 checks) : cas nominal par jour, coincidence day-of-week → -7j, traversee de mois, entrees invalides (type inconnu, date malformee, vide), invariant metier "seance toujours avant match", priorite date explicite, parite des 3 mappings `dayIdxOfType`.

**simulation** (13 checks) : happy path (3 subs → 3 sent), cleanup auto des endpoints 410, message body compose (title/time/location), tag unique par date, cas no-sessions, cas no-subscribers, rien n'est envoye si les subs/sessions sont absents.

**live** (≤ 6 checks selon reponse) : 2xx, JSON valide, `ok:true`, `date: ISO`, `sent: number`, `sessions / subs / cleanedUp` si presents. Diagnostic imprime les volumes reels en prod.

### Limites du test live

L'Edge Fn n'a pas de mode "dry-run". Appeler l'endpoint en prod **envoie potentiellement des notifications reelles** a toute personne abonnee. Pour un vrai E2E isole, deux options :

**Option A — Copie deployee sous un autre nom**

1. `cp supabase/functions/send-pre-session-notifications supabase/functions/send-pre-session-notifications-test`
2. Dans `-test/index.ts` : remplacer `webpush.sendNotification(...)` par un `INSERT` dans une table `push_notifications_log` (id, endpoint, payload, at).
3. Deployer : `supabase functions deploy send-pre-session-notifications-test`
4. Adapter `test-live-invocation.mjs` → lire la table log apres invocation, asserter nb lignes = nb subs.

**Option B — `supabase functions serve` local**

1. `supabase functions serve send-pre-session-notifications --env-file .env.test`
2. `.env.test` avec VAPID keys de test + Supabase local (`supabase start`).
3. Seed de donnees via `supabase db reset` + `seeds.sql` (fixture 1 match + 1 plan + 1 sub avec endpoint `http://localhost:4443/webhook`).
4. Demarrer un petit receveur HTTP local ecoutant `:4443/webhook` et comptant les POSTs.
5. Invoquer `curl localhost:54321/functions/v1/send-pre-session-notifications`.
6. Asserter : 1 POST recu sur le receveur, payload contient le bon titre.

Option A est plus simple pour CI (tourne contre Supabase prod avec une table log dediee). Option B tourne en isolation totale mais requiert `supabase` CLI + `supabase start` + Deno.

### Couverture anti-regression

Ces tests blindent specifiquement contre le **Bug #4 QA 2026-04-20** et son jumeau cote Edge Fn corrige en #131 :

| Regression possible | Detectee par |
|---|---|
| Mapping day-of-week decale (ex. lundi=0 au lieu de 1) | test unit + test parite mapping |
| Oubli du "-7j quand coincidence" | test unit (case samedi+samedi) |
| Seance derivee APRES le match | test unit (invariant metier) |
| Session avec `date:` explicite double-comptee | test unit (date explicite prioritaire) |
| Edge Fn qui envoie 0 notifications alors que des plans existent | test sim (happy path) |
| Subscription 410 jamais purgee | test sim (cleanup) |
| Payload sans `tag` → notifications s'empilent | test sim (tag unique) |
| Drift entre Edge Fn TS et frontend JS | test parite statique |
