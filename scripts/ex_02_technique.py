"""Technical exercises (15) — conduite, passe, contrôle, finition technique."""

TECHNIQUE = [
    {
        "id": "te-01",
        "category": "technique",
        "subcategory": "conduite",
        "age_range": "U11-U15",
        "duration": 10,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Slalom conduite — deux pieds",
        "title_nl": "Slalom dribbel — beide voeten",
        "objective_fr": "Contrôle de balle en conduite rapide alternée pied droit/pied gauche.",
        "objective_nl": "Balcontrole in snelle dribbel afwisselend rechts/links.",
        "setup_fr": "8 cônes alignés espacés de 1,5 m. 1 ballon par joueur. File d'attente à 3 m.",
        "setup_nl": "8 kegels op rij, 1,5 m tussenruimte. 1 bal per speler. Wachtrij op 3 m.",
        "instructions_fr": [
            "Passage aller : slalom intérieur du pied droit uniquement.",
            "Retour : intérieur du pied gauche uniquement.",
            "Passage 3 : alterner intérieur droit / intérieur gauche à chaque cône.",
            "Passage 4 : extérieur du pied à chaque cône.",
            "Finir par sortie cône 1 + tir ou passe à cible."
        ],
        "instructions_nl": [
            "Heen: slalom met alleen binnenkant rechts.",
            "Terug: alleen binnenkant links.",
            "Ronde 3: afwisselend binnenkant rechts/links bij elke kegel.",
            "Ronde 4: buitenkant voet bij elke kegel.",
            "Afsluiten met uitgang kegel 1 + schot of pass naar doel."
        ],
        "variants_fr": [
            "Chronométrer les passages, compétition par équipes.",
            "Supprimer regard vers le bas : coach signale un geste à faire à la sortie."
        ],
        "variants_nl": [
            "Rondes chronometreren, teamcompetitie.",
            "Zonder naar beneden kijken: coach geeft signaal bij uitgang."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.96",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "red", "pos": [18, 10], "label": "1"},
                {"type": "ball", "pos": [18, 10]},
                {"type": "cone", "pos": [16, 10]},
                {"type": "cone", "pos": [14.5, 10]},
                {"type": "cone", "pos": [13, 10]},
                {"type": "cone", "pos": [11.5, 10]},
                {"type": "cone", "pos": [10, 10]},
                {"type": "cone", "pos": [8.5, 10]},
                {"type": "cone", "pos": [7, 10]},
                {"type": "cone", "pos": [5.5, 10]},
                {"type": "arrow", "from": [18, 10], "to": [16, 11], "kind": "offense"},
                {"type": "arrow", "from": [16, 11], "to": [14.5, 9], "kind": "offense"},
                {"type": "arrow", "from": [14.5, 9], "to": [13, 11], "kind": "offense"}
            ]
        }
    },
    {
        "id": "te-02",
        "category": "technique",
        "subcategory": "semelle",
        "age_range": "U11-U17",
        "duration": 8,
        "players_min": 4,
        "intensity": "faible",
        "title_fr": "Semelle futsal — fondamentaux",
        "title_nl": "Zoolcontrole — basis",
        "objective_fr": "Maîtrise de la semelle, signature technique du futsal (roll, stop, drag).",
        "objective_nl": "Zoolcontrole beheersen, technisch kenmerk van futsal (roll, stop, drag).",
        "setup_fr": "Zone 10×10 m. 1 ballon par joueur. Tous dans la zone.",
        "setup_nl": "Zone 10×10 m. 1 bal per speler. Iedereen in de zone.",
        "instructions_fr": [
            "Roulement semelle sur place : alterner pied droit / gauche 30 s chacun.",
            "Roulement en mouvement latéral, 20 s chaque côté.",
            "Drag back : semelle + tirer le ballon derrière soi, demi-tour.",
            "V-cut : semelle stoppe ballon, pied fort pousse ballon de l'autre côté.",
            "Mini-défi : coach appelle un geste, exécution immédiate."
        ],
        "instructions_nl": [
            "Roll met zool ter plaatse: afwisselend rechts/links 30 s elk.",
            "Roll in zijwaartse beweging, 20 s per kant.",
            "Drag back: zool + bal achterwaarts trekken, halve draai.",
            "V-cut: zool stopt bal, sterke voet duwt bal naar andere kant.",
            "Mini-uitdaging: coach noemt beweging, directe uitvoering."
        ],
        "variants_fr": [
            "Deux joueurs face à face imitent mutuellement les gestes.",
            "Enchaîner 3 gestes différents sans pause."
        ],
        "variants_nl": [
            "Twee spelers tegenover elkaar imiteren bewegingen.",
            "3 verschillende bewegingen na elkaar zonder pauze."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Technique foundations",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "cone", "pos": [3, 5]},
                {"type": "cone", "pos": [10, 5]},
                {"type": "cone", "pos": [3, 15]},
                {"type": "cone", "pos": [10, 15]},
                {"type": "player", "team": "red", "pos": [5, 8], "label": ""},
                {"type": "ball", "pos": [5, 8]},
                {"type": "player", "team": "red", "pos": [8, 12], "label": ""},
                {"type": "ball", "pos": [8, 12]},
                {"type": "player", "team": "red", "pos": [6, 10], "label": ""},
                {"type": "ball", "pos": [6, 10]},
                {"type": "player", "team": "red", "pos": [9, 8], "label": ""},
                {"type": "ball", "pos": [9, 8]}
            ]
        }
    },
    {
        "id": "te-03",
        "category": "technique",
        "subcategory": "passe",
        "age_range": "U11-Senior",
        "duration": 12,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "Étoile à 5 — passes orientées",
        "title_nl": "Ster met 5 — gerichte passes",
        "objective_fr": "Qualité de passe tendue, corps orienté avant réception, tête relevée.",
        "objective_nl": "Kwalitatieve strakke pass, lichaam gericht voor ontvangst, hoofd omhoog.",
        "setup_fr": "5 plots en étoile, chacun espacé de 8 m. 1 joueur par plot, 1 ballon au départ.",
        "setup_nl": "5 kegels in ster, elk 8 m uit elkaar. 1 speler per kegel, 1 bal bij start.",
        "instructions_fr": [
            "Séquence A → C → E → B → D → A (passe + suit sa passe, remplace le suivant).",
            "Contrôle en 2 touches max : contrôle orienté puis passe.",
            "Changer de sens de rotation à mi-séance.",
            "Imposer passe tendue (ras du sol, sans rebond).",
            "Variante : 2 ballons simultanés pour densifier."
        ],
        "instructions_nl": [
            "Reeks A → C → E → B → D → A (pass + volg, vervang volgende).",
            "Max 2 contacten: gerichte controle dan pass.",
            "Wissel rotatie halverwege.",
            "Verplicht strakke pass (grondpass, geen stuit).",
            "Variant: 2 ballen tegelijk voor verdichting."
        ],
        "variants_fr": [
            "Imposer passe en une touche.",
            "Ajouter un défenseur passif au centre."
        ],
        "variants_nl": [
            "Verplicht 1-touch pass.",
            "Voeg passieve verdediger toe in het midden."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.102",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "red", "pos": [10, 10], "label": "A"},
                {"type": "player", "team": "red", "pos": [15, 15], "label": "B"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "C"},
                {"type": "player", "team": "red", "pos": [15, 5], "label": "D"},
                {"type": "player", "team": "red", "pos": [7, 7], "label": "E"},
                {"type": "ball", "pos": [10, 10]},
                {"type": "arrow", "from": [10, 10], "to": [18, 10], "kind": "ball"},
                {"type": "arrow", "from": [18, 10], "to": [7, 7], "kind": "ball"},
                {"type": "arrow", "from": [7, 7], "to": [15, 15], "kind": "ball"},
                {"type": "arrow", "from": [15, 15], "to": [15, 5], "kind": "ball"}
            ]
        }
    }
]

TECHNIQUE.extend([
    {
        "id": "te-04",
        "category": "technique",
        "subcategory": "contrôle",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Contrôle orienté + remise",
        "title_nl": "Gerichte controle + terugkaatsen",
        "objective_fr": "Contrôle du premier appui qui oriente le jeu dans la direction voulue.",
        "objective_nl": "Eerste balcontact dat spel in gewenste richting oriënteert.",
        "setup_fr": "Paires face à face à 8 m. Cône latéral à 2 m de chaque joueur.",
        "setup_nl": "Paren tegenover elkaar op 8 m. Zijkegel op 2 m van elke speler.",
        "instructions_fr": [
            "A envoie passe à B. B contrôle orienté vers le cône gauche.",
            "B donne la passe à A depuis ce côté.",
            "A contrôle orienté vers son cône droit, retour à B.",
            "Alterner côtés toutes les 6 passes.",
            "Finir : contrôle + passe en 1 touche (pas de contrôle)."
        ],
        "instructions_nl": [
            "A speelt pass naar B. B controleert gericht naar linker kegel.",
            "B past vanaf daar terug naar A.",
            "A controleert gericht naar rechter kegel, terug naar B.",
            "Wissel van kant elke 6 passes.",
            "Afsluiten: pass + 1-touch (zonder controle)."
        ],
        "variants_fr": [
            "Coach dicte le côté (gauche/droite) à chaque passe.",
            "Ajouter 1 feinte après contrôle."
        ],
        "variants_nl": [
            "Coach dicteert kant (links/rechts) elke pass.",
            "Voeg 1 schijnbeweging toe na controle."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.110",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [3, 10], "label": "A"},
                {"type": "player", "team": "red", "pos": [11, 10], "label": "B"},
                {"type": "cone", "pos": [3, 13]},
                {"type": "cone", "pos": [3, 7]},
                {"type": "cone", "pos": [11, 13]},
                {"type": "cone", "pos": [11, 7]},
                {"type": "ball", "pos": [3, 10]},
                {"type": "arrow", "from": [3, 10], "to": [11, 10], "kind": "ball"},
                {"type": "arrow", "from": [11, 10], "to": [11, 13], "kind": "offense"}
            ]
        }
    },
    {
        "id": "te-05",
        "category": "technique",
        "subcategory": "passe longue",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Passe courte-courte-longue",
        "title_nl": "Kort-kort-lang",
        "objective_fr": "Changer de rythme dans la circulation : 2 passes courtes puis rupture longue.",
        "objective_nl": "Ritmewissel in bal circulatie: 2 korte passes dan lange breekpass.",
        "setup_fr": "6 joueurs en 2 lignes de 3 (15 m écart). Ballon démarre ligne A.",
        "setup_nl": "6 spelers in 2 rijen van 3 (15 m tussen rijen). Bal start in rij A.",
        "instructions_fr": [
            "A1 passe courte à A2 (2 m).",
            "A2 remise courte à A3 (2 m).",
            "A3 passe longue à B1 (ligne opposée).",
            "Ligne B enchaîne le même schéma en sens retour.",
            "Toutes les 90 s, rotation des joueurs dans les lignes."
        ],
        "instructions_nl": [
            "A1 korte pass naar A2 (2 m).",
            "A2 korte terugspeler A3 (2 m).",
            "A3 lange pass naar B1 (andere rij).",
            "Rij B zelfde patroon in omgekeerde richting.",
            "Elke 90 s rotatie van spelers in rijen."
        ],
        "variants_fr": [
            "Passe longue obligatoirement en cloche (balle aérienne).",
            "Ajouter un défenseur qui presse la ligne en possession."
        ],
        "variants_nl": [
            "Lange pass verplicht in boog (luchtbal).",
            "Voeg verdediger toe die rij in balbezit onder druk zet."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.118",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "red", "pos": [3, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [6, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [9, 14], "label": "A3"},
                {"type": "player", "team": "red", "pos": [3, 6], "label": "B1"},
                {"type": "player", "team": "red", "pos": [6, 6], "label": "B2"},
                {"type": "player", "team": "red", "pos": [9, 6], "label": "B3"},
                {"type": "ball", "pos": [3, 14]},
                {"type": "arrow", "from": [3, 14], "to": [6, 14], "kind": "ball"},
                {"type": "arrow", "from": [6, 14], "to": [9, 14], "kind": "ball"},
                {"type": "arrow", "from": [9, 14], "to": [3, 6], "kind": "ball"}
            ]
        }
    },
    {
        "id": "te-06",
        "category": "technique",
        "subcategory": "feinte",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Répertoire feintes — 4 gestes",
        "title_nl": "Schijnbewegingen — 4 moves",
        "objective_fr": "Acquisition et répétition de 4 feintes de base adaptées au futsal.",
        "objective_nl": "Verwerven en herhalen van 4 futsal-basis-schijnbewegingen.",
        "setup_fr": "Cône central, attaquant à 4 m avec ballon, défenseur passif à 2 m derrière le cône.",
        "setup_nl": "Middencone, aanvaller met bal op 4 m, passieve verdediger op 2 m achter cone.",
        "instructions_fr": [
            "Geste 1 — Step-over : simuler passe, retirer pied et prendre l'extérieur.",
            "Geste 2 — V-cut : semelle stoppe, pied opposé pousse ballon.",
            "Geste 3 — Roulette de Zidane : 360° protégé par le corps.",
            "Geste 4 — Élastico : extérieur pied puis intérieur rapide.",
            "6 répétitions par geste, alterner pieds."
        ],
        "instructions_nl": [
            "Move 1 — Overstap: pass faken, voet terugtrekken en buitenom.",
            "Move 2 — V-cut: zool stopt bal, andere voet duwt bal.",
            "Move 3 — Zidane-roulette: 360° met lichaam beschermd.",
            "Move 4 — Elastico: buitenkant voet dan snel binnenkant.",
            "6 herhalingen per move, afwisselend voeten."
        ],
        "variants_fr": [
            "Défenseur actif 50 % dès maîtrise.",
            "Enchaîner 2 feintes par passage."
        ],
        "variants_nl": [
            "Actieve verdediger 50 % na beheersing.",
            "2 schijnbewegingen per passage."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.5 Skills",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [3, 10], "label": "A"},
                {"type": "ball", "pos": [3, 10]},
                {"type": "cone", "pos": [7, 10]},
                {"type": "player", "team": "blue", "pos": [9, 10], "label": "D"},
                {"type": "arrow", "from": [3, 10], "to": [6, 11], "kind": "offense"},
                {"type": "arrow", "from": [6, 11], "to": [9, 8], "kind": "offense"}
            ]
        }
    }
])

TECHNIQUE.extend([
    {
        "id": "te-07",
        "category": "technique",
        "subcategory": "prise de balle",
        "age_range": "U11-U17",
        "duration": 8,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Prise de balle dos au but",
        "title_nl": "Balaanname met rug naar doel",
        "objective_fr": "Contrôle dos au jeu, protection et ouverture avec demi-tour.",
        "objective_nl": "Controle met rug naar spel, afschermen en openen met halve draai.",
        "setup_fr": "Joueur A servant à 6 m, joueur B dos au servant à 4 m.",
        "setup_nl": "Speler A bedient op 6 m, speler B met rug naar bediener op 4 m.",
        "instructions_fr": [
            "A envoie passe au sol à B, dos au jeu.",
            "B contrôle semelle, protège le ballon.",
            "B exécute demi-tour rapide et repasse à A en 2 touches.",
            "Alterner demi-tour pied droit / pied gauche.",
            "Rotation A/B toutes les 6 passes."
        ],
        "instructions_nl": [
            "A speelt grondpass naar B met rug naar spel.",
            "B controleert met zool, schermt bal af.",
            "B maakt snelle halve draai en past in 2 contacten terug naar A.",
            "Halve draai afwisselend rechts/links.",
            "Rotatie A/B elke 6 passes."
        ],
        "variants_fr": [
            "A appuie passivement sur B pour simuler pression.",
            "Au signal coach, B se retourne sans contrôle (1 touche)."
        ],
        "variants_nl": [
            "A duwt passief tegen B om druk te simuleren.",
            "Op signaal: B draait zonder controle (1-touch)."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.122",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [3, 10], "label": "A"},
                {"type": "ball", "pos": [3, 10]},
                {"type": "player", "team": "red", "pos": [9, 10], "label": "B"},
                {"type": "arrow", "from": [3, 10], "to": [9, 10], "kind": "ball"},
                {"type": "arrow", "from": [9, 10], "to": [9.5, 10.5], "kind": "offense"}
            ]
        }
    },
    {
        "id": "te-08",
        "category": "technique",
        "subcategory": "frappe",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Frappe du cou de pied puts",
        "title_nl": "Wreeftrap uit spelsituatie",
        "objective_fr": "Précision de frappe après mouvement, choix du type de tir selon angle.",
        "objective_nl": "Nauwkeurig schieten na beweging, keuze schottype afhankelijk van hoek.",
        "setup_fr": "Gardien en place. 3 zones de tir (axe, droite, gauche) à 8 m du but. Ballons à proximité.",
        "setup_nl": "Keeper staat. 3 schotzones (as, rechts, links) op 8 m van doel. Ballen binnen handbereik.",
        "instructions_fr": [
            "Tour 1 — axe : conduite 3 m + frappe placée.",
            "Tour 2 — droite : conduite latérale + frappe pied fort.",
            "Tour 3 — gauche : conduite latérale + frappe pied fort (angle fermé).",
            "Tour 4 — feinte passe au coach puis tir.",
            "Tour 5 — choix libre : coach crie un côté, tir opposé."
        ],
        "instructions_nl": [
            "Ronde 1 — as: dribbel 3 m + geplaatst schot.",
            "Ronde 2 — rechts: zijdribbel + schot sterke voet.",
            "Ronde 3 — links: zijdribbel + schot sterke voet (gesloten hoek).",
            "Ronde 4 — schijnpass coach dan schot.",
            "Ronde 5 — vrije keuze: coach roept kant, schot aan andere kant."
        ],
        "variants_fr": [
            "Chronométrer + % de réussite affiché.",
            "Défenseur passif qui sort sur la frappe."
        ],
        "variants_nl": [
            "Chronometreren + % rake schoten tonen.",
            "Passieve verdediger komt uit op schot."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.5",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [12, 14], "label": "L"},
                {"type": "player", "team": "red", "pos": [12, 10], "label": "A"},
                {"type": "player", "team": "red", "pos": [12, 6], "label": "R"},
                {"type": "ball", "pos": [12, 14]},
                {"type": "ball", "pos": [12, 10]},
                {"type": "ball", "pos": [12, 6]},
                {"type": "arrow", "from": [12, 14], "to": [0.5, 10], "kind": "ball"},
                {"type": "arrow", "from": [12, 10], "to": [0.5, 10], "kind": "ball"},
                {"type": "arrow", "from": [12, 6], "to": [0.5, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "te-09",
        "category": "technique",
        "subcategory": "head-up",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Conduite tête haute — commandes",
        "title_nl": "Dribbel hoofd omhoog — commando's",
        "objective_fr": "Forcer la prise d'information périphérique pendant la conduite.",
        "objective_nl": "Periferisch zicht afdwingen tijdens dribbel.",
        "setup_fr": "Zone 15×15 m. 6 joueurs avec ballon. Coach au centre avec panneaux de couleur ou chiffres.",
        "setup_nl": "Zone 15×15 m. 6 spelers met bal. Coach in midden met kleurenbordjes of cijfers.",
        "instructions_fr": [
            "Conduite libre, obligation de garder un œil sur le coach.",
            "Coach lève un panneau : tous les joueurs crient la couleur/chiffre.",
            "Coach lève 2 panneaux : joueurs exécutent 2 gestes techniques.",
            "Coach pointe un joueur : passe au joueur désigné.",
            "3 blocs de 2 min, 30 s pause."
        ],
        "instructions_nl": [
            "Vrij dribbelen, één oog op coach houden.",
            "Coach heft bordje: iedereen roept kleur/cijfer.",
            "Coach heft 2 bordjes: 2 technische bewegingen uitvoeren.",
            "Coach wijst speler aan: pass naar die speler.",
            "3 blokken van 2 min, 30 s pauze."
        ],
        "variants_fr": [
            "Coach bouge dans la zone, joueurs doivent toujours le voir.",
            "Ajouter règle : pas de ballon proche de la tête → perte."
        ],
        "variants_nl": [
            "Coach beweegt in zone, moet altijd zichtbaar blijven.",
            "Regel: bal bij de voet houden, niet hoger dan knie."
        ],
        "source": "RFEF Escuela — Técnica individual U14-U16",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "cone", "pos": [2, 5]},
                {"type": "cone", "pos": [12, 5]},
                {"type": "cone", "pos": [2, 15]},
                {"type": "cone", "pos": [12, 15]},
                {"type": "player", "team": "yellow", "pos": [7, 10], "label": "C"},
                {"type": "player", "team": "red", "pos": [4, 8], "label": ""},
                {"type": "ball", "pos": [4, 8]},
                {"type": "player", "team": "red", "pos": [10, 12], "label": ""},
                {"type": "ball", "pos": [10, 12]},
                {"type": "player", "team": "red", "pos": [8, 6], "label": ""},
                {"type": "ball", "pos": [8, 6]},
                {"type": "player", "team": "red", "pos": [5, 13], "label": ""},
                {"type": "ball", "pos": [5, 13]}
            ]
        }
    }
])

TECHNIQUE.extend([
    {
        "id": "te-10",
        "category": "technique",
        "subcategory": "passe diagonale",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Passe diagonale + croisement",
        "title_nl": "Diagonale pass + kruising",
        "objective_fr": "Changer de couloir par passe longue diagonale, gérer la course croisée.",
        "objective_nl": "Vleugel wisselen via diagonale pass, kruislopen beheersen.",
        "setup_fr": "2 couloirs parallèles sur 20 m. 3 joueurs par couloir. 1 ballon.",
        "setup_nl": "2 parallelle corridors over 20 m. 3 spelers per corridor. 1 bal.",
        "instructions_fr": [
            "A1 (couloir gauche) envoie passe diagonale à B1 (couloir droit).",
            "A1 court dans le couloir droit pour remplacer B1.",
            "B1 contrôle, avance 5 m, passe diagonale à A2 (gauche).",
            "Même principe, croisement continu.",
            "Finir avec remise en 1 touche avant passe diagonale."
        ],
        "instructions_nl": [
            "A1 (links) speelt diagonale pass naar B1 (rechts).",
            "A1 loopt rechts om B1 te vervangen.",
            "B1 controleert, loopt 5 m vooruit, diagonale pass naar A2 (links).",
            "Zelfde principe, doorlopende kruising.",
            "Afsluiten met 1-touch terugspelen voor diagonale pass."
        ],
        "variants_fr": [
            "Imposer passe tendue au sol.",
            "Limiter à 1 touche max."
        ],
        "variants_nl": [
            "Verplicht strakke grondpass.",
            "Beperk tot 1-touch."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Flow patterns",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "player", "team": "red", "pos": [8, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [14, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [20, 14], "label": "A3"},
                {"type": "player", "team": "red", "pos": [8, 6], "label": "B1"},
                {"type": "player", "team": "red", "pos": [14, 6], "label": "B2"},
                {"type": "player", "team": "red", "pos": [20, 6], "label": "B3"},
                {"type": "ball", "pos": [8, 14]},
                {"type": "arrow", "from": [8, 14], "to": [14, 6], "kind": "ball"},
                {"type": "arrow", "from": [8, 14], "to": [8, 6], "kind": "offense"}
            ]
        }
    },
    {
        "id": "te-11",
        "category": "technique",
        "subcategory": "amorti",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "faible",
        "title_fr": "Amorti aérien + passe",
        "title_nl": "Luchtbal breken + pass",
        "objective_fr": "Contrôle de la balle aérienne : cuisse, poitrine, semelle.",
        "objective_nl": "Luchtbal onder controle brengen: dij, borst, zool.",
        "setup_fr": "Paires à 5 m. Le serveur lance à la main, le receveur contrôle.",
        "setup_nl": "Paren op 5 m. Bediener gooit met de hand, ontvanger controleert.",
        "instructions_fr": [
            "Contrôle de la cuisse (5 fois chaque jambe).",
            "Contrôle de la poitrine (5 fois).",
            "Contrôle semelle sur ballon demi-volée (5 fois chaque pied).",
            "Variante : amorti + passe en 1 touche retour.",
            "Finir par 1 amorti + contrôle orienté + passe."
        ],
        "instructions_nl": [
            "Dijcontrole (5 x elk been).",
            "Borstcontrole (5 x).",
            "Zoolcontrole op halfvolley (5 x elke voet).",
            "Variant: controle + 1-touch terug.",
            "Afsluiten met controle + gerichte controle + pass."
        ],
        "variants_fr": [
            "Ballon à différentes hauteurs : cuisse, poitrine, tête.",
            "Servir en coup de pied aérien à 10 m."
        ],
        "variants_nl": [
            "Bal op verschillende hoogtes: dij, borst, hoofd.",
            "Bedien met getrapte luchtbal op 10 m."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.128",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [4, 10], "label": "A"},
                {"type": "player", "team": "red", "pos": [9, 10], "label": "B"},
                {"type": "ball", "pos": [4, 10]},
                {"type": "arrow", "from": [4, 10], "to": [9, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "te-12",
        "category": "technique",
        "subcategory": "rapidité",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Conduite vitesse + finition",
        "title_nl": "Dribbel op snelheid + afwerking",
        "objective_fr": "Maîtriser la conduite à pleine vitesse sans perdre le contrôle avant finition.",
        "objective_nl": "Dribbel op volle snelheid beheersen zonder controleverlies vóór afwerking.",
        "setup_fr": "Gardien en place. Cône de départ à 18 m, zone de tir à 6 m. 2 files.",
        "setup_nl": "Keeper staat. Startkegel op 18 m, schotzone op 6 m. 2 rijen.",
        "instructions_fr": [
            "Joueur part en conduite pleine vitesse du cône de départ.",
            "Dernier appui à 6 m : frappe précise dans le coin opposé.",
            "Varier pied fort / pied faible selon le côté de la file.",
            "Après 3 passages, ajouter défenseur passif à 10 m du but.",
            "Finir : 3 essais chronométrés, meilleur temps."
        ],
        "instructions_nl": [
            "Speler vertrekt met volle snelheid vanaf startkegel.",
            "Laatste steun op 6 m: geplaatst schot in tegenoverliggende hoek.",
            "Afwisselen sterke/zwakke voet volgens kant van de rij.",
            "Na 3 passages: passieve verdediger op 10 m van doel.",
            "Afsluiten: 3 gechronometreerde pogingen, beste tijd."
        ],
        "variants_fr": [
            "Ajouter 2 cônes à zigzaguer avant le tir.",
            "Défenseur actif après cônes."
        ],
        "variants_nl": [
            "Voeg 2 slalomkegels toe voor het schot.",
            "Actieve verdediger na kegels."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Finishing drills",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "cone", "pos": [18, 10]},
                {"type": "player", "team": "red", "pos": [19, 10], "label": "A"},
                {"type": "ball", "pos": [19, 10]},
                {"type": "arrow", "from": [19, 10], "to": [6, 10], "kind": "offense"},
                {"type": "arrow", "from": [6, 10], "to": [0.5, 12.5], "kind": "ball"}
            ]
        }
    },
    {
        "id": "te-13",
        "category": "technique",
        "subcategory": "tête et volée",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Volée + tête (reprise aérienne)",
        "title_nl": "Volley + kopstoot (luchtspel)",
        "objective_fr": "Timing du saut ou de la reprise volée sur centre bas ou aérien.",
        "objective_nl": "Timing van sprong of volley op laag of hoog voorzet.",
        "setup_fr": "Centreur sur aile, attaquant à 8 m du but. Gardien en place.",
        "setup_nl": "Voorzetter op vleugel, aanvaller op 8 m van doel. Keeper staat.",
        "instructions_fr": [
            "Centre mi-hauteur : reprise de volée pied fort.",
            "Centre aérien : tête plongeante ou piquée.",
            "Centre au sol : reprise 1 touche intérieur.",
            "Alterner entrée côté gauche / droit.",
            "10 répétitions par type, changer les rôles."
        ],
        "instructions_nl": [
            "Halfhoge voorzet: volley met sterke voet.",
            "Luchtvoorzet: duikkop of gerichte kopstoot.",
            "Grondpass: 1-touch met binnenkant.",
            "Afwisselen links/rechts inkomen.",
            "10 herhalingen per type, rollen wisselen."
        ],
        "variants_fr": [
            "Défenseur qui suit l'attaquant en marquage.",
            "Centre après dribble + feinte."
        ],
        "variants_nl": [
            "Verdediger volgt aanvaller in dekking.",
            "Voorzet na dribbel + schijnbeweging."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.136",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [8, 16], "label": "C"},
                {"type": "player", "team": "red", "pos": [6, 10], "label": "A"},
                {"type": "ball", "pos": [8, 16]},
                {"type": "arrow", "from": [8, 16], "to": [6, 10], "kind": "ball"},
                {"type": "arrow", "from": [6, 10], "to": [0.5, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "te-14",
        "category": "technique",
        "subcategory": "1c1 technique",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 4,
        "intensity": "élevée",
        "title_fr": "1v1 carré technique",
        "title_nl": "1v1 technisch vierkant",
        "objective_fr": "Gagner 1v1 dans zone restreinte, répertoire de feintes, protection de balle.",
        "objective_nl": "1v1 winnen in beperkte zone, schijnbewegingen, afschermen bal.",
        "setup_fr": "Carré 8×8 m. Porteur attaque, défenseur défend. Joueur marque en franchissant la ligne opposée.",
        "setup_nl": "Vierkant 8×8 m. Balbezitter valt aan, verdediger verdedigt. Punt bij lijn overkant doorkruisen.",
        "instructions_fr": [
            "1v1 en 20 s max. But : franchir ligne opposée avec ballon sous contrôle.",
            "Alterner rôles après chaque duel.",
            "Imposer 1 feinte minimum par attaque.",
            "Ajouter règle : 2 duels, changement de partenaire.",
            "Compter les réussites par joueur."
        ],
        "instructions_nl": [
            "1v1 in max 20 s. Doel: lijn overkant doorkruisen met bal.",
            "Rolwissel na elk duel.",
            "Verplicht min 1 schijnbeweging per aanval.",
            "Regel: 2 duels, dan partner wisselen.",
            "Succeskansen per speler tellen."
        ],
        "variants_fr": [
            "Ajouter zone but 1 m devant la ligne pour récompenser tir.",
            "Terminer duel par passe à un appui extérieur."
        ],
        "variants_nl": [
            "Doelzone 1 m voor lijn om schot te belonen.",
            "Duel afsluiten met pass naar externe steunspeler."
        ],
        "source": "RFEF Escuela — Duels individuels",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "cone", "pos": [3, 6]},
                {"type": "cone", "pos": [11, 6]},
                {"type": "cone", "pos": [3, 14]},
                {"type": "cone", "pos": [11, 14]},
                {"type": "player", "team": "red", "pos": [5, 10], "label": "A"},
                {"type": "ball", "pos": [5, 10]},
                {"type": "player", "team": "blue", "pos": [9, 10], "label": "D"},
                {"type": "arrow", "from": [5, 10], "to": [11, 12], "kind": "offense"}
            ]
        }
    },
    {
        "id": "te-15",
        "category": "technique",
        "subcategory": "passe à travers",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Passe dans le dos (fente)",
        "title_nl": "Pass in de rug (gap)",
        "objective_fr": "Exécution et timing de la passe entre deux défenseurs + appel dans l'espace.",
        "objective_nl": "Uitvoering en timing van pass tussen 2 verdedigers + inlopen in ruimte.",
        "setup_fr": "2 cônes espacés de 3 m (fente). Porteur à 6 m en amont, receveur en appel à 5 m en aval.",
        "setup_nl": "2 kegels 3 m uit elkaar (gap). Balbezitter 6 m ervoor, ontvanger 5 m erna in inloop.",
        "instructions_fr": [
            "Porteur contrôle et passe entre les 2 cônes.",
            "Receveur lance son appel au moment de la passe (pas avant).",
            "Réception, contrôle en mouvement, tir ou passe retour.",
            "Rotation : receveur devient porteur.",
            "Ajouter 2 défenseurs passifs positionnés aux cônes."
        ],
        "instructions_nl": [
            "Balbezitter controleert en speelt pass tussen de 2 kegels.",
            "Ontvanger loopt pas in op moment van pass (niet eerder).",
            "Ontvangst in beweging, schot of terugpass.",
            "Rotatie: ontvanger wordt balbezitter.",
            "Voeg 2 passieve verdedigers toe bij kegels."
        ],
        "variants_fr": [
            "Défenseurs actifs qui serrent la fente.",
            "Multi-fentes : 3 passages consécutifs à enchaîner."
        ],
        "variants_nl": [
            "Actieve verdedigers die gap sluiten.",
            "Multi-gaps: 3 opeenvolgende pogingen."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Penetration passing",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "red", "pos": [16, 10], "label": "A"},
                {"type": "ball", "pos": [16, 10]},
                {"type": "cone", "pos": [10, 8.5]},
                {"type": "cone", "pos": [10, 11.5]},
                {"type": "player", "team": "red", "pos": [5, 10], "label": "B"},
                {"type": "arrow", "from": [16, 10], "to": [5, 10], "kind": "ball"},
                {"type": "arrow", "from": [5, 10], "to": [3, 10], "kind": "offense"}
            ]
        }
    }
])
