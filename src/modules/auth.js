import { supabase } from '../utils/supabase.js';
import { state, setState } from '../utils/state.js';

export async function login(email, password) {
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) throw error;
  await loadProfile(data.user);
  return state.profile;
}

export async function logout() {
  await supabase.auth.signOut();
  setState({ user: null, profile: null, role: null });
  localStorage.removeItem('rdv_role');
}

export async function getSession() {
  const { data: { session } } = await supabase.auth.getSession();
  if (session?.user) {
    await loadProfile(session.user);
    return session.user;
  }
  return null;
}

async function loadProfile(user) {
  setState({ user });
  const { data: profile } = await supabase
    .from('user_profiles')
    .select('*, players(name, position)')
    .eq('id', user.id)
    .single();

  if (profile) {
    setState({ profile, role: profile.role });
    localStorage.setItem('rdv_role', profile.role);
  }
}

export function isStaff() {
  return ['admin','coach','physio','gk'].includes(state.role);
}
export function canWrite(resource) {
  const rules = {
    matches:  ['admin','coach'],
    injuries: ['admin','coach','physio'],
    presences:['admin','coach','physio'],
    plans:    ['admin','coach'],
    players:  ['admin','coach'],
  };
  return (rules[resource] || []).includes(state.role);
}
