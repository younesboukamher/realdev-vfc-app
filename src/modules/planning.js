// ── Planning logic — RealDev microcycle Lun/Mar/Mer ───────────────

export const EXERCISE_LIBRARY = {
  lundi: {
    base: [
      { name:'Rondo 5v2 chaîne',        detail:'15 min · 2 rondos simultanés · 2 touches max · Transitions rapides',     focus:['technique','ballon'] },
      { name:'Système 1-2-1 offensif',   detail:'20 min · 4v0 → 4v1 → 4v2 · Rotations pivot ↔ ala · Timing appels',      focus:['système','offensif'] },
      { name:'Contre-attaque 3v2',       detail:'15 min · Transition récup → finition en 5s · 4 séries de 5 min',         focus:['transition','vitesse'] },
      { name:'Possession 4v4+GK',        detail:'20 min · Demi-terrain · Conservation + sortie pression · 2 touches',      focus:['possession','collectif'] },
      { name:'Jeu réduit 3v3',           detail:'3×5 min · Pressing constant · Récup 2 min · Intensité croissante',        focus:['technique','pressing'] },
    ],
    vs_pressing: [
      { name:'Sortie de pressing GK+4',  detail:'20 min · GK + 4 joueurs · Schémas relance face pressing · 3 variantes',  focus:['pressing','relance'] },
      { name:'Triangle court sous pression', detail:'15 min · 3v3 espace réduit · 3 passes avant franchissement',          focus:['technique','pression'] },
    ],
    vs_bloc_bas: [
      { name:'Circulation rapide 2-2',   detail:'20 min · 4v4 · Obligation circuler avant tir · Max 3 passes latérales',   focus:['circulation','patience'] },
      { name:'Pivot crochet + finition', detail:'15 min · Pivot dos au but · Combinaison ala-pivot · 3 schémas',           focus:['pivot','finition'] },
    ],
    vs_physique: [
      { name:'Jeu direct pivot',         detail:'15 min · Balles longues GK → pivot · Protection balle · Déviation alas',  focus:['jeu direct','pivot'] },
      { name:'Tempo élevé 4v4',          detail:'4×4 min · Changements de rythme · Pressing immédiat à la perte',          focus:['tempo','intensité'] },
    ],
  },
  mardi: {
    base: [
      { name:'Échauffement dynamique',   detail:'10 min · Mobilité articulaire · Montées genoux · Changements direction',  focus:['échauffement','prévention'] },
      { name:'Sprint 5-10-15m',          detail:'3 séries : 6×5m / 6×10m / 4×15m · Récup 45s · Chronométré',             focus:['vitesse','explosivité'] },
      { name:'Circuit force-équilibre',  detail:'4 stations × 40s · Squats, fentes, gainage, sauts · Repos 30s',          focus:['force','plyométrie'] },
      { name:'Intervalles high-intensity',detail:'6×(20s max + 40s récup) · 3 répétitions · Pause 3 min',                focus:['cardio','anaérobie'] },
      { name:'Renforcement préventif',   detail:'15 min · Ischio excentrique · Adducteurs · Mollets · Proprio cheville',   focus:['prévention','force'] },
    ],
    semaine_chargee: [
      { name:'Volume réduit HI',         detail:'40 min · Sprints courts 5m × 8 · Circuit 3 stations · Récup allongée',    focus:['intensité','fraîcheur'] },
    ],
  },
  mercredi: {
    base: [
      { name:'Analyse vidéo adversaire', detail:'15 min · Système de jeu · Joueur clé · Points faibles · Consignes',      focus:['analyse','tactique'] },
      { name:'5v4+GK — défense',         detail:'20 min · Simulation GK sorti adverse · Organisation 5 défenseurs',        focus:['5v4+GK','défense'] },
      { name:'5v4+GK — attaque',         detail:'15 min · Nos schémas GK sorti · Circulation 3 passes + finition',         focus:['5v4+GK','attaque'] },
      { name:'Set-pieces complets',      detail:'20 min · CF directs + indirects · Corners · Remise jeu GK',               focus:['set-pieces','organisation'] },
      { name:'Jeu 4v4 contextualisé',    detail:'15 min · Règles spécifiques adversaire · Adaptation pressing/bloc',       focus:['contexte','adaptation'] },
    ],
    vs_top6: [
      { name:'Bloc défensif 1-2-1 bas',  detail:'20 min · Organisation serrée · Couverture pivot · Transitions',           focus:['défense','bloc'] },
      { name:'Pressing haut 30s',        detail:'15 min · Pressing intense 30s puis repositionnement · 4v4+GK',            focus:['pressing','organisation'] },
    ],
    vs_bottom: [
      { name:'Rotation 4 de champ',      detail:'20 min · Tous les joueurs pivot en rotation · Créer incertitude',         focus:['rotation','attaque'] },
      { name:'Pressing très haut',       detail:'15 min · Zone haute dès relance adverse · Récupération haute',             focus:['pressing haut','récupération'] },
    ],
  },
};

export function analyzeOpponent(scouting) {
  if (!scouting) return { lundi: [], mardi: [], mercredi: [], consignes: [] };
  const result = { lundi: [], mardi: [], mercredi: [], consignes: [] };
  const rank = parseInt((scouting.rank || 14));

  if (scouting.pressing?.includes('Haut')) {
    result.lundi.push(...EXERCISE_LIBRARY.lundi.vs_pressing);
    result.consignes.push('⚠ Pressing haut adverse → Sortie de pression dès lundi');
  } else if (scouting.system?.toLowerCase().includes('défensif') || scouting.system?.toLowerCase().includes('bas')) {
    result.lundi.push(...EXERCISE_LIBRARY.lundi.vs_bloc_bas);
    result.consignes.push('🧱 Bloc bas adverse → Patience, circulation, exploit pivot');
  }

  if (scouting.strengths?.toLowerCase().includes('physique')) {
    result.lundi.push(...EXERCISE_LIBRARY.lundi.vs_physique);
    result.consignes.push('💪 Adversaire physique → Jeu direct et tempo élevé lundi');
  }

  if (rank <= 4) {
    result.mercredi.push(...EXERCISE_LIBRARY.mercredi.vs_top6);
    result.consignes.push('🏆 TOP 4 — Organisation défensive prioritaire mercredi');
  } else if (rank >= 9) {
    result.mercredi.push(...EXERCISE_LIBRARY.mercredi.vs_bottom);
    result.consignes.push('📈 Bas de tableau — Pressing haut et rotation offensive');
  }

  if (scouting.note_5v4gk?.toLowerCase().includes('prévisible')) {
    result.consignes.push('⚡ 5v4+GK adverse prévisible → Pression immédiate dès sortie GK');
  }
  if (scouting.key_player) {
    result.consignes.push('🎯 Neutraliser: ' + scouting.key_player);
  }

  return result;
}

export function generateMicrocycle(scouting) {
  const analysis = analyzeOpponent(scouting);

  const lundiEx = [
    ...EXERCISE_LIBRARY.lundi.base.slice(0, 2),
    ...(analysis.lundi.length ? [analysis.lundi[0]] : [EXERCISE_LIBRARY.lundi.base[2]]),
  ];
  const mardiEx = EXERCISE_LIBRARY.mardi.base.slice(0, 3);
  const merPool = analysis.mercredi.length
    ? [...EXERCISE_LIBRARY.mercredi.base.slice(0, 2), analysis.mercredi[0], EXERCISE_LIBRARY.mercredi.base[3]]
    : EXERCISE_LIBRARY.mercredi.base.slice(0, 4);

  return {
    sessions: [
      {
        dayName: 'LUNDI', type: 'lundi',
        label: 'Lundi · Tactique & Ballon',
        rpe_target: '5–6', duration: 75,
        objectif: 'Travail technique et tactique collectif — construire le jeu de la semaine',
        focus: ['Technique ballon', 'Système offensif', 'Transitions',
                analysis.lundi.length ? 'Anti-pressing' : 'Rotations'],
        exercises: lundiEx.slice(0, 3),
        notes: '',
      },
      {
        dayName: 'MARDI', type: 'mardi',
        label: 'Mardi · Physique',
        rpe_target: '7–8', duration: 75,
        objectif: 'Pic de charge physique de la semaine — maintenir le niveau D1',
        focus: ['Explosivité', 'Force membres inférieurs', 'Cardio anaérobie', 'Prévention'],
        exercises: mardiEx,
        notes: '',
      },
      {
        dayName: 'MERCREDI', type: 'mercredi',
        label: 'Mercredi · Phases & Prépa match',
        rpe_target: '6–7', duration: 90,
        objectif: 'Préparation spécifique au prochain adversaire — schémas et phases arrêtées',
        focus: ['Analyse adversaire', '5v4+GK', 'Set-pieces',
                scouting ? 'Contre ' + (scouting.opponent_name||'adversaire').split(' ')[0] : 'Organisation défensive'],
        exercises: merPool.slice(0, 3),
        notes: '',
      },
    ],
    analysis,
  };
}
