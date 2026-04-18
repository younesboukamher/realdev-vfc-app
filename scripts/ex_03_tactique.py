"""Tactical exercises (15) — rotations, 2v1, 3v2, blocs, pressing."""

TACTIQUE = [
    {
        "id": "ta-01",
        "category": "tactique",
        "subcategory": "rotation",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Rotation en losange (quadrado)",
        "title_nl": "Rotatie in ruit (quadrado)",
        "objective_fr": "Principe de rotation futsal : le porteur conduit, un partenaire décroche, un autre s'élance.",
        "objective_nl": "Futsal-rotatieprincipe: balbezitter dribbelt, één medespeler zakt in, ander start door.",
        "setup_fr": "4 joueurs en losange (12 m de côté). 1 ballon.",
        "setup_nl": "4 spelers in ruit (12 m zijde). 1 bal.",
        "instructions_fr": [
            "Porteur conduit vers un coéquipier.",
            "Coéquipier décroche, donne passe en mouvement.",
            "Il remplace la position du porteur.",
            "Le porteur prend sa nouvelle position et relance.",
            "Toutes les 90 s, changer sens de rotation."
        ],
        "instructions_nl": [
            "Balbezitter dribbelt naar medespeler.",
            "Medespeler zakt in, speelt pass in beweging.",
            "Hij vervangt positie van balbezitter.",
            "Balbezitter neemt nieuwe positie en vervolgt.",
            "Elke 90 s: richting wisselen."
        ],
        "variants_fr": [
            "Ajouter 2 défenseurs passifs au centre.",
            "Imposer 2 touches max."
        ],
        "variants_nl": [
            "2 passieve verdedigers in het midden.",
            "Max 2 contacten."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.148",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "player", "team": "red", "pos": [5, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [11, 15], "label": "2"},
                {"type": "player", "team": "red", "pos": [17, 10], "label": "3"},
                {"type": "player", "team": "red", "pos": [11, 5], "label": "4"},
                {"type": "ball", "pos": [5, 10]},
                {"type": "arrow", "from": [5, 10], "to": [11, 15], "kind": "offense"},
                {"type": "arrow", "from": [11, 15], "to": [5, 10], "kind": "offense"},
                {"type": "arrow", "from": [5, 10], "to": [11, 15], "kind": "ball"}
            ]
        }
    },
    {
        "id": "ta-02",
        "category": "tactique",
        "subcategory": "2c1",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "2v1 + finition",
        "title_nl": "2v1 + afwerking",
        "objective_fr": "Décision 2v1 : fixer le défenseur, passe ou dribble, finition.",
        "objective_nl": "Beslissing 2v1: verdediger fixeren, pass of dribbel, afwerking.",
        "setup_fr": "Gardien en place. 2 attaquants à 20 m du but, 1 défenseur à 12 m. Zone tir à 6 m.",
        "setup_nl": "Keeper staat. 2 aanvallers op 20 m van doel, 1 verdediger op 12 m. Schotzone op 6 m.",
        "instructions_fr": [
            "Porteur attaque, partenaire en appui lointain ou croisé.",
            "Principe : fixer le défenseur 2-3 m avant d'agir.",
            "Si défenseur ferme passe → dribble ou frappe.",
            "Si défenseur ferme conduite → passe puis appel diagonal.",
            "8 répétitions par attaquant, rotation avec le défenseur."
        ],
        "instructions_nl": [
            "Balbezitter valt aan, medespeler diepte of kruising.",
            "Principe: verdediger 2-3 m fixeren voor actie.",
            "Als verdediger pass afsluit → dribbel of schot.",
            "Als verdediger dribbel afsluit → pass dan diagonaal inlopen.",
            "8 herhalingen per aanvaller, rotatie met verdediger."
        ],
        "variants_fr": [
            "Défenseur démarre 2 m derrière pour simuler transition.",
            "Limiter à 5 s pour frapper."
        ],
        "variants_nl": [
            "Verdediger start 2 m achter om transitie te simuleren.",
            "Beperk tot 5 s voor schot."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.156",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [17, 13], "label": "A1"},
                {"type": "player", "team": "red", "pos": [17, 7], "label": "A2"},
                {"type": "ball", "pos": [17, 13]},
                {"type": "player", "team": "blue", "pos": [10, 10], "label": "D"},
                {"type": "arrow", "from": [17, 13], "to": [10, 13], "kind": "offense"},
                {"type": "arrow", "from": [17, 13], "to": [17, 7], "kind": "ball"},
                {"type": "arrow", "from": [17, 7], "to": [10, 7], "kind": "offense"}
            ]
        }
    },
    {
        "id": "ta-03",
        "category": "tactique",
        "subcategory": "3c2",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 8,
        "intensity": "élevée",
        "title_fr": "3v2 largeur-profondeur",
        "title_nl": "3v2 breedte-diepte",
        "objective_fr": "Utiliser largeur et profondeur en supériorité, timing des appels.",
        "objective_nl": "Breedte en diepte benutten bij overtal, timing van inlopen.",
        "setup_fr": "Demi-terrain. 3 attaquants, 2 défenseurs, 1 gardien. Zone départ au milieu.",
        "setup_nl": "Halve veld. 3 aanvallers, 2 verdedigers, 1 keeper. Startzone in midden.",
        "instructions_fr": [
            "Les 3 attaquants partent en triangle : 1 au centre, 2 aux ailes.",
            "Les ailiers fixent les défenseurs sur leur couloir.",
            "Le central crée décalages par conduite ou passe.",
            "Finition : passe latérale + appel second poteau.",
            "Tour 1 : jeu libre. Tour 2 : 2 passes max avant tir."
        ],
        "instructions_nl": [
            "3 aanvallers in driehoek: 1 centraal, 2 op vleugels.",
            "Vleugelspelers fixeren verdedigers op hun kant.",
            "Middenspeler creëert ruimte door dribbel of pass.",
            "Afwerking: zijpass + inlopen tweede paal.",
            "Ronde 1: vrij spel. Ronde 2: max 2 passes voor schot."
        ],
        "variants_fr": [
            "Défenseurs + GK démarrent en transition (course retour).",
            "Imposer finition en 1 touche."
        ],
        "variants_nl": [
            "Verdedigers + keeper starten in transitie (terugloop).",
            "Verplicht 1-touch afwerking."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.7",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [17, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [17, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [17, 6], "label": "A3"},
                {"type": "ball", "pos": [17, 10]},
                {"type": "player", "team": "blue", "pos": [10, 12], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [10, 8], "label": "D2"},
                {"type": "arrow", "from": [17, 10], "to": [10, 10], "kind": "offense"},
                {"type": "arrow", "from": [17, 14], "to": [5, 14], "kind": "offense"},
                {"type": "arrow", "from": [17, 6], "to": [5, 6], "kind": "offense"}
            ]
        }
    }
]

TACTIQUE.extend([
    {
        "id": "ta-04",
        "category": "tactique",
        "subcategory": "bloc défensif",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "Bloc 2-2 organisation",
        "title_nl": "Blok 2-2 organisatie",
        "objective_fr": "Coordination bloc défensif à 4 joueurs : distances, couvertures, orientation.",
        "objective_nl": "Coördinatie 4-mans verdedigingsblok: afstanden, dekking, oriëntatie.",
        "setup_fr": "Terrain complet ou moitié. 4 défenseurs en 2-2. 4 attaquants + gardien.",
        "setup_nl": "Volledig veld of helft. 4 verdedigers in 2-2. 4 aanvallers + keeper.",
        "instructions_fr": [
            "Les 4 défenseurs se placent en 2-2, distances 4-6 m entre joueurs.",
            "Règle : quand porteur franchit médiane, toute la ligne coulisse.",
            "Quand ballon à l'aile : bloc se décale du côté du ballon.",
            "Pression sur porteur, couverture du défenseur le plus proche.",
            "Changer les rôles après 3 min."
        ],
        "instructions_nl": [
            "4 verdedigers in 2-2, 4-6 m tussen spelers.",
            "Regel: zodra balbezitter midlijn overschrijdt, hele linie schuift.",
            "Bal op vleugel: blok schuift naar balkant.",
            "Druk op balbezitter, dekking dichtste verdediger.",
            "Rolwissel na 3 min."
        ],
        "variants_fr": [
            "Limiter attaquants à 3 touches max.",
            "Coach scanne attaques pour noter distances entre défenseurs."
        ],
        "variants_nl": [
            "Aanvallers max 3 contacten.",
            "Coach scant aanvallen om afstanden te noteren."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.168",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "blue", "pos": [14, 13], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [14, 7], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [8, 13], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [8, 7], "label": "D4"},
                {"type": "player", "team": "red", "pos": [25, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [22, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [22, 6], "label": "A3"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "A4"},
                {"type": "ball", "pos": [25, 10]}
            ]
        }
    },
    {
        "id": "ta-05",
        "category": "tactique",
        "subcategory": "pressing",
        "age_range": "U15-Senior",
        "duration": 12,
        "players_min": 10,
        "intensity": "élevée",
        "title_fr": "Pressing haut 4v4 + GK",
        "title_nl": "Hoge druk 4v4 + GK",
        "objective_fr": "Mettre en place le pressing coordonné en phase de relance adverse.",
        "objective_nl": "Gecoördineerde druk bij tegenstander-opbouw instellen.",
        "setup_fr": "Terrain complet. 2 équipes 4+1. Relance démarre sur gardien.",
        "setup_nl": "Volledig veld. 2 teams 4+1. Opbouw start bij keeper.",
        "instructions_fr": [
            "Équipe en défense démarre relance sur son GK.",
            "Équipe en pressing déclenche dès que GK touche ballon.",
            "Attaquant le plus proche oriente la relance côté faible.",
            "Les 3 autres ferment lignes de passes adjacentes.",
            "Objectif : récupérer dans les 10 s ou contraindre sortie en touche."
        ],
        "instructions_nl": [
            "Verdedigend team start opbouw bij keeper.",
            "Drukkend team start druk zodra keeper bal raakt.",
            "Dichtste aanvaller dwingt opbouw naar zwakke kant.",
            "3 anderen sluiten aangrenzende pasopties.",
            "Doel: balrecuperatie binnen 10 s of bal uit spel dwingen."
        ],
        "variants_fr": [
            "Récupération haute = 2 points, but classique = 1 point.",
            "GK doit jouer 1 touche maximum."
        ],
        "variants_nl": [
            "Hoge balrecuperatie = 2 punten, gewoon doelpunt = 1 punt.",
            "Keeper 1-touch verplicht."
        ],
        "source": "RFEF — Presión coordinada en fútbol sala",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [5, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [10, 15], "label": "A2"},
                {"type": "player", "team": "red", "pos": [10, 5], "label": "A3"},
                {"type": "player", "team": "red", "pos": [15, 10], "label": "A4"},
                {"type": "ball", "pos": [0.5, 10]},
                {"type": "player", "team": "blue", "pos": [8, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [13, 15], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [13, 5], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [18, 10], "label": "D4"},
                {"type": "arrow", "from": [8, 10], "to": [5, 10], "kind": "defense"},
                {"type": "arrow", "from": [13, 15], "to": [10, 15], "kind": "defense"}
            ]
        }
    },
    {
        "id": "ta-06",
        "category": "tactique",
        "subcategory": "bloc médian",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "Bloc médian 1-2-1",
        "title_nl": "Middenblok 1-2-1",
        "objective_fr": "Bloc médian compact, oblige l'adversaire à jouer sur les côtés.",
        "objective_nl": "Compact middenblok, dwingt tegenstander naar de kanten.",
        "setup_fr": "Terrain complet. 1 pivot, 2 ailes, 1 fixo + gardien côté défense. 4 attaquants.",
        "setup_nl": "Volledig veld. 1 pivot, 2 vleugels, 1 fixo + keeper. 4 aanvallers.",
        "instructions_fr": [
            "Bloc 1-2-1 se place à 15 m du but.",
            "Fixo oriente, les 2 ailes verrouillent couloirs, pivot harcèle.",
            "Règle de sortie : 1 défenseur maximum franchit la ligne du bloc.",
            "Si pas de pression efficace, repli en bloc bas.",
            "Après récupération → contre-attaque directe."
        ],
        "instructions_nl": [
            "Blok 1-2-1 staat op 15 m van doel.",
            "Fixo dirigeert, 2 vleugels sluiten kanten, pivot hindert.",
            "Uittredingsregel: max 1 verdediger voorbij blok.",
            "Geen effectieve druk → terug in laag blok.",
            "Na recuperatie → directe counter."
        ],
        "variants_fr": [
            "Ajouter règle : passe à travers bloc = but automatique pour attaque.",
            "Chronométrer durée de possession adverse."
        ],
        "variants_nl": [
            "Regel: pass door blok = automatisch doelpunt voor aanval.",
            "Duur balbezit tegenstander chronometreren."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.178",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "blue", "pos": [20, 10], "label": "Pv"},
                {"type": "player", "team": "blue", "pos": [15, 14], "label": "W1"},
                {"type": "player", "team": "blue", "pos": [15, 6], "label": "W2"},
                {"type": "player", "team": "blue", "pos": [10, 10], "label": "Fx"},
                {"type": "player", "team": "red", "pos": [30, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [26, 15], "label": "A2"},
                {"type": "player", "team": "red", "pos": [26, 5], "label": "A3"},
                {"type": "player", "team": "red", "pos": [22, 10], "label": "A4"},
                {"type": "ball", "pos": [30, 10]}
            ]
        }
    }
])

TACTIQUE.extend([
    {
        "id": "ta-07",
        "category": "tactique",
        "subcategory": "transition",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 8,
        "intensity": "élevée",
        "title_fr": "Transition 4v4 → 4v3",
        "title_nl": "Transitie 4v4 → 4v3",
        "objective_fr": "Réagir rapidement à une perte/récupération pour basculer attaque-défense.",
        "objective_nl": "Snel reageren bij balverlies/recuperatie voor omschakeling.",
        "setup_fr": "Terrain complet. 2 équipes de 4 + gardiens. Coach sert le ballon à n'importe quelle équipe.",
        "setup_nl": "Volledig veld. 2 teams van 4 + keepers. Coach bedient willekeurig team.",
        "instructions_fr": [
            "Au signal, coach distribue à une équipe.",
            "Équipe en possession a 10 s pour attaquer, l'autre 1 joueur en moins.",
            "Au but, perte ou 10 s, nouveau service côté adverse.",
            "Accent : premier joueur revient au pressing, le reste replie.",
            "3 blocs de 3 min, 1 min récupération."
        ],
        "instructions_nl": [
            "Op signaal bedient coach een team.",
            "Balbezittend team heeft 10 s, ander 1 speler minder.",
            "Bij doelpunt, verlies of 10 s: nieuwe bediening ander team.",
            "Accent: eerste speler terug in druk, rest zakt in.",
            "3 blokken van 3 min, 1 min herstel."
        ],
        "variants_fr": [
            "Ajouter règle : 1ere passe obligatoirement vers l'avant.",
            "Après 5 s, joueur manquant rentre en jeu."
        ],
        "variants_nl": [
            "Regel: eerste pass verplicht naar voren.",
            "Na 5 s: ontbrekende speler komt erbij."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.184",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "gk", "pos": [39.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [12, 12], "label": "A1"},
                {"type": "player", "team": "red", "pos": [16, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [20, 14], "label": "A3"},
                {"type": "player", "team": "red", "pos": [22, 8], "label": "A4"},
                {"type": "player", "team": "blue", "pos": [26, 12], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [24, 7], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [30, 10], "label": "D3"},
                {"type": "ball", "pos": [16, 10]},
                {"type": "arrow", "from": [16, 10], "to": [30, 10], "kind": "offense"}
            ]
        }
    },
    {
        "id": "ta-08",
        "category": "tactique",
        "subcategory": "supériorité numérique",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 7,
        "intensity": "élevée",
        "title_fr": "4v3 maintien supériorité",
        "title_nl": "4v3 overtal behouden",
        "objective_fr": "Conserver l'avantage numérique : positionnement en losange, passes rapides.",
        "objective_nl": "Overtal behouden: ruitpositionering, snelle passes.",
        "setup_fr": "Demi-terrain. 4 attaquants vs 3 défenseurs + GK. Zone de tir 12 m.",
        "setup_nl": "Halve veld. 4 aanvallers vs 3 verdedigers + GK. Schotzone 12 m.",
        "instructions_fr": [
            "Losange : 1 derrière, 2 côtés, 1 pivot.",
            "Passe rapide pour trouver le joueur libre.",
            "Principe : fixer 2 défenseurs pour créer 2v1 latéral.",
            "Finition obligatoire en moins de 15 s.",
            "Variante : 1 attaquant ne peut pas être en zone de tir."
        ],
        "instructions_nl": [
            "Ruit: 1 achter, 2 zijkanten, 1 pivot.",
            "Snelle pass om vrije speler te vinden.",
            "Principe: 2 verdedigers fixeren om lateraal 2v1 te creëren.",
            "Afwerking verplicht in <15 s.",
            "Variant: 1 aanvaller mag niet in schotzone."
        ],
        "variants_fr": [
            "Réduire 4v3 → 5v4 pour tester supériorité en densité.",
            "Imposer 1 passe minimum avant frappe."
        ],
        "variants_nl": [
            "Verklein 4v3 → 5v4 om dichtheid te testen.",
            "Verplicht min. 1 pass voor schot."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.8",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [15, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [11, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [11, 6], "label": "A3"},
                {"type": "player", "team": "red", "pos": [6, 10], "label": "A4"},
                {"type": "ball", "pos": [15, 10]},
                {"type": "player", "team": "blue", "pos": [9, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [5, 13], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [5, 7], "label": "D3"},
                {"type": "arrow", "from": [15, 10], "to": [11, 14], "kind": "ball"}
            ]
        }
    },
    {
        "id": "ta-09",
        "category": "tactique",
        "subcategory": "infériorité",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 7,
        "intensity": "élevée",
        "title_fr": "3v4 défense infériorité",
        "title_nl": "3v4 verdediging in ondertal",
        "objective_fr": "Tenir en infériorité : zone, couverture, fermer axe, retarder l'action.",
        "objective_nl": "Ondertal standhouden: zone, dekking, as sluiten, actie vertragen.",
        "setup_fr": "Demi-terrain. 3 défenseurs + GK vs 4 attaquants. Attaquants partent à 20 m.",
        "setup_nl": "Halve veld. 3 verdedigers + GK vs 4 aanvallers. Aanvallers starten op 20 m.",
        "instructions_fr": [
            "Défenseurs en triangle compact, sommet le plus haut.",
            "Ne jamais sortir 2 défenseurs simultanément.",
            "Forcer l'attaquant sur son pied faible ou latéral.",
            "Gardien sort pour couper passe en profondeur.",
            "Objectif : tenir 15 s sans but ou forcer erreur."
        ],
        "instructions_nl": [
            "Verdedigers in compacte driehoek, punt vooraan.",
            "Nooit 2 verdedigers tegelijk uitbreken.",
            "Aanvaller dwingen op zwakke voet of flank.",
            "Keeper komt uit om diepe pass te onderscheppen.",
            "Doel: 15 s standhouden zonder doelpunt of fout afdwingen."
        ],
        "variants_fr": [
            "Si défenseurs tiennent 20 s → 1 défenseur entre (égalité numérique).",
            "Noter les récupérations par type (interception, duel, tacle)."
        ],
        "variants_nl": [
            "Als verdedigers 20 s standhouden → 1 verdediger erbij (gelijk aantal).",
            "Recuperaties noteren per type (onderschepping, duel, tackle)."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.192",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "blue", "pos": [8, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [5, 14], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [5, 6], "label": "D3"},
                {"type": "player", "team": "red", "pos": [16, 10], "label": "A1"},
                {"type": "player", "team": "red", "pos": [13, 14], "label": "A2"},
                {"type": "player", "team": "red", "pos": [13, 6], "label": "A3"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "A4"},
                {"type": "ball", "pos": [16, 10]}
            ]
        }
    }
])

TACTIQUE.extend([
    {
        "id": "ta-10",
        "category": "tactique",
        "subcategory": "bloc bas",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "Bloc bas 4v4 + GK",
        "title_nl": "Laag blok 4v4 + GK",
        "objective_fr": "Tenir dans les 10 derniers mètres, fermer les espaces clés, encaisser pression.",
        "objective_nl": "Laatste 10 m standhouden, sleutelruimtes afsluiten, druk opvangen.",
        "setup_fr": "Demi-terrain. Défenseurs en bloc bas à 8 m du but. Attaquants partent à 18 m.",
        "setup_nl": "Halve veld. Verdedigers in laag blok op 8 m van doel. Aanvallers starten op 18 m.",
        "instructions_fr": [
            "Défenseurs en ligne 4, distance 3 m entre chacun.",
            "Centre du terrain occupé en priorité, couloirs secondaires.",
            "Gardien en ligne avec défenseurs sur ballon aérien.",
            "Les 4 ne sortent jamais tous simultanément.",
            "Récupération = sortie rapide en contre."
        ],
        "instructions_nl": [
            "Verdedigers op lijn 4, 3 m tussenruimte.",
            "Centrale zone prioriteit, vleugels secundair.",
            "Keeper op lijn met verdedigers bij luchtbal.",
            "Niet alle 4 tegelijk eruit.",
            "Recuperatie = snelle uitbraak in counter."
        ],
        "variants_fr": [
            "Ajouter règle : attaque limitée à 30 s.",
            "Coach donne un score à atteindre (ex. 3 buts en 5 min)."
        ],
        "variants_nl": [
            "Regel: aanval beperkt tot 30 s.",
            "Coach geeft doelscore (bv. 3 doelpunten in 5 min)."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.8 Low block",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "blue", "pos": [6, 13], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [6, 7], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [4, 10], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [8, 10], "label": "D4"},
                {"type": "player", "team": "red", "pos": [16, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [13, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [16, 6], "label": "A3"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "A4"},
                {"type": "ball", "pos": [13, 10]}
            ]
        }
    },
    {
        "id": "ta-11",
        "category": "tactique",
        "subcategory": "para",
        "age_range": "U15-Senior",
        "duration": 12,
        "players_min": 10,
        "intensity": "moyenne",
        "title_fr": "Para (pick & roll futsal)",
        "title_nl": "Para (pick & roll futsal)",
        "objective_fr": "Exécuter un blocage-roulé : poser écran puis rouler vers but ou espace.",
        "objective_nl": "Blok-en-rol uitvoeren: scherm zetten dan draaien naar doel of ruimte.",
        "setup_fr": "Demi-terrain. 2 attaquants vs 2 défenseurs + GK. Coach sert ballon à l'un.",
        "setup_nl": "Halve veld. 2 aanvallers vs 2 verdedigers + GK. Coach bedient één speler.",
        "instructions_fr": [
            "Attaquant A a le ballon, B vient poser écran sur D1.",
            "A utilise l'écran pour conduire ou passer.",
            "B se retourne (roll) en appel dans l'espace libre.",
            "Défenseur D1 doit annoncer switch ou contourner.",
            "3 répétitions par côté, rotation A/B."
        ],
        "instructions_nl": [
            "A heeft bal, B komt scherm zetten op D1.",
            "A gebruikt scherm om te dribbelen of passen.",
            "B draait (roll) in vrije ruimte.",
            "D1 moet 'switch' roepen of omzeilen.",
            "3 herhalingen per kant, rotatie A/B."
        ],
        "variants_fr": [
            "Imposer finition en 2 passes max.",
            "Défenseurs consigne : pas de switch, forcer contournement."
        ],
        "variants_nl": [
            "Afwerking in max 2 passes.",
            "Verdedigers opdracht: geen switch, rond scherm lopen."
        ],
        "source": "RFEF — Sistema de juego 'Para' en fútbol sala",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [16, 10], "label": "A"},
                {"type": "ball", "pos": [16, 10]},
                {"type": "player", "team": "red", "pos": [13, 10], "label": "B"},
                {"type": "player", "team": "blue", "pos": [12, 10], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [8, 10], "label": "D2"},
                {"type": "arrow", "from": [16, 10], "to": [12, 8], "kind": "offense"},
                {"type": "arrow", "from": [13, 10], "to": [10, 14], "kind": "offense"}
            ]
        }
    },
    {
        "id": "ta-12",
        "category": "tactique",
        "subcategory": "sortie de pressing",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 9,
        "intensity": "moyenne",
        "title_fr": "Relance sous pression (4v3)",
        "title_nl": "Opbouw onder druk (4v3)",
        "objective_fr": "Construire proprement en zone basse face à un pressing haut.",
        "objective_nl": "Zuiver opbouwen in achterhoede onder hoge druk.",
        "setup_fr": "Demi-terrain. 4 relanceurs + GK, 3 presseurs. Objectif = franchir ligne à 25 m.",
        "setup_nl": "Halve veld. 4 opbouwers + GK, 3 drukzetters. Doel = lijn op 25 m passeren.",
        "instructions_fr": [
            "Relance démarre sur GK.",
            "Créer 2 lignes : 1 appui court (pivot qui décroche), 1 appui profond.",
            "Principe : passer sur le joueur libre, orienter pour progression.",
            "Un appui doit toujours se proposer derrière le ballon.",
            "Variante : imposer 1 passe sur GK avant la ligne."
        ],
        "instructions_nl": [
            "Opbouw start bij keeper.",
            "2 lijnen creëren: 1 korte steun (pivot inzakt), 1 diepe steun.",
            "Principe: pass naar vrije speler, oriënteren op progressie.",
            "Altijd 1 steun achter bal.",
            "Variant: verplicht 1 pass naar keeper vóór lijn passeren."
        ],
        "variants_fr": [
            "Relance en 6 s max.",
            "Presseurs deviennent 4 (égalité) si 1 passe manquée."
        ],
        "variants_nl": [
            "Opbouw in max 6 s.",
            "Drukzetters worden 4 (gelijk) na 1 gemiste pass."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.202",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [4, 14], "label": "R1"},
                {"type": "player", "team": "red", "pos": [4, 6], "label": "R2"},
                {"type": "player", "team": "red", "pos": [8, 10], "label": "R3"},
                {"type": "player", "team": "red", "pos": [14, 10], "label": "R4"},
                {"type": "ball", "pos": [0.5, 10]},
                {"type": "player", "team": "blue", "pos": [7, 14], "label": "P1"},
                {"type": "player", "team": "blue", "pos": [7, 6], "label": "P2"},
                {"type": "player", "team": "blue", "pos": [11, 10], "label": "P3"},
                {"type": "arrow", "from": [0.5, 10], "to": [4, 14], "kind": "ball"},
                {"type": "arrow", "from": [4, 14], "to": [14, 10], "kind": "ball"}
            ]
        }
    }
])

TACTIQUE.extend([
    {
        "id": "ta-13",
        "category": "tactique",
        "subcategory": "pivot",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 7,
        "intensity": "moyenne",
        "title_fr": "Jeu avec pivot — remise",
        "title_nl": "Pivotspel — terugkaatsen",
        "objective_fr": "Utiliser le pivot fixe comme point d'appui offensif, remise + tir.",
        "objective_nl": "Vaste pivot gebruiken als aanvalssteun, terugleggen + schot.",
        "setup_fr": "Demi-terrain. Pivot à 8 m du but, 3 joueurs en ligne à 18 m + GK.",
        "setup_nl": "Halve veld. Pivot op 8 m van doel, 3 spelers op lijn op 18 m + GK.",
        "instructions_fr": [
            "Un joueur de la ligne passe au pivot.",
            "Pivot remise en 1 touche à un autre appui entrant.",
            "Celui-ci fait 1 passe ou frappe directement.",
            "Varier : remise à gauche, remise à droite.",
            "Rotation du pivot toutes les 2 min."
        ],
        "instructions_nl": [
            "Een speler uit de lijn speelt naar pivot.",
            "Pivot legt 1-touch terug op andere inkomende steun.",
            "Die speelt 1 pass of schiet direct.",
            "Afwisselen: links, rechts terugleggen.",
            "Rotatie pivot elke 2 min."
        ],
        "variants_fr": [
            "Ajouter défenseur sur pivot.",
            "Imposer finition en 1 touche."
        ],
        "variants_nl": [
            "Verdediger op pivot.",
            "Verplicht 1-touch afwerking."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.7",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [8, 10], "label": "Pv"},
                {"type": "player", "team": "red", "pos": [17, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [17, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [17, 6], "label": "A3"},
                {"type": "ball", "pos": [17, 10]},
                {"type": "arrow", "from": [17, 10], "to": [8, 10], "kind": "ball"},
                {"type": "arrow", "from": [8, 10], "to": [13, 14], "kind": "ball"},
                {"type": "arrow", "from": [17, 14], "to": [13, 14], "kind": "offense"}
            ]
        }
    },
    {
        "id": "ta-14",
        "category": "tactique",
        "subcategory": "circulation",
        "age_range": "U13-Senior",
        "duration": 12,
        "players_min": 8,
        "intensity": "moyenne",
        "title_fr": "Circulation 3-1 sans tir",
        "title_nl": "Circulatie 3-1 zonder schot",
        "objective_fr": "Circulation longue du ballon pour déstabiliser et étirer la défense.",
        "objective_nl": "Lange circulatie om defensie te destabiliseren en uit elkaar te trekken.",
        "setup_fr": "Demi-terrain. 4 attaquants en 3-1 (3 en ligne + pivot). 4 défenseurs.",
        "setup_nl": "Halve veld. 4 aanvallers in 3-1 (3 op lijn + pivot). 4 verdedigers.",
        "instructions_fr": [
            "But interdit pendant 60 s, obligation de faire 10 passes.",
            "Pivot doit recevoir et remiser 3 fois par série.",
            "Changement d'aile obligatoire toutes les 5 passes.",
            "Après 10 passes et 3 remises → tir autorisé.",
            "Rotation des rôles toutes les 2 min."
        ],
        "instructions_nl": [
            "Schot verboden gedurende 60 s, 10 passes verplicht.",
            "Pivot moet 3x ontvangen + terugleggen per serie.",
            "Vleugelwissel elke 5 passes.",
            "Na 10 passes en 3 terugleggingen → schot toegestaan.",
            "Rolwissel elke 2 min."
        ],
        "variants_fr": [
            "Pivot seul autorisé à marquer.",
            "Ajouter 1 joker neutre pour fluidifier."
        ],
        "variants_nl": [
            "Alleen pivot mag scoren.",
            "Voeg 1 neutrale joker toe voor vloeibaarheid."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.212",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [16, 14], "label": "A1"},
                {"type": "player", "team": "red", "pos": [16, 10], "label": "A2"},
                {"type": "player", "team": "red", "pos": [16, 6], "label": "A3"},
                {"type": "player", "team": "red", "pos": [8, 10], "label": "Pv"},
                {"type": "ball", "pos": [16, 14]},
                {"type": "player", "team": "blue", "pos": [12, 14], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [12, 10], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [12, 6], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [5, 10], "label": "D4"},
                {"type": "arrow", "from": [16, 14], "to": [16, 6], "kind": "ball"}
            ]
        }
    },
    {
        "id": "ta-15",
        "category": "tactique",
        "subcategory": "GK joueur",
        "age_range": "U15-Senior",
        "duration": 10,
        "players_min": 10,
        "intensity": "élevée",
        "title_fr": "Power play (GK joueur)",
        "title_nl": "Power play (keeper als veldspeler)",
        "objective_fr": "Attaquer en 5v4 avec gardien volant, maintenir supériorité positionnelle.",
        "objective_nl": "Aanvallen in 5v4 met vliegende keeper, positioneel overtal behouden.",
        "setup_fr": "Demi-terrain. 5 attaquants (GK inclus remplaçant un joueur) vs 4 défenseurs + GK adverse.",
        "setup_nl": "Halve veld. 5 aanvallers (keeper als veldspeler) vs 4 verdedigers + tegenkeeper.",
        "instructions_fr": [
            "Disposition : 4 à l'extérieur + GK en appui au centre.",
            "Circulation rapide, minimum 6 passes avant tir.",
            "Trouver tir à l'entrée de zone sur joueur démarqué.",
            "Si récupération adverse, GK doit revenir son but en sprint.",
            "Durée : 4 blocs de 2 min avec récupération."
        ],
        "instructions_nl": [
            "Opstelling: 4 buiten + keeper als steun centraal.",
            "Snelle circulatie, min 6 passes voor schot.",
            "Zoek schot aan rand zone op vrije speler.",
            "Bij balverlies: keeper sprint terug naar eigen doel.",
            "Duur: 4 blokken van 2 min met herstel."
        ],
        "variants_fr": [
            "Imposer tir depuis le 6e mètre uniquement.",
            "Défenseurs marquent 2 points si ils marquent dans le but vide."
        ],
        "variants_nl": [
            "Schot alleen vanaf 6m+.",
            "Verdedigers krijgen 2 punten bij doelpunt in leeg doel."
        ],
        "source": "RFEF / UEFA — Power play tactical framework",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [28, 10], "label": "GK*"},
                {"type": "player", "team": "red", "pos": [22, 15], "label": "A1"},
                {"type": "player", "team": "red", "pos": [22, 5], "label": "A2"},
                {"type": "player", "team": "red", "pos": [15, 15], "label": "A3"},
                {"type": "player", "team": "red", "pos": [15, 5], "label": "A4"},
                {"type": "ball", "pos": [28, 10]},
                {"type": "player", "team": "blue", "pos": [12, 15], "label": "D1"},
                {"type": "player", "team": "blue", "pos": [12, 5], "label": "D2"},
                {"type": "player", "team": "blue", "pos": [8, 12], "label": "D3"},
                {"type": "player", "team": "blue", "pos": [8, 8], "label": "D4"},
                {"type": "arrow", "from": [28, 10], "to": [22, 15], "kind": "ball"},
                {"type": "arrow", "from": [22, 15], "to": [15, 15], "kind": "ball"}
            ]
        }
    }
])
