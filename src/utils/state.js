// ── Global app state ──────────────────────────────────────────────
export const state = {
  user:     null,   // auth.user
  profile:  null,   // user_profiles row
  role:     null,   // 'admin'|'coach'|'physio'|'gk'|'player'
  lang:     localStorage.getItem('rdv_lang') || 'fr',
  offline:  false,

  // cached data (refreshed on login + realtime)
  players:  [],
  matches:  [],
  injuries: [],     // active only
  injHistory: [],   // healed
  presences: [],
  scouting: [],
  trainingPlans: {},

  // UI state
  currentPage: 'dashboard',
  planningMatchIdx: null,
  expandedDays: new Set(),
};

// ── Listeners ─────────────────────────────────────────────────────
const _listeners = {};
export function on(event, fn)  { (_listeners[event] = _listeners[event] || []).push(fn); }
export function off(event, fn) { _listeners[event] = (_listeners[event]||[]).filter(f=>f!==fn); }
export function emit(event, data) { (_listeners[event]||[]).forEach(fn => fn(data)); }

export function setState(patch) {
  Object.assign(state, patch);
  emit('stateChange', patch);
}
