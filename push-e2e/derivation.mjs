// Reproduction fidele de la logique de derivation de date cote Edge Function.
// Doit correspondre EXACTEMENT a :
//   - supabase/functions/send-pre-session-notifications/index.ts (cron backend)
//   - pl2BuildMonthData() dans index.html L6592 (vue calendaire frontend)

export const DAY_IDX_OF_TYPE = Object.freeze({
  dimanche: 0,
  lundi:    1,
  mardi:    2,
  mercredi: 3,
  jeudi:    4,
  vendredi: 5,
  samedi:   6,
});

function pad2(n) { return String(n).padStart(2, '0'); }

export function isoDate(y, m, d) { return `${y}-${pad2(m)}-${pad2(d)}`; }

export function deriveSessionDate(matchDateISO, sessionType) {
  if (!matchDateISO || !sessionType) return null;
  const tp = String(sessionType).toLowerCase();
  const trainDow = DAY_IDX_OF_TYPE[tp];
  if (trainDow == null) return null;

  const matchD = new Date(matchDateISO + 'T12:00:00Z');
  if (isNaN(matchD.getTime())) return null;
  const matchDow = matchD.getUTCDay();

  let diff = matchDow - trainDow;
  if (diff <= 0) diff += 7;

  const sessD = new Date(matchD);
  sessD.setUTCDate(sessD.getUTCDate() - diff);
  return isoDate(sessD.getUTCFullYear(), sessD.getUTCMonth() + 1, sessD.getUTCDate());
}

export function sessionsForDate(plans, matchDateById, targetDateISO) {
  const out = [];
  for (const pl of (plans || [])) {
    const mdate = matchDateById[pl.match_id];
    if (!mdate) continue;
    for (const s of (pl.sessions || [])) {
      if (!s) continue;
      const explicit = s.date || s.session_date;
      if (explicit) {
        if (String(explicit).slice(0, 10) === targetDateISO) {
          out.push({ match_id: pl.match_id, session: s, derivedDate: targetDateISO });
        }
        continue;
      }
      const derived = deriveSessionDate(mdate, s.type);
      if (derived === targetDateISO) {
        out.push({ match_id: pl.match_id, session: s, derivedDate: derived });
      }
    }
  }
  return out;
}
