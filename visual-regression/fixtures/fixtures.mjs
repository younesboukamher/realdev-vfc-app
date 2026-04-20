// Fixtures deterministes — datees en avril 2026 pour etre coherentes avec la
// data prod (saison 2025-2026). Ne PAS utiliser de dates relatives (new Date())
// dans les tests visuels : c'est la source #1 de flakyness.
//
// Pour faire evoluer la fixture : editer ici puis relancer
//   npx playwright test --update-snapshots

const TODAY = '2026-04-20'; // Freeze date pour les screenshots

export const fixtures = {
  authUser: {
    id: 'uid-coach-1',
    email: 'coach@rdv.test',
    role: 'authenticated',
    aud: 'authenticated',
  },

  user_profiles: [
    {
      id: 'uid-coach-1',
      role: 'coach',
      full_name: 'Coach Test',
      favorite_exercises: [],
      players: null,
    },
  ],

  players: [
    { id: 1, number: 1,  name: 'Alex Gardien',        position: 'GK', birthdate: '2000-03-15' },
    { id: 2, number: 4,  name: 'Bruno Defenseur',     position: 'DF', birthdate: '1998-11-02' },
    { id: 3, number: 7,  name: 'Carlos Ailier',       position: 'MF', birthdate: '2001-05-19' },
    { id: 4, number: 10, name: 'Damien Pivot Longuet', position: 'FW', birthdate: '1999-07-22' },
    { id: 5, number: 11, name: 'Ethan Ailier Droit',  position: 'FW', birthdate: '2002-01-30' },
  ],

  matches: [
    // Prochain match : 25/04/2026 (5 jours apres TODAY)
    {
      id: 101,
      match_date: '2026-04-25',
      match_time: '20:30',
      opponent: 'FC Prochain',
      venue: 'home',
      matchday: 'J17',
      result: null,
      goals_for: null,
      goals_against: null,
      lineup: null,
    },
    // Match passe : 17/04/2026 (3 jours avant TODAY, resultat saisi)
    {
      id: 100,
      match_date: '2026-04-17',
      match_time: '20:00',
      opponent: 'FC Passe',
      venue: 'away',
      matchday: 'J16',
      result: 'W',
      goals_for: 4,
      goals_against: 2,
      lineup: null,
    },
  ],

  injuries: [],

  presences: [
    {
      id: 1, player_id: 2, session_date: '2026-04-16', session_type: 'mardi',
      status: 'present', rpe: 6, players: { name: 'Bruno Defenseur', position: 'DF' }
    },
    {
      id: 2, player_id: 3, session_date: '2026-04-16', session_type: 'mardi',
      status: 'late', rpe: 5, players: { name: 'Carlos Ailier', position: 'MF' }
    },
  ],

  scouting: [
    {
      id: 1, rank: 1, opponent: 'FC Prochain',
      strengths: 'pressing haut et transitions rapides',
      weaknesses: 'faiblesse dans les duels aeriens',
      key_players: 'N10 creatif, N7 vif',
    },
  ],

  training_plans: [],

  // metadata (pas une table : utilise par les tests pour piloter les dates)
  TODAY,
};
