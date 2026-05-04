-- ════════════════════════════════════════════════════════════════════
-- RealDev VFC — Migration multi-team (Sprint multi-team 2026-05)
-- Adds team_id scoping to all business tables.
-- Backfills existing data to team_id = 'a-team'.
-- New tables: teams, user_teams.
-- New helper: get_my_team_ids().
-- Rewrites RLS so reads/writes are scoped by user_teams membership.
-- Run in Supabase SQL Editor (idempotent — safe to re-run).
-- ════════════════════════════════════════════════════════════════════

BEGIN;

-- ─────────────────────────────────────────
-- 1. teams
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS public.teams (
  id            text PRIMARY KEY,
  display_name  text NOT NULL,
  short_label   text,
  color         text,
  age_category  text,
  display_order int,
  active        boolean DEFAULT true,
  created_at    timestamptz DEFAULT now()
);

INSERT INTO public.teams (id, display_name, short_label, color, age_category, display_order) VALUES
  ('a-team', 'A Team', 'A',   '#B8CC2E', 'senior', 1),
  ('u21',    'U21',    'U21', '#FB8C00', 'u21',    2),
  ('u17',    'U17',    'U17', '#1E88E5', 'u17',    3),
  ('u15',    'U15',    'U15', '#8E24AA', 'u15',    4),
  ('women',  'Women',  'W',   '#EC407A', 'women',  5)
ON CONFLICT (id) DO NOTHING;

ALTER TABLE public.teams ENABLE ROW LEVEL SECURITY;
DROP POLICY IF EXISTS teams_read ON public.teams;
CREATE POLICY teams_read ON public.teams FOR SELECT USING (auth.role() = 'authenticated');

-- ─────────────────────────────────────────
-- 2. user_teams (jointure user ↔ équipes)
-- ─────────────────────────────────────────
CREATE TABLE IF NOT EXISTS public.user_teams (
  user_id    uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  team_id    text NOT NULL REFERENCES public.teams(id) ON DELETE CASCADE,
  role       text NOT NULL CHECK (role IN ('admin','coach','assistant','physio','gk','player')),
  is_default boolean DEFAULT false,
  created_at timestamptz DEFAULT now(),
  PRIMARY KEY (user_id, team_id)
);

CREATE INDEX IF NOT EXISTS user_teams_user_idx ON public.user_teams(user_id);
CREATE INDEX IF NOT EXISTS user_teams_team_idx ON public.user_teams(team_id);

ALTER TABLE public.user_teams ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS user_teams_own_read ON public.user_teams;
CREATE POLICY user_teams_own_read ON public.user_teams
  FOR SELECT USING (user_id = auth.uid());

DROP POLICY IF EXISTS user_teams_admin_read ON public.user_teams;
CREATE POLICY user_teams_admin_read ON public.user_teams
  FOR SELECT USING (
    EXISTS (SELECT 1 FROM public.user_profiles WHERE id = auth.uid() AND role = 'admin')
  );

DROP POLICY IF EXISTS user_teams_admin_write ON public.user_teams;
CREATE POLICY user_teams_admin_write ON public.user_teams
  FOR ALL USING (
    EXISTS (SELECT 1 FROM public.user_profiles WHERE id = auth.uid() AND role = 'admin')
  );

-- ─────────────────────────────────────────
-- 3. helper SQL : team_ids accessibles à l'user courant
-- ─────────────────────────────────────────
CREATE OR REPLACE FUNCTION public.get_my_team_ids() RETURNS text[] AS $$
  SELECT COALESCE(array_agg(team_id), ARRAY[]::text[])
  FROM public.user_teams
  WHERE user_id = auth.uid();
$$ LANGUAGE sql STABLE SECURITY DEFINER;

REVOKE ALL ON FUNCTION public.get_my_team_ids() FROM PUBLIC;
GRANT EXECUTE ON FUNCTION public.get_my_team_ids() TO authenticated;

-- ─────────────────────────────────────────
-- 4. ADD COLUMN team_id sur tables métier (idempotent)
--    Ordre : ALTER nullable → backfill 'a-team' → SET NOT NULL → FK + index
-- ─────────────────────────────────────────
DO $migrate$
DECLARE
  t text;
  business_tables text[] := ARRAY[
    'players',
    'matches',
    'injuries',
    'presences',
    'training_plans',
    'scouting',
    'player_availability'
  ];
BEGIN
  FOREACH t IN ARRAY business_tables LOOP
    -- Skip silently if table missing (e.g. player_availability ajoutée later)
    IF NOT EXISTS (
      SELECT 1 FROM information_schema.tables
      WHERE table_schema='public' AND table_name=t
    ) THEN
      RAISE NOTICE 'Skipping % (table not present)', t;
      CONTINUE;
    END IF;

    -- 4.a ADD COLUMN nullable
    EXECUTE format('ALTER TABLE public.%I ADD COLUMN IF NOT EXISTS team_id text', t);

    -- 4.b backfill
    EXECUTE format('UPDATE public.%I SET team_id = ''a-team'' WHERE team_id IS NULL', t);

    -- 4.c NOT NULL
    EXECUTE format('ALTER TABLE public.%I ALTER COLUMN team_id SET NOT NULL', t);

    -- 4.d Default for new inserts (defensive — client should set explicitly)
    EXECUTE format('ALTER TABLE public.%I ALTER COLUMN team_id SET DEFAULT ''a-team''', t);

    -- 4.e FK to teams (drop+create to be idempotent if rerun)
    EXECUTE format(
      'ALTER TABLE public.%I DROP CONSTRAINT IF EXISTS %I',
      t, t || '_team_id_fkey'
    );
    EXECUTE format(
      'ALTER TABLE public.%I ADD CONSTRAINT %I FOREIGN KEY (team_id) REFERENCES public.teams(id)',
      t, t || '_team_id_fkey'
    );

    -- 4.f index
    EXECUTE format(
      'CREATE INDEX IF NOT EXISTS %I ON public.%I (team_id)',
      t || '_team_id_idx', t
    );

    RAISE NOTICE 'Migrated table % (team_id NOT NULL + FK + index)', t;
  END LOOP;
END
$migrate$;

-- ─────────────────────────────────────────
-- 5. Seed user_teams pour les users existants → A Team avec leur rôle actuel
-- ─────────────────────────────────────────
INSERT INTO public.user_teams (user_id, team_id, role, is_default)
SELECT id, 'a-team',
  CASE
    WHEN role IN ('admin','coach','assistant','physio','gk','player') THEN role
    ELSE 'player'
  END,
  true
FROM public.user_profiles
ON CONFLICT (user_id, team_id) DO NOTHING;

-- ─────────────────────────────────────────
-- 6. RLS — réécriture pour scoping par team_id
--    NB: 'admin' (rôle global dans user_profiles) garde l'override universel.
-- ─────────────────────────────────────────

-- ── players ────────────────────────────────────────────────
DROP POLICY IF EXISTS "players_read"  ON public.players;
DROP POLICY IF EXISTS "players_write" ON public.players;
CREATE POLICY players_read ON public.players FOR SELECT
  USING (
    get_my_role() = 'admin'
    OR team_id = ANY(public.get_my_team_ids())
  );
CREATE POLICY players_write ON public.players FOR ALL
  USING (
    get_my_role() = 'admin'
    OR (
      team_id = ANY(public.get_my_team_ids())
      AND get_my_role() IN ('admin','coach','assistant')
    )
  );

-- ── matches ────────────────────────────────────────────────
DROP POLICY IF EXISTS "matches_read"  ON public.matches;
DROP POLICY IF EXISTS "matches_write" ON public.matches;
CREATE POLICY matches_read ON public.matches FOR SELECT
  USING (
    get_my_role() = 'admin'
    OR team_id = ANY(public.get_my_team_ids())
  );
CREATE POLICY matches_write ON public.matches FOR ALL
  USING (
    get_my_role() = 'admin'
    OR (
      team_id = ANY(public.get_my_team_ids())
      AND get_my_role() IN ('admin','coach','assistant')
    )
  );

-- ── injuries ───────────────────────────────────────────────
DROP POLICY IF EXISTS "injuries_staff" ON public.injuries;
DROP POLICY IF EXISTS "injuries_own"   ON public.injuries;
DROP POLICY IF EXISTS "injuries_write" ON public.injuries;
CREATE POLICY injuries_staff ON public.injuries FOR SELECT
  USING (
    (get_my_role() IN ('admin','coach','assistant','physio','gk'))
    AND (get_my_role() = 'admin' OR team_id = ANY(public.get_my_team_ids()))
  );
CREATE POLICY injuries_own ON public.injuries FOR SELECT
  USING (
    team_id = ANY(public.get_my_team_ids())
    AND player_id IN (
      SELECT player_id FROM public.user_profiles
      WHERE id = auth.uid() AND player_id IS NOT NULL
    )
  );
CREATE POLICY injuries_write ON public.injuries FOR ALL
  USING (
    get_my_role() = 'admin'
    OR (
      team_id = ANY(public.get_my_team_ids())
      AND get_my_role() IN ('admin','coach','assistant','physio')
    )
  );

-- ── presences ──────────────────────────────────────────────
DROP POLICY IF EXISTS "presences_staff" ON public.presences;
DROP POLICY IF EXISTS "presences_own"   ON public.presences;
DROP POLICY IF EXISTS "presences_write" ON public.presences;
CREATE POLICY presences_staff ON public.presences FOR SELECT
  USING (
    (get_my_role() IN ('admin','coach','assistant','physio'))
    AND (get_my_role() = 'admin' OR team_id = ANY(public.get_my_team_ids()))
  );
CREATE POLICY presences_own ON public.presences FOR SELECT
  USING (
    team_id = ANY(public.get_my_team_ids())
    AND player_id IN (
      SELECT player_id FROM public.user_profiles
      WHERE id = auth.uid() AND player_id IS NOT NULL
    )
  );
CREATE POLICY presences_write ON public.presences FOR ALL
  USING (
    get_my_role() = 'admin'
    OR (
      team_id = ANY(public.get_my_team_ids())
      AND get_my_role() IN ('admin','coach','assistant','physio')
    )
  );

-- ── training_plans ─────────────────────────────────────────
DROP POLICY IF EXISTS "plans_staff"  ON public.training_plans;
DROP POLICY IF EXISTS "plans_player" ON public.training_plans;
DROP POLICY IF EXISTS "plans_write"  ON public.training_plans;
-- (la 2026-04-20 fix migration référence "plans" — DROP IF EXISTS au cas où, gardé seulement si la table existe)
DO $$ BEGIN
  IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema='public' AND table_name='plans') THEN
    EXECUTE 'DROP POLICY IF EXISTS plans_player ON public.plans';
  END IF;
END $$;

CREATE POLICY plans_staff ON public.training_plans FOR SELECT
  USING (
    (get_my_role() IN ('admin','coach','assistant','physio','gk'))
    AND (get_my_role() = 'admin' OR team_id = ANY(public.get_my_team_ids()))
  );
CREATE POLICY plans_player ON public.training_plans FOR SELECT
  USING (
    team_id = ANY(public.get_my_team_ids())
    AND week_start >= date_trunc('week', CURRENT_DATE)::date
  );
CREATE POLICY plans_write ON public.training_plans FOR ALL
  USING (
    get_my_role() = 'admin'
    OR (
      team_id = ANY(public.get_my_team_ids())
      AND get_my_role() IN ('admin','coach','assistant')
    )
  );

-- ── scouting ───────────────────────────────────────────────
DROP POLICY IF EXISTS "scouting_read"  ON public.scouting;
DROP POLICY IF EXISTS "scouting_write" ON public.scouting;
CREATE POLICY scouting_read ON public.scouting FOR SELECT
  USING (
    (get_my_role() IN ('admin','coach','assistant','physio','gk'))
    AND (get_my_role() = 'admin' OR team_id = ANY(public.get_my_team_ids()))
  );
CREATE POLICY scouting_write ON public.scouting FOR ALL
  USING (
    get_my_role() = 'admin'
    OR (
      team_id = ANY(public.get_my_team_ids())
      AND get_my_role() IN ('admin','coach','assistant')
    )
  );

-- ── player_availability ────────────────────────────────────
-- (la table peut ne pas exister selon l'historique — guard)
DO $$ BEGIN
  IF EXISTS (
    SELECT 1 FROM information_schema.tables
    WHERE table_schema='public' AND table_name='player_availability'
  ) THEN
    EXECUTE 'ALTER TABLE public.player_availability ENABLE ROW LEVEL SECURITY';

    EXECUTE 'DROP POLICY IF EXISTS pavail_read  ON public.player_availability';
    EXECUTE 'DROP POLICY IF EXISTS pavail_write ON public.player_availability';

    EXECUTE $p$
      CREATE POLICY pavail_read ON public.player_availability FOR SELECT
      USING (
        get_my_role() = 'admin'
        OR team_id = ANY(public.get_my_team_ids())
      )
    $p$;
    EXECUTE $p$
      CREATE POLICY pavail_write ON public.player_availability FOR ALL
      USING (
        get_my_role() = 'admin'
        OR (
          team_id = ANY(public.get_my_team_ids())
          AND get_my_role() IN ('admin','coach','assistant','physio','player')
        )
      )
    $p$;
  END IF;
END $$;

COMMIT;

-- ════════════════════════════════════════════════════════════════════
-- POST-MIGRATION CHECKS (à exécuter manuellement après COMMIT)
-- ════════════════════════════════════════════════════════════════════
-- SELECT count(*) FROM public.teams;                          -- expect 5
-- SELECT count(*) FROM public.user_teams;                     -- expect = #user_profiles
-- SELECT count(*) FROM public.players  WHERE team_id <> 'a-team'; -- expect 0
-- SELECT count(*) FROM public.matches  WHERE team_id <> 'a-team'; -- expect 0
-- SELECT count(*) FROM public.injuries WHERE team_id <> 'a-team'; -- expect 0
-- SELECT public.get_my_team_ids();                            -- expect array containing 'a-team' (when run as a logged-in user)

-- ════════════════════════════════════════════════════════════════════
-- ROLLBACK (en cas de besoin — supprime les colonnes team_id et restore RLS)
-- À copier-coller dans le SQL Editor uniquement si rollback voulu.
-- ════════════════════════════════════════════════════════════════════
-- BEGIN;
--   -- restore RLS pre-multi-team (cf. 20260413000000_init.sql + 20260420000000_fixes.sql)
--   -- ALTER TABLE players DROP COLUMN team_id;       (etc. pour chaque table)
--   -- DROP TABLE user_teams; DROP TABLE teams; DROP FUNCTION get_my_team_ids();
-- COMMIT;
