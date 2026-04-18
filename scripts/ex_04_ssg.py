"""Small-Sided Games (8) — jeux réduits thématiques."""

SSG = [
    {
        "id": "sg-01",
        "category": "ssg",
        "subcategory": "possession",
        "age_range": "U11-Senior",
        "duration": 12,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "4v4 en 3 zones",
        "title_nl": "4v4 in 3 zones",
        "objective_fr": "Développer circulation par zones, traverser le bloc adverse.",
        "objective_nl": "Circulatie per zone, tegenstanderblok doorkruisen.",
        "setup_fr": "Terrain divisé en 3 zones (10-20-10 m). 2 équipes de 4. Pas de gardien.",
        "setup_nl": "Veld in 3 zones (10-20-10 m). 2 teams van 4. Geen keeper.",
        "instructions_fr": [
            "Pour marquer : franchir les 3 zones avec le ballon.",
            "Max 3 joueurs d'une équipe par zone.",
            "1 point : 6 passes consécutives dans 2 zones différentes.",
            "Au signal coach, changer d'équipe en possession.",
            "Durée : 3 blocs de 4 min, 1 min pause."
        ],
        "instructions_nl": [
            "Om te scoren: 3 zones met bal doorkruisen.",
            "Max 3 spelers van een team per zone.",
            "1 punt: 6 opeenvolgende passes in 2 verschillende zones.",
            "Op signaal coach: balbezit wisselen.",
            "Duur: 3 blokken van 4 min, 1 min pauze."
        ],
        "variants_fr": [
            "Ajouter 2 mini-buts à chaque extrémité.",
            "Interdire retour vers sa zone de départ."
        ],
        "variants_nl": [
            "Voeg 2 minidoeltjes toe aan elk uiteinde.",
            "Terugpass naar beginzone verboden."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), ch.9 SSG",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "player", "team": "red", "pos": [6, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [16, 13], "label": "A2"},
                {"type": "player", "team": "red", "pos": [16, 7], "label": "A3"},
                {"type": "player", "team": "red", "pos": [24, 10], "label": "A4"},
                {"type": "player", "team": "blue", "pos": [16, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [24, 14], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [28, 10], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [32, 10], "label": "D4"},
                {"type": "ball", "pos": [6, 10]},
                {"type": "cone", "pos": [13, 0]},
                {"type": "cone", "pos": [13, 20]},
                {"type": "cone", "pos": [27, 0]},
                {"type": "cone", "pos": [27, 20]}
            ]
        }
    },
    {
        "id": "sg-02",
        "category": "ssg",
        "subcategory": "multi-buts",
        "age_range": "U11-U17",
        "duration": 10,
        "players_min": 8,
        "intensity": "élevée",
        "title_fr": "4v4 quatre mini-buts",
        "title_nl": "4v4 vier minidoelen",
        "objective_fr": "Changer d'orientation rapidement, identifier le but libre.",
        "objective_nl": "Snel wisselen van oriëntatie, vrij doel herkennen.",
        "setup_fr": "Demi-terrain. 4 mini-buts : 2 à chaque extrémité, décalés sur largeur.",
        "setup_nl": "Halve veld. 4 minidoeltjes: 2 aan elk uiteinde, verspreid over breedte.",
        "instructions_fr": [
            "Chaque équipe attaque 2 mini-buts opposés.",
            "Changer de but offensif après chaque but marqué.",
            "Pas de gardien, tirs autorisés à partir de 5 m.",
            "Objectif : scanner la situation pour choisir but libre.",
            "3 blocs de 3 min."
        ],
        "instructions_nl": [
            "Elk team valt 2 minidoeltjes aan de overkant aan.",
            "Na elk doelpunt: wissel doel.",
            "Geen keeper, schot toegestaan vanaf 5 m.",
            "Doel: situatie scannen en vrij doel kiezen.",
            "3 blokken van 3 min."
        ],
        "variants_fr": [
            "Ajouter règle : tir 1 touche uniquement.",
            "Bonus : but avec passe décisive adverse = 2 points."
        ],
        "variants_nl": [
            "Regel: 1-touch schot verplicht.",
            "Bonus: doelpunt na pass op andere kant = 2 punten."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), SSG library",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "cone", "pos": [0, 4]},
                {"type": "cone", "pos": [1, 4]},
                {"type": "cone", "pos": [0, 16]},
                {"type": "cone", "pos": [1, 16]},
                {"type": "cone", "pos": [19, 4]},
                {"type": "cone", "pos": [20, 4]},
                {"type": "cone", "pos": [19, 16]},
                {"type": "cone", "pos": [20, 16]},
                {"type": "player", "team": "red", "pos": [5, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [8, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [8, 6], "label": "A3"},
                {"type": "player", "team": "red", "pos": [11, 10], "label": "A4"},
                {"type": "player", "team": "blue", "pos": [14, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [12, 14], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [12, 6], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [17, 10], "label": "D4"},
                {"type": "ball", "pos": [5, 10]}
            ]
        }
    },
    {
        "id": "sg-03",
        "category": "ssg",
        "subcategory": "transition",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 10,
        "intensity": "élevée",
        "title_fr": "3v3 + 2 jokers neutres",
        "title_nl": "3v3 + 2 neutrale jokers",
        "objective_fr": "Jouer en supériorité offensive permanente, exploiter les jokers.",
        "objective_nl": "Permanente offensieve overmacht, jokers uitbuiten.",
        "setup_fr": "Terrain complet. 3v3 + 2 jokers qui jouent toujours avec l'équipe en possession. Gardiens.",
        "setup_nl": "Volledig veld. 3v3 + 2 jokers altijd met balbezittend team. Keepers.",
        "instructions_fr": [
            "5 joueurs attaquent (3 + 2 jokers), 3 défenseurs.",
            "Jokers limités à 2 touches pour éviter monopolisation.",
            "À la perte, jokers changent de camp (maintien supériorité pour nouvelle équipe en attaque).",
            "Objectif : finir en moins de 12 s.",
            "Bloc 4 min, 2 min pause, répéter 3x."
        ],
        "instructions_nl": [
            "5 aanvallers (3 + 2 jokers), 3 verdedigers.",
            "Jokers max 2 contacten om monopolie te vermijden.",
            "Bij balverlies: jokers wisselen (overmacht behouden voor nieuwe aanvaller).",
            "Doel: afwerken in <12 s.",
            "Blok 4 min, 2 min pauze, 3 herhalingen."
        ],
        "variants_fr": [
            "Réduire jokers à 1 seul.",
            "Imposer : 1 joker côté droit, 1 joker côté gauche."
        ],
        "variants_nl": [
            "Verminder naar 1 joker.",
            "Regel: 1 joker rechts, 1 joker links."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.9",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "gk", "pos": [39.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [14, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [14, 6], "label": "A3"},
                {"type": "player", "team": "yellow", "pos": [20, 12], "label": "J"},
                {"type": "player", "team": "yellow", "pos": [20, 8], "label": "J"},
                {"type": "player", "team": "blue", "pos": [26, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [30, 14], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [30, 6], "label": "D3"},
                {"type": "ball", "pos": [10, 10]}
            ]
        }
    },
    {
        "id": "sg-04",
        "category": "ssg",
        "subcategory": "blitz",
        "age_range": "U11-Senior",
        "duration": 10,
        "players_min": 10,
        "intensity": "élevée",
        "title_fr": "5v5 blitz 60 secondes",
        "title_nl": "5v5 blitz 60 seconden",
        "objective_fr": "Intensité maximale, gestion effort court, transitions permanentes.",
        "objective_nl": "Maximale intensiteit, korte inspanning, continue omschakeling.",
        "setup_fr": "Terrain complet. 2 équipes de 5 (+ gardien). Temps fort et court.",
        "setup_nl": "Volledig veld. 2 teams van 5 (+ keeper). Korte intense blokken.",
        "instructions_fr": [
            "Jeu 5v5 classique, durée 60 s.",
            "Chaque but compte double pendant blitz.",
            "Après 60 s : 90 s récupération.",
            "Alterner avec 3 rotations d'équipes différentes.",
            "Total : 6 blocs de 60 s."
        ],
        "instructions_nl": [
            "Klassiek 5v5, duur 60 s.",
            "Elk doelpunt telt dubbel tijdens blitz.",
            "Na 60 s: 90 s herstel.",
            "Wisselen met 3 verschillende teamrotaties.",
            "Totaal: 6 blokken van 60 s."
        ],
        "variants_fr": [
            "Imposer 1 touche max pendant blitz.",
            "Règle : pas de passe avec GK pendant blitz."
        ],
        "variants_nl": [
            "1-touch verplicht tijdens blitz.",
            "Regel: geen terugspeler naar keeper."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.10",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "gk", "pos": [39.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [14, 15], "label": "2"},
                {"type": "player", "team": "red", "pos": [14, 5], "label": "3"},
                {"type": "player", "team": "red", "pos": [18, 13], "label": "4"},
                {"type": "player", "team": "red", "pos": [18, 7], "label": "5"},
                {"type": "player", "team": "blue", "pos": [30, 10], "label": "1"},
                {"type": "player", "team": "blue", "pos": [26, 15], "label": "2"},
                {"type": "player", "team": "blue", "pos": [26, 5], "label": "3"},
                {"type": "player", "team": "blue", "pos": [22, 13], "label": "4"},
                {"type": "player", "team": "blue", "pos": [22, 7], "label": "5"},
                {"type": "ball", "pos": [14, 15]}
            ]
        }
    }
]

SSG.extend([
    {
        "id": "sg-05",
        "category": "ssg",
        "subcategory": "contraintes",
        "age_range": "U11-U17",
        "duration": 10,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "4v4 2 touches max",
        "title_nl": "4v4 max 2 contacten",
        "objective_fr": "Rapidité d'exécution, qualité du 1er contrôle, choix de passe.",
        "objective_nl": "Snelheid van uitvoering, kwaliteit eerste contact, paskeuze.",
        "setup_fr": "Terrain réduit (20×15 m). 2 équipes de 4. 2 mini-buts.",
        "setup_nl": "Kleiner veld (20×15 m). 2 teams van 4. 2 minidoeltjes.",
        "instructions_fr": [
            "Max 2 touches par joueur.",
            "3e touche = perte de balle (règle stricte).",
            "Tir possible dès que reçu (1 touche).",
            "Exception : pivot fixe peut 3 touches.",
            "3 blocs de 3 min."
        ],
        "instructions_nl": [
            "Max 2 contacten per speler.",
            "3e contact = balverlies (strikte regel).",
            "Schot vanaf ontvangst toegestaan (1-touch).",
            "Uitzondering: vaste pivot mag 3 contacten.",
            "3 blokken van 3 min."
        ],
        "variants_fr": [
            "Passer à 1 touche si dominé.",
            "Ajouter 1 joker neutre à 3 touches."
        ],
        "variants_nl": [
            "1-touch als te makkelijk.",
            "Voeg 1 neutrale joker toe met 3 contacten."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Time pressure",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "cone", "pos": [0, 9]},
                {"type": "cone", "pos": [0, 11]},
                {"type": "cone", "pos": [20, 9]},
                {"type": "cone", "pos": [20, 11]},
                {"type": "player", "team": "red", "pos": [5, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [8, 13], "label": "A2"},
                {"type": "player", "team": "red", "pos": [8, 7], "label": "A3"},
                {"type": "player", "team": "red", "pos": [11, 10], "label": "A4"},
                {"type": "player", "team": "blue", "pos": [15, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [12, 14], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [12, 6], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [18, 10], "label": "D4"},
                {"type": "ball", "pos": [5, 10]}
            ]
        }
    },
    {
        "id": "sg-06",
        "category": "ssg",
        "subcategory": "but extérieur",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "4v4 zones de tir extérieur",
        "title_nl": "4v4 buitenschotzones",
        "objective_fr": "Entraîner la frappe longue distance, utiliser les zones extérieures.",
        "objective_nl": "Trainen op lange afstand schot, buitenzones benutten.",
        "setup_fr": "Terrain complet. 2 équipes + gardiens. Zones à 10-15 m du but marquées.",
        "setup_nl": "Volledig veld. 2 teams + keepers. Zones op 10-15 m van doel gemarkeerd.",
        "instructions_fr": [
            "But 1 point : depuis zone tir (proche).",
            "But 2 points : depuis zone 10-15 m (extérieur).",
            "But 3 points : depuis zone milieu (>15 m).",
            "Interdiction tir direct de relance gardien.",
            "3 blocs de 4 min, 1 min pause."
        ],
        "instructions_nl": [
            "Doelpunt 1 punt: uit schotzone (dichtbij).",
            "Doelpunt 2 punten: uit zone 10-15 m (buiten).",
            "Doelpunt 3 punten: uit middenzone (>15 m).",
            "Direct schot vanaf keeperopbouw verboden.",
            "3 blokken van 4 min, 1 min pauze."
        ],
        "variants_fr": [
            "Ajouter bonus : passe décisive venant de la même zone.",
            "Encourager tir lointain par coach."
        ],
        "variants_nl": [
            "Bonus: assist uit dezelfde zone.",
            "Coach stimuleert afstandsschot."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Shooting zones",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "gk", "pos": [39.5, 10], "label": "GK"},
                {"type": "zone", "pos": [6, 5], "size": [4, 10], "label": "1pt"},
                {"type": "zone", "pos": [10, 3], "size": [5, 14], "label": "2pts"},
                {"type": "zone", "pos": [15, 3], "size": [10, 14], "label": "3pts"},
                {"type": "player", "team": "red", "pos": [12, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [18, 13], "label": "A2"},
                {"type": "player", "team": "red", "pos": [18, 7], "label": "A3"},
                {"type": "player", "team": "red", "pos": [24, 10], "label": "A4"},
                {"type": "player", "team": "blue", "pos": [28, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [22, 15], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [22, 5], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [33, 10], "label": "D4"},
                {"type": "ball", "pos": [18, 13]}
            ]
        }
    },
    {
        "id": "sg-07",
        "category": "ssg",
        "subcategory": "directionnel",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 10,
        "intensity": "moyenne",
        "title_fr": "5v5 règle des couloirs",
        "title_nl": "5v5 regel van de corridors",
        "objective_fr": "Forcer l'utilisation de la largeur, étirer l'adversaire.",
        "objective_nl": "Dwingen tot gebruik van breedte, tegenstander uit elkaar trekken.",
        "setup_fr": "Terrain divisé longitudinalement en 3 couloirs (gauche-centre-droit).",
        "setup_nl": "Veld longitudinaal in 3 corridors (links-midden-rechts).",
        "instructions_fr": [
            "But vaut 1 point normalement.",
            "But après passe de couloir à couloir vaut 2 points.",
            "But après 2 changements de couloir vaut 3 points.",
            "Interdiction : 3 joueurs dans même couloir simultanément.",
            "3 blocs de 3 min."
        ],
        "instructions_nl": [
            "Normaal doelpunt: 1 punt.",
            "Doelpunt na pass corridor-naar-corridor: 2 punten.",
            "Doelpunt na 2 corridorwissels: 3 punten.",
            "Verboden: 3 spelers in zelfde corridor tegelijk.",
            "3 blokken van 3 min."
        ],
        "variants_fr": [
            "Interdire 2 passes de suite dans le même couloir.",
            "Seul le couloir avec ballon peut tirer."
        ],
        "variants_nl": [
            "Verboden 2 opeenvolgende passes in zelfde corridor.",
            "Alleen corridor met bal mag schieten."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), ch.9",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "gk", "pos": [39.5, 10], "label": "GK"},
                {"type": "cone", "pos": [20, 6.7]},
                {"type": "cone", "pos": [10, 6.7]},
                {"type": "cone", "pos": [30, 6.7]},
                {"type": "cone", "pos": [20, 13.3]},
                {"type": "cone", "pos": [10, 13.3]},
                {"type": "cone", "pos": [30, 13.3]},
                {"type": "player", "team": "red", "pos": [10, 3], "label": "A1"},
                {"type": "player", "team": "red", "pos": [15, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [18, 17], "label": "A3"},
                {"type": "player", "team": "red", "pos": [22, 10], "label": "A4"},
                {"type": "player", "team": "red", "pos": [6, 10], "label": "A5"},
                {"type": "ball", "pos": [10, 3]}
            ]
        }
    },
    {
        "id": "sg-08",
        "category": "ssg",
        "subcategory": "ratio",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 10,
        "intensity": "élevée",
        "title_fr": "5v5 ratio attaque/défense",
        "title_nl": "5v5 aanval/verdedigings-ratio",
        "objective_fr": "Match intégré avec thèmes coachés : ratio passes/pertes, tirs cadrés.",
        "objective_nl": "Wedstrijd met coachthema's: pass/verlies ratio, schoten tussen palen.",
        "setup_fr": "Terrain complet. 2 équipes de 5 + gardiens. Coach note statistiques.",
        "setup_nl": "Volledig veld. 2 teams van 5 + keepers. Coach noteert statistieken.",
        "instructions_fr": [
            "Match classique, durée 4×3 min avec coach pause.",
            "Coach note : passes réussies / tentées, tirs cadrés, fautes.",
            "Feedback en fin de bloc, consigne pour bloc suivant.",
            "Équipe qui mène par >2 buts : joue avec 1 joueur en moins.",
            "Objectif : équilibre compétition."
        ],
        "instructions_nl": [
            "Klassieke match, duur 4×3 min met coachpauze.",
            "Coach noteert: geslaagde/gespeelde passes, schoten op doel, fouten.",
            "Feedback na blok, opdracht volgende blok.",
            "Team voorop met >2: 1 speler minder.",
            "Doel: competitieve balans."
        ],
        "variants_fr": [
            "Noter score coach : thème respecté = +1 point.",
            "Imposer un système (1-2-1, 2-2, diamant)."
        ],
        "variants_nl": [
            "Coach-score: thema gerespecteerd = +1 punt.",
            "Systeem opleggen (1-2-1, 2-2, ruit)."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.10 match intégré",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "gk", "pos": [39.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [14, 14], "label": "2"},
                {"type": "player", "team": "red", "pos": [14, 6], "label": "3"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "4"},
                {"type": "player", "team": "red", "pos": [7, 10], "label": "5"},
                {"type": "player", "team": "blue", "pos": [26, 10], "label": "1"},
                {"type": "player", "team": "blue", "pos": [22, 14], "label": "2"},
                {"type": "player", "team": "blue", "pos": [22, 6], "label": "3"},
                {"type": "player", "team": "blue", "pos": [30, 10], "label": "4"},
                {"type": "player", "team": "blue", "pos": [33, 10], "label": "5"},
                {"type": "ball", "pos": [14, 14]}
            ]
        }
    }
])
