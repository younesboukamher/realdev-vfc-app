-- ════════════════════════════════════════════════════════════════════
-- RealDev VFC — admin_list_users RPC (Sprint multi-team 2026-05)
-- Adds an RPC function for admins to enumerate users for the
-- Settings → Accès équipes matrix.
-- auth.users is not directly readable by clients, so we expose a
-- minimal SECURITY DEFINER function that returns only what the matrix UI needs.
-- ════════════════════════════════════════════════════════════════════

BEGIN;

CREATE OR REPLACE FUNCTION public.admin_list_users()
RETURNS TABLE (
  user_id      uuid,
  email        text,
  display_name text,
  profile_role text,
  created_at   timestamptz
) AS $$
  SELECT
    u.id,
    u.email::text,
    p.display_name,
    COALESCE(p.role, 'player') AS profile_role,
    u.created_at
  FROM auth.users u
  LEFT JOIN public.user_profiles p ON p.id = u.id
  WHERE EXISTS (
    SELECT 1 FROM public.user_profiles
    WHERE id = auth.uid() AND role = 'admin'
  )
  ORDER BY u.created_at;
$$ LANGUAGE sql STABLE SECURITY DEFINER;

REVOKE ALL ON FUNCTION public.admin_list_users() FROM PUBLIC;
GRANT EXECUTE ON FUNCTION public.admin_list_users() TO authenticated;

COMMENT ON FUNCTION public.admin_list_users() IS
  'Returns the list of authenticated users + their profile metadata. Admin-only (checks user_profiles.role=admin). Used by the Settings → Accès équipes matrix.';

COMMIT;

-- ════════════════════════════════════════════════════════════════════
-- POST-MIGRATION CHECKS
-- ════════════════════════════════════════════════════════════════════
-- SELECT * FROM public.admin_list_users();   -- as admin: returns 4 rows. as non-admin: returns 0 rows.
