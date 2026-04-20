-- ============================================================
-- RealDev VFC — Fixes audit 2026-04-20
-- P0: colonnes/tables manquantes
-- P1: RLS plans_player (semaine en cours)
-- ============================================================

-- P0: matches.lineup (JSON composition 5v5)
ALTER TABLE public.matches
  ADD COLUMN IF NOT EXISTS lineup JSONB;

-- P0: matches.exercise_ids (lien vers exercices)
ALTER TABLE public.matches
  ADD COLUMN IF NOT EXISTS exercise_ids UUID[] DEFAULT '{}';

-- P0: players.birthdate (Sq10 Anniversaires)
ALTER TABLE public.players
  ADD COLUMN IF NOT EXISTS birthdate DATE;

-- P0: push_subscriptions (Edge Function + client PWA)
CREATE TABLE IF NOT EXISTS public.push_subscriptions (
  id BIGSERIAL PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  endpoint TEXT NOT NULL UNIQUE,
  p256dh TEXT NOT NULL,
  auth TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX IF NOT EXISTS push_subscriptions_user_id_idx
  ON public.push_subscriptions(user_id);

ALTER TABLE public.push_subscriptions ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS push_subscriptions_own ON public.push_subscriptions;
CREATE POLICY push_subscriptions_own ON public.push_subscriptions
  FOR ALL
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

-- Edge Function uses service-role key, bypassing RLS — no extra policy needed.

-- P1: fix plans_player — la semaine en cours doit rester visible
-- (ancienne règle: week_start >= CURRENT_DATE → invisible après lundi)
DROP POLICY IF EXISTS plans_player ON public.plans;
CREATE POLICY plans_player ON public.plans
  FOR SELECT
  USING (
    week_start >= date_trunc('week', CURRENT_DATE)::date
  );

-- ============================================================
-- Fin migration fixes 2026-04-20
-- ============================================================
