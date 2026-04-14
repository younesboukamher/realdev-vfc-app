import { supabase } from '../utils/supabase.js';
import { state, setState } from '../utils/state.js';

// ── PLAYERS ───────────────────────────────────────────────────────
export async function fetchPlayers() {
  const { data, error } = await supabase.from('players').select('*').order('number');
  if (!error) setState({ players: data || [] });
  return data;
}
export async function upsertPlayer(player) {
  const { data, error } = player.id
    ? await supabase.from('players').update(player).eq('id', player.id).select().single()
    : await supabase.from('players').insert(player).select().single();
  if (error) throw error;
  await fetchPlayers();
  return data;
}

// ── MATCHES ───────────────────────────────────────────────────────
export async function fetchMatches() {
  const { data, error } = await supabase.from('matches').select('*').order('match_date');
  if (!error) setState({ matches: data || [] });
  return data;
}
export async function saveMatch(match) {
  // Auto-calculate result
  if (match.score_home != null && match.score_away != null) {
    match.result = match.score_home > match.score_away ? 'V'
                 : match.score_home < match.score_away ? 'D' : 'N';
  }
  const { data, error } = match.id
    ? await supabase.from('matches').update(match).eq('id', match.id).select().single()
    : await supabase.from('matches').insert(match).select().single();
  if (error) throw error;
  await fetchMatches();
  return data;
}

// ── INJURIES ──────────────────────────────────────────────────────
export async function fetchInjuries() {
  const { data: active } = await supabase
    .from('injuries').select('*, players(name,position)')
    .eq('is_active', true).order('injury_date', { ascending: false });
  const { data: history } = await supabase
    .from('injuries').select('*, players(name,position)')
    .eq('is_active', false).order('healed_at', { ascending: false });
  setState({ injuries: active || [], injHistory: history || [] });
}
export async function saveInjury(inj) {
  const payload = { ...inj };
  delete payload.players; // remove joined data
  const { data, error } = payload.id
    ? await supabase.from('injuries').update(payload).eq('id', payload.id).select().single()
    : await supabase.from('injuries').insert(payload).select().single();
  if (error) throw error;
  // Update player status
  await supabase.from('players').update({ status: 'Blessé' }).eq('id', payload.player_id);
  await fetchInjuries();
  await fetchPlayers();
  return data;
}
export async function healInjury(injId, playerId) {
  await supabase.from('injuries').update({
    is_active: false, healed_at: new Date().toISOString().split('T')[0]
  }).eq('id', injId);
  await supabase.from('players').update({ status: 'Disponible' }).eq('id', playerId);
  await fetchInjuries();
  await fetchPlayers();
}

// ── PRESENCES ─────────────────────────────────────────────────────
export async function fetchPresences(limit = 10) {
  // Get last N distinct session_dates
  const { data: sessions } = await supabase
    .from('presences')
    .select('session_date')
    .order('session_date', { ascending: false })
    .limit(limit * 3); // over-fetch then deduplicate

  const dates = [...new Set((sessions||[]).map(s=>s.session_date))].slice(0, limit);

  if (!dates.length) { setState({ presences: [] }); return []; }

  const { data } = await supabase
    .from('presences')
    .select('*, players(name,position)')
    .in('session_date', dates)
    .order('session_date', { ascending: false });

  setState({ presences: data || [] });
  return data;
}
export async function savePresenceBatch(sessionDate, sessionType, entries) {
  // entries = [{player_id, status, rpe}]
  const rows = entries.map(e => ({
    player_id: e.player_id,
    session_date: sessionDate,
    session_type: sessionType,
    status: e.status,
    rpe: e.rpe || null,
  }));
  const { error } = await supabase.from('presences').upsert(rows, {
    onConflict: 'player_id,session_date,session_type'
  });
  if (error) throw error;
  await fetchPresences();
}

// ── SCOUTING ──────────────────────────────────────────────────────
export async function fetchScouting() {
  const { data } = await supabase.from('scouting').select('*').order('rank');
  setState({ scouting: data || [] });
  return data;
}

// ── TRAINING PLANS ────────────────────────────────────────────────
export async function fetchPlan(matchId) {
  const { data } = await supabase
    .from('training_plans').select('*')
    .eq('match_id', matchId).maybeSingle();
  if (data) {
    const plans = { ...state.trainingPlans, [matchId]: data };
    setState({ trainingPlans: plans });
  }
  return data;
}
export async function savePlan(matchId, sessions, weekNote) {
  const existing = state.trainingPlans[matchId];
  const payload = {
    match_id: matchId,
    sessions: sessions,
    week_note: weekNote,
    week_start: new Date().toISOString().split('T')[0],
  };
  const { data, error } = existing?.id
    ? await supabase.from('training_plans').update(payload).eq('id', existing.id).select().single()
    : await supabase.from('training_plans').insert(payload).select().single();
  if (error) throw error;
  const plans = { ...state.trainingPlans, [matchId]: data };
  setState({ trainingPlans: plans });
  return data;
}

// ── REALTIME ──────────────────────────────────────────────────────
export function subscribeRealtime(onUpdate) {
  const channel = supabase.channel('rdv-realtime')
    .on('postgres_changes', { event: '*', schema: 'public', table: 'injuries' }, async () => {
      await fetchInjuries(); onUpdate('injuries');
    })
    .on('postgres_changes', { event: '*', schema: 'public', table: 'matches' }, async () => {
      await fetchMatches(); onUpdate('matches');
    })
    .on('postgres_changes', { event: '*', schema: 'public', table: 'presences' }, async () => {
      await fetchPresences(); onUpdate('presences');
    })
    .on('postgres_changes', { event: '*', schema: 'public', table: 'training_plans' }, async () => {
      onUpdate('plans');
    })
    .subscribe();
  return () => supabase.removeChannel(channel);
}

// ── LOAD ALL ──────────────────────────────────────────────────────
export async function loadAll() {
  await Promise.all([
    fetchPlayers(),
    fetchMatches(),
    fetchInjuries(),
    fetchPresences(),
    fetchScouting(),
  ]);
}
