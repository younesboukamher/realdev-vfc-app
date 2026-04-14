-- ═══════════════════════════════════════════════════════════════
-- REALDEV VILVOORDE FC — Migration initiale
-- Exécuter dans Supabase SQL Editor (une seule fois)
-- ═══════════════════════════════════════════════════════════════

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ─────────────────────────────────────────
-- players
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS players (
  id             uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  name           text NOT NULL,
  number         integer,
  position       text CHECK (position IN ('GK','FIXO','ALA','PIVOT')),
  age            integer,
  nationality    text,
  preferred_foot text CHECK (preferred_foot IN ('D','G','B')),
  status         text DEFAULT 'Disponible'
                 CHECK (status IN ('Disponible','Blessé','Suspendu','Incertain')),
  goals          integer DEFAULT 0,
  assists        integer DEFAULT 0,
  yellow_cards   integer DEFAULT 0,
  red_cards      integer DEFAULT 0,
  rating         numeric(3,1),
  photo_url      text,
  created_at     timestamptz DEFAULT now(),
  updated_at     timestamptz DEFAULT now()
);

-- ─────────────────────────────────────────
-- matches
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS matches (
  id           uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  journee      text,
  match_date   date,
  is_home      boolean NOT NULL,
  opponent     text NOT NULL,
  score_home   integer,
  score_away   integer,
  result       text CHECK (result IN ('V','N','D') OR result IS NULL),
  scorers      text,
  cards        text,
  notes        text,
  created_at   timestamptz DEFAULT now(),
  updated_at   timestamptz DEFAULT now()
);

-- ─────────────────────────────────────────
-- injuries
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS injuries (
  id             uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  player_id      uuid NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  type           text NOT NULL,
  severity       text CHECK (severity IN ('G1','G2','G3','G4')),
  status         text DEFAULT 'En récupération',
  injury_date    date NOT NULL,
  return_date    date,
  mechanism      text,
  anatomy_zone   text,
  exam           text,
  treatment      text,
  protocol       jsonb DEFAULT '[]',
  matches_missed text,
  notes          text,
  healed_at      date,
  is_active      boolean DEFAULT true,
  created_at     timestamptz DEFAULT now(),
  updated_at     timestamptz DEFAULT now()
);

-- ─────────────────────────────────────────
-- presences
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS presences (
  id           uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  player_id    uuid NOT NULL REFERENCES players(id) ON DELETE CASCADE,
  session_date date NOT NULL,
  session_type text CHECK (session_type IN ('Entraînement','Match','Physique')),
  status       text NOT NULL CHECK (status IN ('P','A','B','E')),
  rpe          integer CHECK (rpe BETWEEN 1 AND 10),
  notes        text,
  created_by   uuid REFERENCES auth.users(id),
  created_at   timestamptz DEFAULT now(),
  UNIQUE (player_id, session_date, session_type)
);

-- ─────────────────────────────────────────
-- training_plans
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS training_plans (
  id          uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  match_id    uuid REFERENCES matches(id) ON DELETE SET NULL,
  week_start  date,
  sessions    jsonb DEFAULT '[]',
  week_note   text,
  created_by  uuid REFERENCES auth.users(id),
  created_at  timestamptz DEFAULT now(),
  updated_at  timestamptz DEFAULT now()
);

-- ─────────────────────────────────────────
-- scouting
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS scouting (
  id            uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
  opponent_name text NOT NULL UNIQUE,
  rank          integer,
  points        integer,
  system        text,
  pressing      text,
  strengths     text,
  weaknesses    text,
  key_player    text,
  note_5v4gk    text,
  coach_note    text,
  diff_goals    text,
  color         text DEFAULT '#3BBDE4',
  season        text DEFAULT '2025-2026',
  updated_at    timestamptz DEFAULT now()
);

-- ─────────────────────────────────────────
-- user_profiles
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS user_profiles (
  id           uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  player_id    uuid REFERENCES players(id) ON DELETE SET NULL,
  role         text NOT NULL DEFAULT 'player'
               CHECK (role IN ('admin','coach','physio','gk','player')),
  display_name text,
  created_at   timestamptz DEFAULT now()
);

-- ─────────────────────────────────────────
-- Triggers updated_at
-- ─────────────────────────────────────────
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN NEW.updated_at = now(); RETURN NEW; END;
$$ LANGUAGE plpgsql;

DO $$ BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_trigger WHERE tgname='trg_players_upd') THEN
    CREATE TRIGGER trg_players_upd BEFORE UPDATE ON players FOR EACH ROW EXECUTE FUNCTION update_updated_at();
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_trigger WHERE tgname='trg_matches_upd') THEN
    CREATE TRIGGER trg_matches_upd BEFORE UPDATE ON matches FOR EACH ROW EXECUTE FUNCTION update_updated_at();
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_trigger WHERE tgname='trg_injuries_upd') THEN
    CREATE TRIGGER trg_injuries_upd BEFORE UPDATE ON injuries FOR EACH ROW EXECUTE FUNCTION update_updated_at();
  END IF;
  IF NOT EXISTS (SELECT 1 FROM pg_trigger WHERE tgname='trg_training_upd') THEN
    CREATE TRIGGER trg_training_upd BEFORE UPDATE ON training_plans FOR EACH ROW EXECUTE FUNCTION update_updated_at();
  END IF;
END $$;

-- ─────────────────────────────────────────
-- RLS
-- ─────────────────────────────────────────
ALTER TABLE players        ENABLE ROW LEVEL SECURITY;
ALTER TABLE matches        ENABLE ROW LEVEL SECURITY;
ALTER TABLE injuries       ENABLE ROW LEVEL SECURITY;
ALTER TABLE presences      ENABLE ROW LEVEL SECURITY;
ALTER TABLE training_plans ENABLE ROW LEVEL SECURITY;
ALTER TABLE scouting       ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_profiles  ENABLE ROW LEVEL SECURITY;

CREATE OR REPLACE FUNCTION get_my_role()
RETURNS text AS $$
  SELECT role FROM user_profiles WHERE id = auth.uid();
$$ LANGUAGE sql SECURITY DEFINER STABLE;

-- players
DROP POLICY IF EXISTS "players_read" ON players;
CREATE POLICY "players_read" ON players FOR SELECT USING (auth.role() = 'authenticated');
DROP POLICY IF EXISTS "players_write" ON players;
CREATE POLICY "players_write" ON players FOR ALL USING (get_my_role() IN ('admin','coach'));

-- matches
DROP POLICY IF EXISTS "matches_read" ON matches;
CREATE POLICY "matches_read" ON matches FOR SELECT USING (auth.role() = 'authenticated');
DROP POLICY IF EXISTS "matches_write" ON matches;
CREATE POLICY "matches_write" ON matches FOR ALL USING (get_my_role() IN ('admin','coach'));

-- injuries
DROP POLICY IF EXISTS "injuries_staff" ON injuries;
CREATE POLICY "injuries_staff" ON injuries FOR SELECT USING (get_my_role() IN ('admin','coach','physio','gk'));
DROP POLICY IF EXISTS "injuries_own" ON injuries;
CREATE POLICY "injuries_own" ON injuries FOR SELECT USING (
  player_id IN (SELECT player_id FROM user_profiles WHERE id = auth.uid() AND player_id IS NOT NULL)
);
DROP POLICY IF EXISTS "injuries_write" ON injuries;
CREATE POLICY "injuries_write" ON injuries FOR ALL USING (get_my_role() IN ('admin','coach','physio'));

-- presences
DROP POLICY IF EXISTS "presences_staff" ON presences;
CREATE POLICY "presences_staff" ON presences FOR SELECT USING (get_my_role() IN ('admin','coach','physio'));
DROP POLICY IF EXISTS "presences_own" ON presences;
CREATE POLICY "presences_own" ON presences FOR SELECT USING (
  player_id IN (SELECT player_id FROM user_profiles WHERE id = auth.uid() AND player_id IS NOT NULL)
);
DROP POLICY IF EXISTS "presences_write" ON presences;
CREATE POLICY "presences_write" ON presences FOR ALL USING (get_my_role() IN ('admin','coach','physio'));

-- training_plans
DROP POLICY IF EXISTS "plans_staff" ON training_plans;
CREATE POLICY "plans_staff" ON training_plans FOR SELECT USING (get_my_role() IN ('admin','coach','physio','gk'));
DROP POLICY IF EXISTS "plans_player" ON training_plans;
CREATE POLICY "plans_player" ON training_plans FOR SELECT USING (get_my_role() = 'player' AND week_start >= CURRENT_DATE);
DROP POLICY IF EXISTS "plans_write" ON training_plans;
CREATE POLICY "plans_write" ON training_plans FOR ALL USING (get_my_role() IN ('admin','coach'));

-- scouting
DROP POLICY IF EXISTS "scouting_read" ON scouting;
CREATE POLICY "scouting_read" ON scouting FOR SELECT USING (get_my_role() IN ('admin','coach','physio','gk'));
DROP POLICY IF EXISTS "scouting_write" ON scouting;
CREATE POLICY "scouting_write" ON scouting FOR ALL USING (get_my_role() IN ('admin','coach'));

-- user_profiles
DROP POLICY IF EXISTS "profiles_own" ON user_profiles;
CREATE POLICY "profiles_own" ON user_profiles FOR SELECT USING (id = auth.uid());
DROP POLICY IF EXISTS "profiles_admin_read" ON user_profiles;
CREATE POLICY "profiles_admin_read" ON user_profiles FOR SELECT USING (get_my_role() = 'admin');
DROP POLICY IF EXISTS "profiles_admin_write" ON user_profiles;
CREATE POLICY "profiles_admin_write" ON user_profiles FOR ALL USING (get_my_role() = 'admin');

-- ─────────────────────────────────────────
-- SEED: players
-- ─────────────────────────────────────────
INSERT INTO players (name,number,position,nationality,preferred_foot,status,goals,assists,yellow_cards,red_cards,rating) VALUES
('BOULLERMAUN Hicham', 13,'GK',   'BEL','D','Disponible', 0, 0,0,0,7.8),
('TALHAOUI Morad',     14,'GK',   'MAR','D','Disponible', 0, 0,0,0,7.2),
('MATHIEU O.',         15,'FIXO', 'BEL','D','Disponible', 2, 4,0,0,7.5),
('HACHEM Bilal',       17,'FIXO', 'BEL','D','Disponible', 2, 3,2,0,7.6),
('EL BOUHADIFI Bilal', 18,'FIXO', 'BEL','G','Disponible', 3, 4,1,0,7.4),
('EL HAFID Abdessamad',19,'ALA',  'BEL','D','Disponible',14, 5,1,0,8.3),
('EL FAKIRI Soufiane', 20,'ALA',  'BEL','D','Disponible',25, 8,0,0,9.1),
('QOLI Yassine',       21,'ALA',  'BEL','G','Disponible', 6, 3,3,0,7.7),
('CHOUAA Mounir',      22,'PIVOT','MAR','D','Disponible', 7, 2,0,0,7.9),
('BOUCHOIRI Marwan',   23,'PIVOT','MAR','D','Blessé',     12, 4,0,0,8.1),
('EL KAJOUI Raid',    NULL,'ALA', 'BEL','D','Blessé',      3, 2,0,0,7.6),
('BOUZID Mouhsin',    NULL,'ALA', 'BEL','D','Disponible',  4, 2,0,0,7.3)
ON CONFLICT DO NOTHING;

-- SEED: injuries
INSERT INTO injuries (player_id,type,severity,status,injury_date,return_date,mechanism,anatomy_zone,treatment,protocol,is_active)
SELECT id,'Entorse cheville droite','G1','En récupération','2026-04-05','2026-04-19',
  'Torsion en appui lors d''un duel en J15 vs FAL Soumagne (03/04/26)',
  'Cheville droite — ligaments latéraux externes',
  'RICE J1-J2 · Kiné 3×/sem · Strapping · Reprise progressive',
  '[{"phase":"J1-J3","desc":"Repos relatif, glace, compression"},{"phase":"J4-J7","desc":"Kiné mobilisation douce, proprioception"},{"phase":"J15","desc":"Reprise entraînement collectif"}]'::jsonb,
  true FROM players WHERE name='EL KAJOUI Raid' ON CONFLICT DO NOTHING;

INSERT INTO injuries (player_id,type,severity,status,injury_date,return_date,mechanism,anatomy_zone,exam,treatment,protocol,is_active)
SELECT id,'Entorse cheville gauche (grave)','G3','En récupération','2026-03-22','2026-05-05',
  'Réception déséquilibrée lors d''un duel en J13 vs Shokudo Aarschot',
  'Cheville gauche — rupture partielle LLE + LTFA',
  'IRM 24/03 — lésion grade 2-3 LLE. Pas de fracture.',
  'Immobilisation 10j · Kiné intensive 3×/sem · Ondes de choc',
  '[{"phase":"J1-J10","desc":"Immobilisation totale, béquilles, glace"},{"phase":"J11-J21","desc":"Kiné mobilisation passive, renforcement isométrique"},{"phase":"J36-J42","desc":"Exercices spécifiques futsal, contacts progressifs"}]'::jsonb,
  true FROM players WHERE name='BOUCHOIRI Marwan' ON CONFLICT DO NOTHING;

INSERT INTO injuries (player_id,type,severity,status,injury_date,return_date,mechanism,anatomy_zone,is_active,healed_at)
SELECT id,'Élongation adducteurs','G2','Guéri','2026-01-18','2026-03-22',
  'Sprint en accélération lors du match aller vs FAL Soumagne (J5)',
  'Adducteur long gauche — jonction musculo-tendineuse',
  false,'2026-03-22' FROM players WHERE name='CHOUAA Mounir' ON CONFLICT DO NOTHING;

-- SEED: matches
INSERT INTO matches (journee,match_date,is_home,opponent,score_home,score_away,result,scorers) VALUES
('J1','2025-10-31',true, 'Full Hasselt',              7,1,'V','El Hafid, El Fakiri (x2), Bouchoiri (x2), Chouaa, El Bouhadifi'),
('J2','2025-11-08',false,'Sensei Sushi Anderlecht',   3,3,'N','El Fakiri, Bouchoiri, El Hafid'),
('J3','2025-11-15',true, 'ZVC Pibo Bilzen',           2,3,'D','El Hafid, Mathieu O.'),
('J4','2025-12-12',false,'Futsal RWDM',              10,4,'V','El Fakiri (x3), Bouchoiri (x2), El Hafid, Chouaa, Qoli, Bouzid, Hachem'),
('J5','2026-01-18',false,'FAL Soumagne',              6,7,'D','El Fakiri (x2), El Hafid, Bouchoiri, Chouaa, El Bouhadifi'),
('J6','2026-01-25',true, 'RE Herentals',              3,2,'V','El Fakiri, El Hafid, Bouchoiri'),
('J7','2026-02-08',false,'FT Antwerpen',              1,3,'D','El Fakiri'),
('J8','2025-10-26',false,'Sp. Anderlecht FS',         0,6,'D',''),
('J9','2026-02-22',true, 'FST Charleroi',             4,6,'D','El Hafid, El Fakiri, Bouchoiri, Qoli'),
('J10','2026-02-28',true,'Eisden Dorp',               6,3,'V','El Fakiri (x2), Bouchoiri, El Hafid, Chouaa, Qoli'),
('J11','2026-03-08',false,'Los Leones Hasselt',       5,4,'V','El Fakiri (x2), El Hafid, Bouchoiri, Bouzid'),
('J12','2026-03-15',false,'B-M Bruxelles',            3,5,'D','El Fakiri, El Hafid, Chouaa'),
('J13','2026-03-22',true, 'Shokudo Aarschot',         7,2,'V','El Fakiri (x3), Bouchoiri (x2), El Hafid, Qoli'),
('J14','2026-03-29',false,'Futsal RWDM',              4,4,'N','El Fakiri (x2), Chouaa, El Hafid'),
('J15','2026-04-03',true, 'FAL Soumagne',             8,7,'V','El Fakiri (x3), El Hafid (x2), Bouchoiri, Chouaa, Bouzid'),
('J16','2026-04-17',false,'Sensei Sushi Anderlecht', NULL,NULL,NULL,NULL)
ON CONFLICT DO NOTHING;

-- SEED: scouting (13 équipes D1)
INSERT INTO scouting (opponent_name,rank,points,system,pressing,strengths,weaknesses,key_player,note_5v4gk,coach_note,diff_goals,color) VALUES
('Sp. Anderlecht FS',  1,63,'1-2-1 pressing haut','Haut permanent','Pressing intense, transitions rapides, profondeur de banc','Prévisible dans la construction, vulnérable au jeu direct','Omar Rahou (ALA, top scorer)','Sortie GK très agressive — timing critique','TOP 1 — match référence. Bloc défensif bas requis.','+30','#E53935'),
('FT Antwerpen',       2,56,'1-2-1 mixte','Moyen-Haut','Organisation défensive solide, duels physiques','Lents en transition défensive','Roncaglio (PIVOT, technique)','5v4+GK prévisible côté droit','Physique — tenir le tempo 40 min.','+18','#1E88E5'),
('RE Herentals',       3,55,'1-3 défensif','Bas-Moyen','Bloc bas compact, efficacité sur contre','Manque de créativité offensive','Ghislandi (ALA, vitesse)','GK sort tard — laisser venir','+15','#43A047'),
('FST Charleroi',      4,50,'1-2-1 offensif','Haut','Pressing haut coordonné, bonne condition physique','Espaces en transition après pressing raté','Hamza Zaaf (FIXO, vision)','Agressif — sortir vite ou pas du tout','+12','#FB8C00'),
('B-M Bruxelles',      5,45,'1-2-1 mixte','Moyen','Technique individuelle élevée, jeu en triangle','Défense désorganisée après faute','Sander Van Mol (ALA, dribble)','Classique — schéma côté fort','+10','#8E24AA'),
('FAL Soumagne',       6,39,'1-2-1 pressing','Haut','Intensité physique, duels aériens','Fatiguent en 2e mi-temps','Ilias Bachar (PIVOT, force)','Sortie précoce — exploiter l''espace','Dangereux sur coup franc direct.','+5','#00ACC1'),
('RealDev Vilvoorde',  7,36,'1-2-1 mixte','Moyen','Technique de finition, expérience El Fakiri','Dépendance El Fakiri','El Fakiri Soufiane (ALA, 25 buts)','Schémas variés','Notre équipe — référence interne.','0','#B8CC2E'),
('Los Leones Hasselt', 8,28,'1-2-1 défensif','Bas','Solidité défensive, discipline','Manque de créativité, peu de solutions offensives','Dries Vrancken (GK, réflexes)','Hésitants — pressing immédiat efficace','-8','#F4511E'),
('ZVC Pibo Bilzen',    9,27,'1-3 défensif','Bas','Organisation, discipline tactique','Attaque limitée, peu de vitesse','Lahraoui (FIXO, expérience)','Schéma côté gauche uniquement','-9','#039BE5'),
('Eisden Dorp',       10,21,'1-2-1 basique','Bas','Physique, jeu aérien','Technique faible, décisions lentes','Senne Thijs (ALA, pressing)','Hésitants — sortie au signal','-15','#7CB342'),
('Shokudo Aarschot',  11,19,'1-2-1 défensif','Bas','Discipline défensive','Peu créatifs, lents offensivement','Bram Claes (PIVOT, taille)','Schéma basique côté droit','-28','#6D4C41'),
('Sensei Sushi Anderlecht',12,15,'1-2-1 basique','Bas','Combativité, engagement','Qualité technique insuffisante','Mehdi Lachgar (ALA)','Peu d''expérience — pressing haut décisif','-35','#546E7A'),
('Futsal RWDM',       13,13,'1-3 défensif','Bas','Organisation, discipline','Manque d''individualités','Kevin Moris (FIXO)','Sortie tardive — exploiter espace central','-40','#78909C'),
('Anneesens Anderlecht',14,2,'1-2-1 basique','Bas','Combativité','Niveau insuffisant D1','Ridouane Taouil (ALA)','Sortie immédiate — chaos offensif','-55','#90A4AE')
ON CONFLICT (opponent_name) DO NOTHING;
