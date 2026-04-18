"""Set pieces (6) — coups francs, corners, kick-in, 4 secondes."""

SETPIECES = [
    {
        "id": "sp-01",
        "category": "setpieces",
        "subcategory": "corner",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Corner combiné — 1er poteau",
        "title_nl": "Corner combinatie — 1e paal",
        "objective_fr": "Organiser un corner court avec appel 1er poteau, déviation.",
        "objective_nl": "Korte hoekschop organiseren met inloop 1e paal, afleiding.",
        "setup_fr": "Gardien. Tireur au corner, 3 attaquants + 2 défenseurs passifs dans la zone.",
        "setup_nl": "Keeper. Nemer bij hoek, 3 aanvallers + 2 passieve verdedigers in zone.",
        "instructions_fr": [
            "Tireur : court vers 1er poteau (centre tendu au sol).",
            "Attaquant 1 (A1) au 1er poteau : fait passer en déviant.",
            "Attaquant 2 (A2) démarque du 2e poteau, tire au 1er poteau ou remise.",
            "Attaquant 3 (A3) en point de penalty pour rebonds.",
            "10 répétitions, noter réussites."
        ],
        "instructions_nl": [
            "Nemer: kort naar 1e paal (strakke grondbal).",
            "A1 op 1e paal: verlengt in één tik.",
            "A2 loskomen van 2e paal, schiet op 1e paal of terugleggen.",
            "A3 op strafschotstip voor rebounds.",
            "10 herhalingen, succes noteren."
        ],
        "variants_fr": [
            "Version 2 : centre aérien pour tête.",
            "Version 3 : tir direct en 2 touches par tireur."
        ],
        "variants_nl": [
            "Versie 2: luchtvoorzet voor kopbal.",
            "Versie 3: direct schot in 2 touches door nemer."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Set plays",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [0, 20], "label": "T"},
                {"type": "ball", "pos": [0, 20]},
                {"type": "player", "team": "red", "pos": [3, 16], "label": "A1"},
                {"type": "player", "team": "red", "pos": [3, 4], "label": "A2"},
                {"type": "player", "team": "red", "pos": [7, 10], "label": "A3"},
                {"type": "player", "team": "blue", "pos": [2, 13], "label": "D"},
                {"type": "player", "team": "blue", "pos": [4, 10], "label": "D"},
                {"type": "arrow", "from": [0, 20], "to": [3, 16], "kind": "ball"},
                {"type": "arrow", "from": [3, 4], "to": [3, 12], "kind": "offense"}
            ]
        }
    },
    {
        "id": "sp-02",
        "category": "setpieces",
        "subcategory": "coup-franc",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Coup franc indirect — combinaison",
        "title_nl": "Indirecte vrije trap — combinatie",
        "objective_fr": "Exécuter 2 variantes de coup-franc : feinte et tir à l'extérieur du mur.",
        "objective_nl": "2 varianten vrije trap: schijnbeweging en schot naast muur.",
        "setup_fr": "Coup-franc à 10 m du but, mur de 3 défenseurs.",
        "setup_nl": "Vrije trap op 10 m van doel, muur van 3 verdedigers.",
        "instructions_fr": [
            "Variante 1 — feinte : joueur A approche, laisse passer. Joueur B frappe au-dessus du mur.",
            "Variante 2 — latéral : A passe en 2 touches à B positionné sur le côté. B frappe en extérieur du pied.",
            "Variante 3 — one-two : A passe court à B, B remise, A frappe.",
            "Alterner les variantes toutes les 3 répétitions.",
            "Gardien avec consigne standard."
        ],
        "instructions_nl": [
            "Variant 1 — schijn: A loopt, laat bal gaan. B schiet over muur.",
            "Variant 2 — lateraal: A past in 2 touches naar B opzij. B schiet met buitenkant.",
            "Variant 3 — een-twee: A kort naar B, B terug, A schiet.",
            "Varianten afwisselen elke 3 herhalingen.",
            "Keeper standaard opdracht."
        ],
        "variants_fr": [
            "Mur à 4 joueurs.",
            "Imposer passe longue avant tir."
        ],
        "variants_nl": [
            "Muur van 4 spelers.",
            "Verplicht lange pass voor schot."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Set pieces",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "blue", "pos": [5, 9], "label": "D"},
                {"type": "player", "team": "blue", "pos": [5, 10], "label": "D"},
                {"type": "player", "team": "blue", "pos": [5, 11], "label": "D"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "A"},
                {"type": "ball", "pos": [10, 10]},
                {"type": "player", "team": "red", "pos": [12, 13], "label": "B"},
                {"type": "arrow", "from": [10, 10], "to": [12, 13], "kind": "ball"},
                {"type": "arrow", "from": [12, 13], "to": [0.5, 8], "kind": "ball"}
            ]
        }
    },
    {
        "id": "sp-03",
        "category": "setpieces",
        "subcategory": "touche",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "faible",
        "title_fr": "Kick-in — relance rapide",
        "title_nl": "Intrap — snelle opbouw",
        "objective_fr": "Exécuter kick-in précis sous pression (règle 4 secondes).",
        "objective_nl": "Precieze intrap onder druk (4-secondenregel).",
        "setup_fr": "Ligne de touche. 1 tireur avec ballon, 2 appuis (1 court, 1 long), 1 presseur.",
        "setup_nl": "Zijlijn. 1 nemer met bal, 2 steunen (1 kort, 1 lang), 1 drukzetter.",
        "instructions_fr": [
            "Tireur a 4 s max pour remettre en jeu.",
            "Option A : passe courte à appui sous pression, retour.",
            "Option B : passe longue à appui en appel profond.",
            "Presseur simule défenseur adverse (marquage court).",
            "Alterner options selon signal coach."
        ],
        "instructions_nl": [
            "Nemer heeft max 4 s.",
            "Optie A: korte pass naar nabije steun, terug.",
            "Optie B: lange pass naar diepe steun.",
            "Drukzetter simuleert verdediger (kortmarkering).",
            "Afwisselen volgens coach-signaal."
        ],
        "variants_fr": [
            "Ajouter 2 appuis + 2 défenseurs.",
            "Chronométrer : 4 s strictes."
        ],
        "variants_nl": [
            "Voeg 2 steunen + 2 verdedigers toe.",
            "Strikte 4 s chrono."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Kick-in",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "player", "team": "red", "pos": [20, 19.5], "label": "T"},
                {"type": "ball", "pos": [20, 19.5]},
                {"type": "player", "team": "red", "pos": [23, 16], "label": "A1"},
                {"type": "player", "team": "red", "pos": [28, 10], "label": "A2"},
                {"type": "player", "team": "blue", "pos": [22, 17], "label": "D"},
                {"type": "arrow", "from": [20, 19.5], "to": [28, 10], "kind": "ball"},
                {"type": "arrow", "from": [20, 19.5], "to": [23, 16], "kind": "ball"}
            ]
        }
    },
    {
        "id": "sp-04",
        "category": "setpieces",
        "subcategory": "penalty",
        "age_range": "U13-Senior",
        "duration": 6,
        "players_min": 2,
        "intensity": "faible",
        "title_fr": "Penalty + 2e penalty (10 m)",
        "title_nl": "Strafschop + 2e strafschop (10 m)",
        "objective_fr": "Répéter les tirs de penalty (6 m) et second penalty (10 m) sous pression.",
        "objective_nl": "Strafschoppen (6 m) en tweede strafschop (10 m) oefenen onder druk.",
        "setup_fr": "Gardien. Points de penalty à 6 m et 10 m.",
        "setup_nl": "Keeper. Strafschotstippen op 6 m en 10 m.",
        "instructions_fr": [
            "Série 1 : 5 penalties à 6 m par joueur.",
            "Série 2 : 5 penalties à 10 m par joueur.",
            "Varier placement : lucarne gauche, lucarne droite, ras du poteau.",
            "Coach note % de réussite.",
            "Concours élimination en fin de séance."
        ],
        "instructions_nl": [
            "Serie 1: 5 strafschoppen op 6 m per speler.",
            "Serie 2: 5 strafschoppen op 10 m per speler.",
            "Varieer plaatsing: hoek links, hoek rechts, paal.",
            "Coach noteert % rake.",
            "Afsluiten: afvalconcours."
        ],
        "variants_fr": [
            "Imposer annoncer le coin avant tir.",
            "Concours équipes : 1v1 après chaque salve."
        ],
        "variants_nl": [
            "Verplicht hoek aankondigen voor schot.",
            "Teamcompetitie: 1v1 na elke serie."
        ],
        "source": "FIFA Futsal Laws of the Game — Penalty kicks",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "cone", "pos": [6, 10]},
                {"type": "cone", "pos": [10, 10]},
                {"type": "player", "team": "red", "pos": [12, 10], "label": "A"},
                {"type": "ball", "pos": [6, 10]},
                {"type": "arrow", "from": [6, 10], "to": [0.5, 13], "kind": "ball"}
            ]
        }
    },
    {
        "id": "sp-05",
        "category": "setpieces",
        "subcategory": "corner direct",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "faible",
        "title_fr": "Corner direct (olympique)",
        "title_nl": "Directe corner (olympisch)",
        "objective_fr": "Exécuter corner rentrant direct à 180° ou vers lucarne.",
        "objective_nl": "Directe corner uitvoeren (ingedraaid of in de hoek).",
        "setup_fr": "Gardien. Tireur au corner, 1 attaquant en zone.",
        "setup_nl": "Keeper. Nemer bij hoek, 1 aanvaller in zone.",
        "instructions_fr": [
            "Tireur frappe brossée avec effet rentrant.",
            "Objectif : ballon directement au 1er ou 2e poteau.",
            "Attaquant prêt à marquer sur rebond gardien.",
            "Alterner pied fort / pied faible (tireur).",
            "5 tentatives par pied."
        ],
        "instructions_nl": [
            "Nemer trapt met effect (ingedraaid).",
            "Doel: bal direct op 1e of 2e paal.",
            "Aanvaller klaar voor rebound.",
            "Afwisselen sterke/zwakke voet.",
            "5 pogingen per voet."
        ],
        "variants_fr": [
            "Imposer coin haut du but (lucarne).",
            "Ajouter 1 défenseur sur la ligne."
        ],
        "variants_nl": [
            "Hoek bovenhoek (kruising) verplicht.",
            "Voeg 1 verdediger op lijn toe."
        ],
        "source": "FIFA Futsal Laws — Corner kick",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [0, 20], "label": "T"},
                {"type": "ball", "pos": [0, 20]},
                {"type": "player", "team": "red", "pos": [4, 10], "label": "A"},
                {"type": "arrow", "from": [0, 20], "to": [0.5, 11], "kind": "ball"}
            ]
        }
    },
    {
        "id": "sp-06",
        "category": "setpieces",
        "subcategory": "mur défensif",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 7,
        "intensity": "faible",
        "title_fr": "Organisation mur défensif",
        "title_nl": "Muur-organisatie verdediging",
        "objective_fr": "Positionner le mur et les autres défenseurs sur coup-franc.",
        "objective_nl": "Muur en andere verdedigers plaatsen bij vrije trap.",
        "setup_fr": "Gardien. Coup-franc à 10 m. 4 défenseurs à organiser.",
        "setup_nl": "Keeper. Vrije trap op 10 m. 4 verdedigers te plaatsen.",
        "instructions_fr": [
            "3 joueurs en mur : côté opposé au pied fort du tireur.",
            "1 défenseur sort sur tireur après coup siffle.",
            "Autres défenseurs marquent attaquants en zone.",
            "GK couvre le côté opposé au mur.",
            "Répéter avec tireur droitier puis gaucher."
        ],
        "instructions_nl": [
            "3 in muur: tegenovergestelde kant van sterke voet nemer.",
            "1 verdediger komt uit op nemer na fluit.",
            "Anderen dekken aanvallers in zone.",
            "Keeper dekt kant zonder muur.",
            "Herhaal met rechtsbeen dan linksbeen nemer."
        ],
        "variants_fr": [
            "Changer position mur selon angle du coup-franc.",
            "Mur 4 pour angles plus centraux."
        ],
        "variants_nl": [
            "Muur verplaatsen volgens hoek.",
            "Muur van 4 bij centrale vrije trap."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Defensive set plays",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 8], "label": "GK"},
                {"type": "player", "team": "blue", "pos": [5, 9], "label": "M"},
                {"type": "player", "team": "blue", "pos": [5, 10], "label": "M"},
                {"type": "player", "team": "blue", "pos": [5, 11], "label": "M"},
                {"type": "player", "team": "blue", "pos": [7, 14], "label": "D"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "T"},
                {"type": "ball", "pos": [10, 10]},
                {"type": "player", "team": "red", "pos": [6, 15], "label": "A"}
            ]
        }
    }
]
