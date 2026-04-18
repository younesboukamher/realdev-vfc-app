"""Defense (6) — individual and collective defensive work."""

DEFENSE = [
    {
        "id": "df-01",
        "category": "defense",
        "subcategory": "marquage",
        "age_range": "U11-Senior",
        "duration": 10,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Marquage individuel — ombre",
        "title_nl": "Individuele dekking — schaduw",
        "objective_fr": "Position de marquage : distance, orientation, appui arrière actif.",
        "objective_nl": "Dekkingpositie: afstand, oriëntatie, actieve steun achteraan.",
        "setup_fr": "Paires attaquant/défenseur. Zone 15×10 m. 1 ballon au coach.",
        "setup_nl": "Paren aanvaller/verdediger. Zone 15×10 m. 1 bal bij coach.",
        "instructions_fr": [
            "Coach sert ballon aléatoirement à un attaquant.",
            "Défenseur marque à 1,5 m, orienté légèrement côté ballon.",
            "Attaquant tente dribble ou passe.",
            "Défenseur doit rester entre attaquant et but.",
            "Rotation après 30 s, analyser distance et orientation."
        ],
        "instructions_nl": [
            "Coach bedient willekeurig aanvaller.",
            "Verdediger dekt op 1,5 m, licht naar balkant gericht.",
            "Aanvaller probeert dribbel of pass.",
            "Verdediger blijft tussen aanvaller en doel.",
            "Rotatie na 30 s, afstand en oriëntatie analyseren."
        ],
        "variants_fr": [
            "Ajouter règle : défenseur ne peut reculer qu'en pas chassé.",
            "Réduire zone pour densité."
        ],
        "variants_nl": [
            "Verdediger mag alleen in chassé achteruit.",
            "Zone verkleinen voor dichtheid."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Individual defending",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "red", "pos": [14, 10], "label": "A"},
                {"type": "ball", "pos": [14, 10]},
                {"type": "player", "team": "blue", "pos": [11, 10], "label": "D"},
                {"type": "player", "team": "red", "pos": [8, 14], "label": "A"},
                {"type": "player", "team": "blue", "pos": [6, 14], "label": "D"},
                {"type": "player", "team": "yellow", "pos": [18, 10], "label": "C"}
            ]
        }
    },
    {
        "id": "df-02",
        "category": "defense",
        "subcategory": "tacle",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Tacle rasant + récupération",
        "title_nl": "Sliding + recuperatie",
        "objective_fr": "Technique du tacle rasant (1 jambe étendue), prévention faute.",
        "objective_nl": "Techniek van sliding (1 been gestrekt), fout vermijden.",
        "setup_fr": "Attaquant en conduite, défenseur de côté. Zone 10×5 m.",
        "setup_nl": "Aanvaller dribbelt, verdediger zijwaarts. Zone 10×5 m.",
        "instructions_fr": [
            "Attaquant conduit sur 10 m.",
            "Défenseur arrive en diagonale et tacle ballon uniquement.",
            "Jambe d'appui fléchie, jambe d'attaque tendue pour sortir ballon.",
            "Relevé rapide et récupération course.",
            "Alterner rôles toutes les 3 répétitions."
        ],
        "instructions_nl": [
            "Aanvaller dribbelt over 10 m.",
            "Verdediger komt diagonaal en tackelt enkel de bal.",
            "Steunbeen gebogen, aanvalsbeen gestrekt om bal weg te halen.",
            "Snel opstaan en in loop hernemen.",
            "Rolwissel elke 3 herhalingen."
        ],
        "variants_fr": [
            "Ajouter finition : défenseur doit sortir ballon en touche.",
            "Coach évalue hauteur du tacle (pas au-dessus genou)."
        ],
        "variants_nl": [
            "Verdediger moet bal in 'uit' werken.",
            "Coach evalueert hoogte tackle (niet boven knie)."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Tackling",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "red", "pos": [15, 10], "label": "A"},
                {"type": "ball", "pos": [15, 10]},
                {"type": "player", "team": "blue", "pos": [14, 13], "label": "D"},
                {"type": "arrow", "from": [15, 10], "to": [5, 10], "kind": "offense"},
                {"type": "arrow", "from": [14, 13], "to": [12, 10], "kind": "defense"}
            ]
        }
    },
    {
        "id": "df-03",
        "category": "defense",
        "subcategory": "coulissage",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Coulissage en ligne 3 défenseurs",
        "title_nl": "Verschuiven met 3 verdedigers",
        "objective_fr": "Travailler la ligne défensive qui coulisse en fonction du ballon.",
        "objective_nl": "Defensieve lijn laten verschuiven volgens de bal.",
        "setup_fr": "3 défenseurs en ligne, 3 attaquants face (15 m). Coach derrière attaquants.",
        "setup_nl": "3 verdedigers op lijn, 3 aanvallers tegenover (15 m). Coach achter aanvallers.",
        "instructions_fr": [
            "Coach nomme un attaquant → celui-ci reçoit ballon.",
            "Les 3 défenseurs coulissent : 1 presse porteur, 2 couvrent.",
            "Distance défenseurs : 3-4 m maximum.",
            "Changer d'attaquant porteur, ligne doit coulisser fluide.",
            "3 min d'exercice, 30 s pause, 3 séries."
        ],
        "instructions_nl": [
            "Coach noemt aanvaller → die ontvangt bal.",
            "3 verdedigers verschuiven: 1 druk, 2 dekking.",
            "Afstand verdedigers: max 3-4 m.",
            "Balbezitter wisselt, lijn verschuift soepel.",
            "3 min oefening, 30 s rust, 3 series."
        ],
        "variants_fr": [
            "Ajouter 4e défenseur en couverture.",
            "Attaquants avec 2 touches max."
        ],
        "variants_nl": [
            "4e verdediger in dekking.",
            "Aanvallers max 2 contacten."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.236",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "player", "team": "blue", "pos": [10, 14], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [10, 10], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [10, 6], "label": "D3"},
                {"type": "player", "team": "red", "pos": [18, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [18, 6], "label": "A3"},
                {"type": "ball", "pos": [18, 14]},
                {"type": "arrow", "from": [10, 14], "to": [14, 14], "kind": "defense"},
                {"type": "arrow", "from": [10, 10], "to": [12, 12], "kind": "defense"},
                {"type": "arrow", "from": [10, 6], "to": [12, 8], "kind": "defense"}
            ]
        }
    },
    {
        "id": "df-04",
        "category": "defense",
        "subcategory": "repli",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 8,
        "intensity": "élevée",
        "title_fr": "Repli défensif rapide",
        "title_nl": "Snel defensief terugloopwerk",
        "objective_fr": "Transition perte de balle → organisation défensive en <5 s.",
        "objective_nl": "Transitie balverlies → verdedigingsorganisatie binnen 5 s.",
        "setup_fr": "Terrain complet. 4 attaquants vs 4 défenseurs + GK. Coach signale perte.",
        "setup_nl": "Volledig veld. 4 aanvallers vs 4 verdedigers + GK. Coach signaleert verlies.",
        "instructions_fr": [
            "Phase 1 : attaquants font circuler le ballon.",
            "Coach siffle, ballon donné aux adverses.",
            "Équipe en perte : repli sprint, bloquer retour attaquant proche.",
            "Objectif : reformer bloc 2-2 en 5 s.",
            "Alterner rôles toutes les 3 min."
        ],
        "instructions_nl": [
            "Fase 1: aanvallers doen bal circuleren.",
            "Coach fluit, bal naar tegenstander.",
            "Verliezend team: sprint terug, dichtste aanvaller bij bal vooruit-stoppen.",
            "Doel: blok 2-2 hervormen binnen 5 s.",
            "Rolwissel elke 3 min."
        ],
        "variants_fr": [
            "Imposer 1 joueur reste en haut (pressing future).",
            "Mesurer temps de repli avec chronomètre."
        ],
        "variants_nl": [
            "1 speler blijft vooraan (toekomstige druk).",
            "Terugloop-tijd meten met chrono."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Transition",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [22, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [22, 6], "label": "A2"},
                {"type": "player", "team": "red", "pos": [27, 14], "label": "A3"},
                {"type": "player", "team": "red", "pos": [27, 6], "label": "A4"},
                {"type": "player", "team": "blue", "pos": [30, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [35, 14], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [35, 6], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [38, 10], "label": "D4"},
                {"type": "ball", "pos": [30, 10]},
                {"type": "arrow", "from": [35, 14], "to": [25, 14], "kind": "defense"},
                {"type": "arrow", "from": [35, 6], "to": [25, 6], "kind": "defense"}
            ]
        }
    },
    {
        "id": "df-05",
        "category": "defense",
        "subcategory": "duel aérien",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Duel aérien + dégagement",
        "title_nl": "Luchtduel + wegwerken",
        "objective_fr": "Timing du saut, positionnement du corps, dégagement orienté.",
        "objective_nl": "Sprongtiming, lichaamspositionering, gericht wegwerken.",
        "setup_fr": "Coach sert balle aérienne à 5 m. Attaquant + défenseur en duel.",
        "setup_nl": "Coach bedient luchtbal op 5 m. Aanvaller + verdediger in duel.",
        "instructions_fr": [
            "Coach sert ballon aérien entre les 2.",
            "Défenseur doit dégager de la tête ou du pied en sécurité.",
            "Attaquant tente reprise directe.",
            "Alterner rôles et côtés de service.",
            "10 duels par joueur."
        ],
        "instructions_nl": [
            "Coach bedient luchtbal tussen beiden.",
            "Verdediger moet met hoofd of voet veilig wegwerken.",
            "Aanvaller probeert directe afronding.",
            "Rollen en zijdes afwisselen.",
            "10 duels per speler."
        ],
        "variants_fr": [
            "Ajouter but pour attaquant.",
            "Défenseur doit dégager vers une zone cible."
        ],
        "variants_nl": [
            "Doel voor aanvaller.",
            "Verdediger wegwerken naar doelzone."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Aerial duels",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "yellow", "pos": [12, 15], "label": "C"},
                {"type": "ball", "pos": [12, 15]},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "A"},
                {"type": "player", "team": "blue", "pos": [9, 10], "label": "D"},
                {"type": "arrow", "from": [12, 15], "to": [10, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "df-06",
        "category": "defense",
        "subcategory": "communication",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "Bloc défensif verbal",
        "title_nl": "Verbaal verdedigingsblok",
        "objective_fr": "Imposer communication entre défenseurs : appels, switch, couverture.",
        "objective_nl": "Communicatie tussen verdedigers: 'mij', 'switch', 'dekking'.",
        "setup_fr": "4 défenseurs vs 4 attaquants, demi-terrain. GK en place.",
        "setup_nl": "4 verdedigers vs 4 aanvallers, halve veld. GK staat.",
        "instructions_fr": [
            "Règle : chaque défenseur DOIT crier à chaque action.",
            "'Mien\!' = je prends le porteur.",
            "'Switch\!' = on échange de marquage.",
            "'Couvre\!' = je demande couverture.",
            "Perte de balle sans communication = 1 tour de terrain."
        ],
        "instructions_nl": [
            "Regel: elke verdediger MOET roepen bij elke actie.",
            "'Mij\!' = ik pak balbezitter.",
            "'Switch\!' = we wisselen dekking.",
            "'Dek\!' = ik vraag dekking.",
            "Balverlies zonder communicatie = 1 rondje veld."
        ],
        "variants_fr": [
            "Interdire parole en 1er bloc pour illustrer différence.",
            "Filmer et analyser à la fin."
        ],
        "variants_nl": [
            "Eerste blok stil om verschil te tonen.",
            "Filmen en nabespreken."
        ],
        "source": "RFEF — Coaching defensivo, comunicación",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "blue", "pos": [6, 13], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [6, 7], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [10, 13], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [10, 7], "label": "D4"},
                {"type": "player", "team": "red", "pos": [15, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [15, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [15, 6], "label": "A3"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "A4"},
                {"type": "ball", "pos": [15, 10]}
            ]
        }
    }
]
