# RealDev Vilvoorde FC — Application Staff & Joueurs

Application web progressive (PWA) pour la gestion du club de futsal RealDev Vilvoorde FC,  
évoluant en 1ère Division Nationale (Betcenter Futsal League).

---

## Stack

| Couche | Technologie |
|--------|-------------|
| Frontend | HTML/CSS/JS Vanilla · ES Modules · PWA |
| Backend | Supabase (PostgreSQL + Auth + Realtime) |
| Hébergement | GitHub Pages |
| Fonts | Barlow Condensed (Google Fonts) |

---

## Déploiement (GitHub Pages)

### 1. Prérequis
- Compte GitHub avec accès au repo `realdev-vilvoorde/app`
- Projet Supabase existant (voir ci-dessous)

### 2. Structure du repo
```
index.html          ← App principale (fichier unique)
manifest.json       ← PWA manifest
sw.js               ← Service Worker
src/
  modules/
    planning.js     ← Logique microcycle Lun/Mar/Mer
    auth.js         ← Auth helpers
    data.js         ← Supabase queries
  utils/
    supabase.js     ← Client Supabase
    state.js        ← Store global
    i18n.js         ← Traductions FR/NL
supabase/
  migrations/
    20260413000000_init.sql  ← Script SQL complet
README.md
```

### 3. Activer GitHub Pages
1. Aller dans **Settings → Pages**
2. Source : **Deploy from a branch → main → / (root)**
3. L'app sera accessible à `https://[org].github.io/[repo]`

---

## Configuration Supabase

### Clés d'accès
```
Project URL : https://jgytwvtdqpotdaleotok.supabase.co
Anon Key    : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Dashboard   : https://supabase.com/dashboard/project/jgytwvtdqpotdaleotok
```

### Initialiser la base de données
1. Ouvrir **Supabase Dashboard → SQL Editor → New query**
2. Copier-coller le contenu de `supabase/migrations/20260413000000_init.sql`
3. Cliquer **Run**

Le script crée :
- 6 tables (players, matches, injuries, presences, training_plans, scouting, user_profiles)
- Triggers updated_at
- Politiques RLS pour les 5 rôles
- Données seed : 12 joueurs + 15 matchs + 13 équipes scouting + 2 blessures actives

---

## Créer les comptes utilisateurs

### Procédure pour chaque membre du staff/joueur
1. **Supabase Dashboard → Authentication → Users → Invite user**
2. Saisir l'email → envoyer l'invitation
3. L'utilisateur reçoit un email, clique le lien, définit son mot de passe
4. **Dans SQL Editor**, insérer le profil :

```sql
-- Remplacer l'UUID par celui visible dans Authentication → Users
INSERT INTO user_profiles (id, role, display_name)
VALUES ('uuid-de-l-utilisateur', 'coach', 'Mustapha Harram');

-- Pour un joueur, lier au profil player :
INSERT INTO user_profiles (id, player_id, role, display_name)
VALUES (
  'uuid-auth-user',
  (SELECT id FROM players WHERE name = 'EL FAKIRI Soufiane'),
  'player',
  'Soufiane El Fakiri'
);
```

### Comptes à créer (staff)
| Nom | Email | Rôle |
|-----|-------|------|
| Mustapha Harram | m.harram@realdev-vfc.be | coach |
| Mustapha El Hajami | m.elhajami@realdev-vfc.be | coach |
| Mustapha Aabbassi | m.aabbassi@realdev-vfc.be | physio |
| Edward Bzdak | e.bzdak@realdev-vfc.be | gk |
| Miloudi Baouider | m.baouider@realdev-vfc.be | coach |
| Nordine Boukamher | n.boukamher@realdev-vfc.be | admin |

---

## Ajouter un joueur en cours de saison

```sql
-- 1. Insérer le joueur
INSERT INTO players (name, number, position, nationality, preferred_foot, status)
VALUES ('NOM PRENOM', 10, 'ALA', 'BEL', 'D', 'Disponible');

-- 2. Créer son compte via Auth → Invite User, puis :
INSERT INTO user_profiles (id, player_id, role, display_name)
VALUES (
  'uuid-du-nouveau-compte-auth',
  (SELECT id FROM players WHERE name = 'NOM PRENOM'),
  'player', 'NOM PRENOM'
);
```

---

## Migrations (modifications du schéma)

Ne jamais faire `ALTER TABLE` directement en production. Toujours :

1. Créer un fichier `supabase/migrations/YYYYMMDDHHMMSS_description.sql`
2. L'exécuter dans **SQL Editor** après avoir testé en dev
3. Committer le fichier dans le repo

---

## Modules de l'application

| Module | Rôles | Fonctionnalités |
|--------|-------|-----------------|
| Dashboard | Tous | KPIs, prochain match, alertes, derniers résultats |
| Présences | Coach/Physio | Pointer P/A/B/E + RPE · Historique · Stats % |
| Matchs | Tous | Calendrier · Encoder · Scouting 13 équipes |
| Blessures | Coach/Physio | Actives · Fiche médicale · Protocole retour · Historique |
| Planning | Coach | Microcycle Lun/Mar/Mer · Analyse adversaire auto |
| Plus | Coach+ | Effectif · Discipline · Performance |
| Mon profil | Player | Stats perso · Présences · Blessures perso |

---

## Temps réel (Supabase Realtime)

L'app souscrit aux changements sur les tables `injuries`, `matches`, `presences`, `training_plans`.  
Toute modification par un membre du staff est instantanément visible par tous les autres.

---

## PWA — Installation mobile

**iPhone/iPad :** Safari → bouton partage → "Sur l'écran d'accueil"  
**Android :** Chrome → menu → "Ajouter à l'écran d'accueil"

L'app fonctionne hors-ligne en lecture (données en cache service worker).  
Les modifications (encoder match, blessure...) nécessitent une connexion réseau.

---

## Contact

Younes — futsal-realdev.com  
Projet Supabase : jgytwvtdqpotdaleotok
