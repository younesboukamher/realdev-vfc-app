"""Gardien (8) — GK specific exercises."""

GARDIEN = [
    {
        "id": "gk-01",
        "category": "gardien",
        "subcategory": "position",
        "age_range": "U11-Senior",
        "duration": 8,
        "players_min": 2,
        "intensity": "faible",
        "title_fr": "Position de base + déplacement",
        "title_nl": "Basispositie + verplaatsing",
        "objective_fr": "Ancrer position de base GK futsal (pieds largeur épaules, fléchi, mains prêtes).",
        "objective_nl": "Basispositie inprenten (voeten schouderbreedte, gebogen, handen klaar).",
        "setup_fr": "Gardien dans ses 6 m. Coach à 8 m avec ballons.",
        "setup_nl": "Keeper in eigen 6 m. Coach op 8 m met ballen.",
        "instructions_fr": [
            "Coach signale couleur → GK se déplace en pas chassé au cône correspondant.",
            "Retour systématique à position centrale après chaque action.",
            "Garder position basse et active tout le temps.",
            "10 signaux, 30 s pause entre séries.",
            "Corriger la distance mains/cuisses, pieds parallèles."
        ],
        "instructions_nl": [
            "Coach signaleert kleur → keeper verplaatst in chassé naar juiste kegel.",
            "Systematische terugkeer naar centrum na elke actie.",
            "Lage actieve positie altijd behouden.",
            "10 signalen, 30 s pauze tussen series.",
            "Handen/dijen afstand corrigeren, voeten parallel."
        ],
        "variants_fr": [
            "Ajouter tir après chaque déplacement.",
            "Varier signal : auditif, visuel, mixte."
        ],
        "variants_nl": [
            "Schot na elke verplaatsing.",
            "Signaal variëren: auditief, visueel, mix."
        ],
        "source": "FIFA Futsal Goalkeeper Manual (2023), ch.2",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "cone", "pos": [3, 8]},
                {"type": "cone", "pos": [3, 12]},
                {"type": "cone", "pos": [5, 10]},
                {"type": "player", "team": "yellow", "pos": [10, 10], "label": "C"},
                {"type": "ball", "pos": [10, 10]}
            ]
        }
    },
    {
        "id": "gk-02",
        "category": "gardien",
        "subcategory": "réflexes",
        "age_range": "U11-Senior",
        "duration": 8,
        "players_min": 2,
        "intensity": "élevée",
        "title_fr": "Réflexes — multi-ballons",
        "title_nl": "Reflexen — multi-ballen",
        "objective_fr": "Temps de réaction sur tirs rapprochés successifs.",
        "objective_nl": "Reactietijd op opeenvolgende schoten dichtbij.",
        "setup_fr": "GK en place. Coach à 5 m avec 8-10 ballons.",
        "setup_nl": "Keeper staat. Coach op 5 m met 8-10 ballen.",
        "instructions_fr": [
            "Coach tire à rythme soutenu, chaque 2 s.",
            "Alterner : gauche bas, droite mi-hauteur, lucarne, pieds.",
            "GK doit rester debout et actif entre chaque tir.",
            "10 ballons par série, 45 s récupération.",
            "3 séries."
        ],
        "instructions_nl": [
            "Coach schiet vlot, elke 2 s.",
            "Afwisselen: links laag, rechts half, kruising, voeten.",
            "Keeper blijft staan en actief tussen schoten.",
            "10 ballen per serie, 45 s herstel.",
            "3 series."
        ],
        "variants_fr": [
            "Faire rebondir ballon sol avant tir.",
            "Ajouter obstacle visuel temporaire."
        ],
        "variants_nl": [
            "Bal op grond laten stuiten voor schot.",
            "Tijdelijk visueel obstakel."
        ],
        "source": "FIFA Futsal Goalkeeper Manual (2023), Reflexes",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "player", "team": "yellow", "pos": [6, 10], "label": "C"},
                {"type": "ball", "pos": [6, 10]},
                {"type": "arrow", "from": [6, 10], "to": [1, 7], "kind": "ball"},
                {"type": "arrow", "from": [6, 10], "to": [1, 13], "kind": "ball"}
            ]
        }
    },
    {
        "id": "gk-03",
        "category": "gardien",
        "subcategory": "relance",
        "age_range": "U11-Senior",
        "duration": 10,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Relance main + pied",
        "title_nl": "Opbouw met hand + voet",
        "objective_fr": "Précision de la relance : main (courte), pied (longue).",
        "objective_nl": "Precisie opbouw: hand (kort), voet (lang).",
        "setup_fr": "GK dans ses 6 m. 3 appuis à 10, 20 et 30 m.",
        "setup_nl": "Keeper in eigen 6 m. 3 steunen op 10, 20 en 30 m.",
        "instructions_fr": [
            "Relance main à appui proche (10 m) : précision à 2 m près.",
            "Relance pied à appui moyen (20 m) : passe au sol.",
            "Relance pied longue (30 m) : ballon aérien à cible mobile.",
            "Alterner les 3 types à chaque tour.",
            "10 relances par type."
        ],
        "instructions_nl": [
            "Handworp naar dichte steun (10 m): precisie op 2 m.",
            "Trap naar middelste steun (20 m): grondpass.",
            "Lange trap (30 m): luchtbal naar bewegend doel.",
            "3 types afwisselen elke ronde.",
            "10 herhalingen per type."
        ],
        "variants_fr": [
            "Ajouter pressing sur l'appui.",
            "Imposer relance sous 4 s."
        ],
        "variants_nl": [
            "Druk op steun toevoegen.",
            "Opbouw binnen 4 s."
        ],
        "source": "FIFA Futsal Goalkeeper Manual (2023), Distribution",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "ball", "pos": [1, 10]},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [20, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [30, 10], "label": "A3"},
                {"type": "arrow", "from": [1, 10], "to": [10, 10], "kind": "ball"},
                {"type": "arrow", "from": [1, 10], "to": [20, 14], "kind": "ball"},
                {"type": "arrow", "from": [1, 10], "to": [30, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "gk-04",
        "category": "gardien",
        "subcategory": "duel",
        "age_range": "U11-Senior",
        "duration": 10,
        "players_min": 4,
        "intensity": "élevée",
        "title_fr": "Sortie sur duel 1v1",
        "title_nl": "Uittreden bij 1v1",
        "objective_fr": "Gérer le duel face à attaquant lancé : sortir ou attendre.",
        "objective_nl": "1v1 beheren tegen ingelopen aanvaller: uittreden of wachten.",
        "setup_fr": "GK en place. Attaquant part à 15 m, ballon au pied.",
        "setup_nl": "Keeper staat. Aanvaller start op 15 m, bal aan voet.",
        "instructions_fr": [
            "Attaquant part en conduite vers but.",
            "GK évalue à quel moment sortir : angle, vitesse, surface au pied.",
            "Principe : fermer angle à l'étoile (gros).",
            "Varier vitesse de course attaquant.",
            "10 duels par série, 3 séries."
        ],
        "instructions_nl": [
            "Aanvaller dribbelt naar doel.",
            "Keeper bepaalt wanneer uit te komen: hoek, snelheid, balpositie.",
            "Principe: hoek sluiten als 'ster' (groot).",
            "Variëer loopsnelheid aanvaller.",
            "10 duels per serie, 3 series."
        ],
        "variants_fr": [
            "Ajouter 2e attaquant en soutien (2v1).",
            "Attaquant arrive après rebond coach."
        ],
        "variants_nl": [
            "Voeg 2e aanvaller in steun toe (2v1).",
            "Aanvaller komt na rebound coach."
        ],
        "source": "FIFA Futsal Goalkeeper Manual (2023), 1v1",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [15, 10], "label": "A"},
                {"type": "ball", "pos": [15, 10]},
                {"type": "arrow", "from": [15, 10], "to": [4, 10], "kind": "offense"},
                {"type": "arrow", "from": [1, 10], "to": [4, 10], "kind": "defense"}
            ]
        }
    }
]

GARDIEN.extend([
    {
        "id": "gk-05",
        "category": "gardien",
        "subcategory": "plongeon",
        "age_range": "U11-Senior",
        "duration": 8,
        "players_min": 2,
        "intensity": "moyenne",
        "title_fr": "Plongeon latéral — bas",
        "title_nl": "Zijwaartse duik — laag",
        "objective_fr": "Technique du plongeon latéral sur ballon ras du sol.",
        "objective_nl": "Techniek zijwaartse duik op laag schot.",
        "setup_fr": "GK dans les 6 m, genoux fléchis, mains prêtes.",
        "setup_nl": "Keeper in 6 m, knieën gebogen, handen klaar.",
        "instructions_fr": [
            "Coach sert ballon roulé à 2 m à gauche ou droite.",
            "GK plonge jambe opposée pousse, main avant puis main arrière.",
            "Atterrissage côté du ballon, amortir épaule.",
            "10 plongeons par côté.",
            "Coach corrige position mains et épaules."
        ],
        "instructions_nl": [
            "Coach rolt bal op 2 m links of rechts.",
            "Keeper duikt, tegenoverliggend been duwt, voorste hand dan achterste hand.",
            "Landing op balkant, schouder dempen.",
            "10 duiken per kant.",
            "Coach corrigeert positie handen/schouders."
        ],
        "variants_fr": [
            "Ballon aérien mi-hauteur.",
            "Ballon de coach en multi-service (2 ballons successifs)."
        ],
        "variants_nl": [
            "Halfhoge luchtbal.",
            "Multi-service (2 ballen op rij)."
        ],
        "source": "FIFA Futsal Goalkeeper Manual (2023), Diving",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "player", "team": "yellow", "pos": [5, 10], "label": "C"},
                {"type": "ball", "pos": [5, 10]},
                {"type": "arrow", "from": [5, 10], "to": [1, 7], "kind": "ball"},
                {"type": "arrow", "from": [5, 10], "to": [1, 13], "kind": "ball"}
            ]
        }
    },
    {
        "id": "gk-06",
        "category": "gardien",
        "subcategory": "jeu au pied",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 5,
        "intensity": "moyenne",
        "title_fr": "GK-joueur — construction",
        "title_nl": "Keeper-veldspeler — opbouw",
        "objective_fr": "GK impliqué dans construction avec les pieds, sous pression modérée.",
        "objective_nl": "Keeper betrokken bij opbouw met voeten, onder matige druk.",
        "setup_fr": "4 joueurs + GK dans moitié défensive. 2 presseurs adverses.",
        "setup_nl": "4 spelers + keeper op eigen helft. 2 drukzetters.",
        "instructions_fr": [
            "GK reçoit ballon, joue avec les pieds uniquement.",
            "Option 1 : passe courte à défenseur latéral.",
            "Option 2 : passe longue à joueur en appel profond.",
            "Presseurs tentent récupération.",
            "Compter 10 constructions réussies / série."
        ],
        "instructions_nl": [
            "Keeper krijgt bal, speelt enkel met voeten.",
            "Optie 1: korte pass naar lateraal verdediger.",
            "Optie 2: lange pass naar diepe steun.",
            "Drukzetters proberen recuperatie.",
            "10 geslaagde opbouwacties per serie."
        ],
        "variants_fr": [
            "Réduire à 3v3 pour intensifier.",
            "Imposer 2 touches max pour GK."
        ],
        "variants_nl": [
            "Verklein naar 3v3 voor intensiteit.",
            "Max 2 contacten voor keeper."
        ],
        "source": "RFEF — Fútbol sala, portero como jugador",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "ball", "pos": [1, 10]},
                {"type": "player", "team": "red", "pos": [5, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [5, 6], "label": "A2"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "A3"},
                {"type": "player", "team": "red", "pos": [15, 10], "label": "A4"},
                {"type": "player", "team": "blue", "pos": [7, 12], "label": "P1"},
                {"type": "player", "team": "blue", "pos": [7, 8], "label": "P2"},
                {"type": "arrow", "from": [1, 10], "to": [5, 14], "kind": "ball"}
            ]
        }
    },
    {
        "id": "gk-07",
        "category": "gardien",
        "subcategory": "centres",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 3,
        "intensity": "moyenne",
        "title_fr": "Sortie sur centre aérien",
        "title_nl": "Uittreden op voorzet",
        "objective_fr": "Lecture de trajectoire, timing du saut, prise de balle ou déviation.",
        "objective_nl": "Traject lezen, sprongtiming, bal vangen of weggeven.",
        "setup_fr": "GK en place. Centreur à l'aile, 1 attaquant + 1 défenseur en zone.",
        "setup_nl": "Keeper staat. Voorzetter op vleugel, 1 aanvaller + 1 verdediger in zone.",
        "instructions_fr": [
            "Centre aérien venant de l'aile.",
            "GK évalue : sortir avec mains ou rester en ligne.",
            "Si sortie : appel 'GK\!' + saut + prise à 2 mains.",
            "Si rester : couvrir ligne de but, anticiper tête.",
            "Alterner centreur gauche / droit."
        ],
        "instructions_nl": [
            "Luchtvoorzet vanaf vleugel.",
            "Keeper bepaalt: met handen uit of op lijn blijven.",
            "Bij uit: 'GK\!' roepen + sprong + 2 handen vangen.",
            "Bij blijven: doellijn dekken, kop anticiperen.",
            "Voorzet afwisselend links/rechts."
        ],
        "variants_fr": [
            "Ajouter 2e attaquant pour obstacle.",
            "Varier hauteur du centre."
        ],
        "variants_nl": [
            "2e aanvaller als obstakel.",
            "Variëer hoogte voorzet."
        ],
        "source": "FIFA Futsal Goalkeeper Manual (2023), Crosses",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [10, 17], "label": "C"},
                {"type": "ball", "pos": [10, 17]},
                {"type": "player", "team": "red", "pos": [4, 11], "label": "A"},
                {"type": "player", "team": "blue", "pos": [4, 9], "label": "D"},
                {"type": "arrow", "from": [10, 17], "to": [4, 11], "kind": "ball"}
            ]
        }
    },
    {
        "id": "gk-08",
        "category": "gardien",
        "subcategory": "fatigue",
        "age_range": "U15-Senior",
        "duration": 10,
        "players_min": 4,
        "intensity": "élevée",
        "title_fr": "Circuit GK haute intensité",
        "title_nl": "Keeper-circuit hoge intensiteit",
        "objective_fr": "Enchaîner actions rapides pour travailler résistance spécifique.",
        "objective_nl": "Snelle acties opvolgen voor specifieke weerstand.",
        "setup_fr": "GK en place. 3 stations : tir frontal, tir latéral, centre. Coaches en rotation.",
        "setup_nl": "Keeper staat. 3 stations: schot centraal, zijdelings, voorzet. Coaches in rotatie.",
        "instructions_fr": [
            "Station 1 — Tir frontal (8 m), 5 tirs en 20 s.",
            "Station 2 — Tir latéral (angle fermé), 5 tirs en 20 s.",
            "Station 3 — Centre aérien + rebond, 5 actions en 30 s.",
            "Pause 30 s entre stations, 2 min après circuit complet.",
            "3 circuits complets."
        ],
        "instructions_nl": [
            "Station 1 — Centraal schot (8 m), 5 schoten in 20 s.",
            "Station 2 — Zijschot (gesloten hoek), 5 schoten in 20 s.",
            "Station 3 — Luchtvoorzet + rebound, 5 acties in 30 s.",
            "30 s pauze tussen stations, 2 min na volledig circuit.",
            "3 volledige circuits."
        ],
        "variants_fr": [
            "Ajouter récupération active (jongles).",
            "Filmer pour analyser posture en fatigue."
        ],
        "variants_nl": [
            "Actief herstel (jongleren).",
            "Filmen voor houding bij vermoeidheid."
        ],
        "source": "FIFA Futsal Goalkeeper Manual (2023), Conditioning",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [1, 10], "label": "GK"},
                {"type": "player", "team": "yellow", "pos": [9, 10], "label": "C1"},
                {"type": "player", "team": "yellow", "pos": [8, 4], "label": "C2"},
                {"type": "player", "team": "yellow", "pos": [10, 17], "label": "C3"},
                {"type": "ball", "pos": [9, 10]},
                {"type": "ball", "pos": [8, 4]},
                {"type": "ball", "pos": [10, 17]},
                {"type": "arrow", "from": [9, 10], "to": [1, 10], "kind": "ball"},
                {"type": "arrow", "from": [8, 4], "to": [1, 11], "kind": "ball"},
                {"type": "arrow", "from": [10, 17], "to": [3, 12], "kind": "ball"}
            ]
        }
    }
])
