"""Finition (8) — ateliers de finition."""

FINITION = [
    {
        "id": "fi-01",
        "category": "finition",
        "subcategory": "classique",
        "age_range": "U11-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Atelier finition — cercle",
        "title_nl": "Afwerking — cirkel",
        "objective_fr": "Répéter 3 types de finition en enchaînement rapide.",
        "objective_nl": "3 afwerktypes in snelle opvolging herhalen.",
        "setup_fr": "Gardien en place. 6 plots en demi-cercle à 8 m. Ballons à disposition.",
        "setup_nl": "Keeper staat. 6 kegels in halve cirkel op 8 m. Ballen beschikbaar.",
        "instructions_fr": [
            "Poste 1-2 : conduite + tir placé pied fort.",
            "Poste 3-4 : passe coach + remise + tir.",
            "Poste 5-6 : 1v1 avec défenseur passif + finition.",
            "Enchaîner les 6 postes sans pause.",
            "3 tours, 1 min pause entre tours."
        ],
        "instructions_nl": [
            "Post 1-2: dribbel + geplaatst schot sterke voet.",
            "Post 3-4: pass coach + terugleggen + schot.",
            "Post 5-6: 1v1 met passieve verdediger + afwerking.",
            "6 posten zonder pauze.",
            "3 rondes, 1 min pauze tussen rondes."
        ],
        "variants_fr": [
            "Chronométrer les 6 postes par joueur.",
            "Alterner pied fort/faible par poste."
        ],
        "variants_nl": [
            "6 posten chronometreren per speler.",
            "Afwisselen sterke/zwakke voet per post."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Finishing circuit",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "cone", "pos": [8, 17]},
                {"type": "cone", "pos": [10, 15]},
                {"type": "cone", "pos": [11, 10]},
                {"type": "cone", "pos": [10, 5]},
                {"type": "cone", "pos": [8, 3]},
                {"type": "cone", "pos": [6, 1]},
                {"type": "player", "team": "red", "pos": [12, 17], "label": "1"},
                {"type": "ball", "pos": [12, 17]},
                {"type": "arrow", "from": [12, 17], "to": [8, 17], "kind": "offense"},
                {"type": "arrow", "from": [8, 17], "to": [0.5, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "fi-02",
        "category": "finition",
        "subcategory": "appui",
        "age_range": "U11-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Appui-remise + tir",
        "title_nl": "Aangespeeld-terugleggen + schot",
        "objective_fr": "Jouer en une-deux avec appui pivot avant finition.",
        "objective_nl": "Een-twee spelen met pivot-steun voor afwerking.",
        "setup_fr": "Gardien. Appui (pivot) à 6 m du but. Attaquant à 18 m.",
        "setup_nl": "Keeper. Steun (pivot) op 6 m van doel. Aanvaller op 18 m.",
        "instructions_fr": [
            "Attaquant conduit 3 m, passe au pivot.",
            "Pivot remise en 1 touche décalée (gauche/droite).",
            "Attaquant tire en 1 touche.",
            "Alterner pivot droit/gauche selon file.",
            "10 répétitions par joueur."
        ],
        "instructions_nl": [
            "Aanvaller dribbelt 3 m, speelt naar pivot.",
            "Pivot 1-touch terugleggen (links/rechts).",
            "Aanvaller 1-touch afwerken.",
            "Pivot afwisselend links/rechts.",
            "10 herhalingen per speler."
        ],
        "variants_fr": [
            "Ajouter défenseur passif entre pivot et but.",
            "Imposer 1 feinte avant passe au pivot."
        ],
        "variants_nl": [
            "Passieve verdediger tussen pivot en doel.",
            "1 schijnbeweging voor pass."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Finishing",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [6, 10], "label": "Pv"},
                {"type": "player", "team": "red", "pos": [17, 10], "label": "A"},
                {"type": "ball", "pos": [17, 10]},
                {"type": "arrow", "from": [17, 10], "to": [14, 10], "kind": "offense"},
                {"type": "arrow", "from": [14, 10], "to": [6, 10], "kind": "ball"},
                {"type": "arrow", "from": [6, 10], "to": [11, 13], "kind": "ball"},
                {"type": "arrow", "from": [11, 13], "to": [0.5, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "fi-03",
        "category": "finition",
        "subcategory": "centre-tir",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Centre + reprise 2e poteau",
        "title_nl": "Voorzet + afronding 2e paal",
        "objective_fr": "Timing de l'appel 2e poteau, précision de la reprise.",
        "objective_nl": "Timing inloop 2e paal, nauwkeurig afronden.",
        "setup_fr": "Centreur à l'aile, attaquant en zone. Gardien en place.",
        "setup_nl": "Voorzetter op vleugel, aanvaller in zone. Keeper staat.",
        "instructions_fr": [
            "Centreur conduit le long de l'aile et centre bas.",
            "Attaquant se démarque du 1er appui, court au 2e poteau.",
            "Reprise en 1 touche pied droit/gauche selon côté.",
            "Ajouter 2e attaquant sur 1er poteau (détournement).",
            "10 répétitions par côté."
        ],
        "instructions_nl": [
            "Voorzetter dribbelt langs vleugel en legt laag voor.",
            "Aanvaller lost van 1e paal los, loopt naar 2e paal.",
            "1-touch afronding rechts/links afhankelijk kant.",
            "2e aanvaller op 1e paal (afleiding).",
            "10 herhalingen per kant."
        ],
        "variants_fr": [
            "Centre aérien → tête.",
            "Centre arrière → tir pour joueur en soutien."
        ],
        "variants_nl": [
            "Luchtvoorzet → kopbal.",
            "Achterwaartse voorzet → schot voor steunspeler."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.222",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [10, 17], "label": "C"},
                {"type": "ball", "pos": [10, 17]},
                {"type": "player", "team": "red", "pos": [12, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [9, 5], "label": "A2"},
                {"type": "arrow", "from": [10, 17], "to": [5, 12], "kind": "ball"},
                {"type": "arrow", "from": [12, 10], "to": [5, 12], "kind": "offense"},
                {"type": "arrow", "from": [5, 12], "to": [0.5, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "fi-04",
        "category": "finition",
        "subcategory": "contre-attaque",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Contre-attaque 3v1",
        "title_nl": "Counter 3v1",
        "objective_fr": "Finir en 6 s après récupération, prise de décision rapide.",
        "objective_nl": "Afwerken binnen 6 s na recuperatie, snelle besluitvorming.",
        "setup_fr": "Terrain complet. 3 attaquants partent au milieu, 1 défenseur + GK en défense.",
        "setup_nl": "Volledig veld. 3 aanvallers starten in midden, 1 verdediger + GK in verdediging.",
        "instructions_fr": [
            "Coach siffle, 3 attaquants démarrent ballon au pied.",
            "Défenseur part du but, suit la course.",
            "Objectif : marquer en <6 s, max 4 passes.",
            "Répétition directe : défenseur devient attaquant.",
            "3 rotations par équipe."
        ],
        "instructions_nl": [
            "Coach fluit, 3 aanvallers starten met bal.",
            "Verdediger start vanaf doel, volgt.",
            "Doel: scoren binnen 6 s, max 4 passes.",
            "Directe herhaling: verdediger wordt aanvaller.",
            "3 rotaties per team."
        ],
        "variants_fr": [
            "Ajouter 2e défenseur à 10 s.",
            "Imposer tir avant entrée zone."
        ],
        "variants_nl": [
            "2e verdediger na 10 s.",
            "Schot verplicht voor zone-ingang."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Counter",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [20, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [20, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [20, 6], "label": "A3"},
                {"type": "ball", "pos": [20, 10]},
                {"type": "player", "team": "blue", "pos": [5, 10], "label": "D1"},
                {"type": "arrow", "from": [20, 10], "to": [4, 10], "kind": "offense"},
                {"type": "arrow", "from": [20, 14], "to": [4, 14], "kind": "offense"},
                {"type": "arrow", "from": [20, 6], "to": [4, 6], "kind": "offense"}
            ]
        }
    },
    {
        "id": "fi-05",
        "category": "finition",
        "subcategory": "premier poteau",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Tir premier poteau",
        "title_nl": "Eerste paal schot",
        "objective_fr": "Placer la frappe au premier poteau depuis angle fermé.",
        "objective_nl": "Plaatsen van schot op eerste paal vanuit gesloten hoek.",
        "setup_fr": "Gardien en place. Plots à 7 m, côté aile. Ballons prêts.",
        "setup_nl": "Keeper staat. Kegels op 7 m, vleugelkant. Ballen klaar.",
        "instructions_fr": [
            "Joueur part conduire vers le plot côté aile.",
            "Arrivé au plot, déclenche frappe rasante 1er poteau.",
            "Pied fort depuis extérieur = pied droit côté droit, pied gauche côté gauche.",
            "Gardien doit lire la course.",
            "10 tentatives par côté, alterner."
        ],
        "instructions_nl": [
            "Speler dribbelt naar kegel aan vleugelkant.",
            "Bij kegel: schot op eerste paal laag.",
            "Sterke voet vanaf buitenkant: rechts rechts, links links.",
            "Keeper moet loop lezen.",
            "10 pogingen per kant, afwisselen."
        ],
        "variants_fr": [
            "Défenseur passif entre attaquant et but.",
            "Chronométrer : 2 s max entre plot et tir."
        ],
        "variants_nl": [
            "Passieve verdediger tussen aanvaller en doel.",
            "Chronometreren: max 2 s tussen kegel en schot."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Angles",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "cone", "pos": [7, 16]},
                {"type": "cone", "pos": [7, 4]},
                {"type": "player", "team": "red", "pos": [15, 17], "label": "A"},
                {"type": "ball", "pos": [15, 17]},
                {"type": "arrow", "from": [15, 17], "to": [7, 16], "kind": "offense"},
                {"type": "arrow", "from": [7, 16], "to": [0.5, 11.5], "kind": "ball"}
            ]
        }
    },
    {
        "id": "fi-06",
        "category": "finition",
        "subcategory": "combinée",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 8,
        "intensity": "élevée",
        "title_fr": "Combinaison 3 joueurs",
        "title_nl": "Combinatie met 3 spelers",
        "objective_fr": "Enchaînement passe, remise, tir, exécution précise à 3.",
        "objective_nl": "Pass, terugleggen, schot opvolgen, precieze uitvoering met 3.",
        "setup_fr": "Gardien. 3 zones : appui 1 (gauche), appui 2 (droit), tireur central.",
        "setup_nl": "Keeper. 3 zones: steun 1 (links), steun 2 (rechts), schutter centraal.",
        "instructions_fr": [
            "Central (A) passe à appui gauche (B).",
            "B remise 1 touche à appui droit (C).",
            "C remise décalée à A.",
            "A frappe en 1 touche.",
            "Permuter les 3 rôles toutes les 3 répétitions."
        ],
        "instructions_nl": [
            "Centraal (A) speelt naar links (B).",
            "B 1-touch terug naar rechts (C).",
            "C versneld terug naar A.",
            "A 1-touch afronden.",
            "Rolwissel elke 3 herhalingen."
        ],
        "variants_fr": [
            "Ajouter défenseur entre A et but.",
            "Imposer passe en 1 touche à tous."
        ],
        "variants_nl": [
            "Voeg verdediger toe tussen A en doel.",
            "1-touch verplicht voor iedereen."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.228",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [10, 15], "label": "B"},
                {"type": "player", "team": "red", "pos": [10, 5], "label": "C"},
                {"type": "player", "team": "red", "pos": [16, 10], "label": "A"},
                {"type": "ball", "pos": [16, 10]},
                {"type": "arrow", "from": [16, 10], "to": [10, 15], "kind": "ball"},
                {"type": "arrow", "from": [10, 15], "to": [10, 5], "kind": "ball"},
                {"type": "arrow", "from": [10, 5], "to": [14, 10], "kind": "ball"},
                {"type": "arrow", "from": [14, 10], "to": [0.5, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "fi-07",
        "category": "finition",
        "subcategory": "défenseur actif",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Finition 1v1 sous pression",
        "title_nl": "Afwerking 1v1 onder druk",
        "objective_fr": "Tir avec défenseur actif, gérer le stress de finition.",
        "objective_nl": "Schot met actieve verdediger, afwerkstress hanteren.",
        "setup_fr": "Gardien. Attaquant part à 15 m avec ballon, défenseur derrière à 2 m.",
        "setup_nl": "Keeper. Aanvaller start op 15 m met bal, verdediger 2 m erachter.",
        "instructions_fr": [
            "Coach siffle, attaquant part, défenseur poursuit.",
            "Attaquant doit déclencher frappe en moins de 3 s.",
            "Varier surface : pied fort / faible / extérieur.",
            "Rotation attaquant / défenseur / gardien.",
            "8 tentatives par joueur."
        ],
        "instructions_nl": [
            "Coach fluit, aanvaller start, verdediger volgt.",
            "Aanvaller moet schieten binnen 3 s.",
            "Voet wisselen: sterk / zwak / buitenkant.",
            "Rotatie aanvaller / verdediger / keeper.",
            "8 pogingen per speler."
        ],
        "variants_fr": [
            "Chronométrer + % réussite.",
            "Ajouter obligation de feinte."
        ],
        "variants_nl": [
            "Chronometreren + % rake.",
            "Verplichte schijnbeweging."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Pressure finishing",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [14, 10], "label": "A"},
                {"type": "ball", "pos": [14, 10]},
                {"type": "player", "team": "blue", "pos": [16, 10], "label": "D"},
                {"type": "arrow", "from": [14, 10], "to": [5, 10], "kind": "offense"},
                {"type": "arrow", "from": [16, 10], "to": [5, 9], "kind": "defense"}
            ]
        }
    },
    {
        "id": "fi-08",
        "category": "finition",
        "subcategory": "rebond",
        "age_range": "U11-Senior",
        "duration": 8,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Finition sur rebond",
        "title_nl": "Afronden op rebound",
        "objective_fr": "Anticiper le rebond gardien, réagir vite sur ballon en l'air ou rebondi.",
        "objective_nl": "Keeperrebound anticiperen, snel reageren op lucht of stuitbal.",
        "setup_fr": "Gardien. Coach tir depuis 10 m, attaquant se démarque.",
        "setup_nl": "Keeper. Coach schiet vanaf 10 m, aanvaller loopt in.",
        "instructions_fr": [
            "Coach frappe au but (force modérée, gardien stoppe).",
            "Attaquant anticipe le rebond et finit en 1 touche.",
            "Alterner tirs coach : court, aérien, excentré.",
            "Attaquant varie appuis et positions d'attaque.",
            "10 répétitions par joueur."
        ],
        "instructions_nl": [
            "Coach schiet op doel (gemiddelde kracht, keeper stopt).",
            "Aanvaller anticipeert rebound en werkt 1-touch af.",
            "Afwisselen: laag, hoog, buiten-as schot.",
            "Aanvaller varieert steunposten en aanvalspositie.",
            "10 herhalingen per speler."
        ],
        "variants_fr": [
            "Ajouter défenseur qui suit attaquant.",
            "Attaquant doit réagir à rebond d'adversaire (blocage défensif)."
        ],
        "variants_nl": [
            "Voeg verdediger toe die volgt.",
            "Aanvaller reageert op tegenstander-rebound (blok)."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Rebound play",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "yellow", "pos": [11, 10], "label": "C"},
                {"type": "ball", "pos": [11, 10]},
                {"type": "player", "team": "red", "pos": [6, 13], "label": "A"},
                {"type": "arrow", "from": [11, 10], "to": [0.5, 10], "kind": "ball"},
                {"type": "arrow", "from": [0.5, 10], "to": [5, 12], "kind": "ball"},
                {"type": "arrow", "from": [5, 12], "to": [0.5, 11], "kind": "ball"}
            ]
        }
    }
]
