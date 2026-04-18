"""Warm-up exercises (10) — échauffements dynamiques orientés futsal U15."""

WARMUPS = [
    {
        "id": "wu-01",
        "category": "warmup",
        "subcategory": "mobilité",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 6,
        "intensity": "faible",
        "title_fr": "Mobilité articulaire dynamique",
        "title_nl": "Dynamische gewrichtsmobiliteit",
        "objective_fr": "Préparer articulations et chaînes musculaires au contact répété du futsal.",
        "objective_nl": "Gewrichten en spierketens voorbereiden op het herhaalde contact van futsal.",
        "setup_fr": "Joueurs en demi-cercle face au coach, 1,5 m entre chacun, sans ballon.",
        "setup_nl": "Spelers in halve cirkel tegenover coach, 1,5 m tussenruimte, zonder bal.",
        "instructions_fr": [
            "Rotations de chevilles (10 par côté), puis de genoux (10).",
            "Fentes avant marchées 10 m, retour avec rotation de buste.",
            "Skipping bas puis haut sur 10 m, allers-retours.",
            "Déplacements latéraux croisés (pas chassés + rotation hanche).",
            "Finir par 2 x accélérations progressives sur 15 m."
        ],
        "instructions_nl": [
            "Enkelrotaties (10 per kant), dan knierotaties (10).",
            "Uitvalpassen vooruit 10 m, terug met romprotatie.",
            "Lage dan hoge skipping over 10 m, heen en weer.",
            "Zijwaartse kruispassen (chassé + heuprotatie).",
            "Afsluiten met 2 x progressieve versnellingen over 15 m."
        ],
        "variants_fr": [
            "Ajouter un ballon en main pour travail coordination bras/jambes.",
            "Enchaîner avec mini-jeu de réaction visuelle (coach pointe direction)."
        ],
        "variants_nl": [
            "Voeg bal in de hand toe voor coördinatie arm/been.",
            "Volg met mini-reactiespel (coach wijst richting aan)."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.58",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "cone", "pos": [12, 4]},
                {"type": "cone", "pos": [22, 4]},
                {"type": "player", "team": "red", "pos": [12, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [15, 10], "label": "2"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "3"},
                {"type": "player", "team": "red", "pos": [21, 10], "label": "4"},
                {"type": "player", "team": "red", "pos": [24, 10], "label": "5"},
                {"type": "player", "team": "yellow", "pos": [17, 14], "label": "C"},
                {"type": "arrow", "from": [12, 10], "to": [12, 4], "kind": "offense"},
                {"type": "arrow", "from": [22, 4], "to": [22, 10], "kind": "offense"}
            ]
        }
    },
    {
        "id": "wu-02",
        "category": "warmup",
        "subcategory": "conduite",
        "age_range": "U11-Senior",
        "duration": 6,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Conduite libre en zone",
        "title_nl": "Vrij dribbelen in zone",
        "objective_fr": "Relancer le toucher de balle, varier appuis et prise d'information tête haute.",
        "objective_nl": "Balgevoel activeren, steunbenen variëren en rondkijken met opgeheven hoofd.",
        "setup_fr": "Zone 20×15 m délimitée par 8 cônes. 1 ballon par joueur.",
        "setup_nl": "Zone 20×15 m afgebakend met 8 kegels. 1 bal per speler.",
        "instructions_fr": [
            "Conduite libre, tête haute, éviter contacts et ballons adverses.",
            "Au signal coach, changer de pied/surface (semelle, intérieur, extérieur).",
            "Toutes les 30 s : 3 dribbles puis stop-and-go.",
            "Terminer par 3 x 20 s de conduite vitesse maximale contrôlée.",
            "Récupération active : jongles en équipe libres."
        ],
        "instructions_nl": [
            "Vrij dribbelen, hoofd omhoog, contact en ballen van anderen vermijden.",
            "Op signaal coach: wissel voet/voetoppervlak (zool, binnenkant, buitenkant).",
            "Elke 30 s: 3 dribbels dan stop-and-go.",
            "Afsluiten met 3 x 20 s gecontroleerd maximaal tempo dribbelen.",
            "Actief herstel: vrij jongleren in team."
        ],
        "variants_fr": [
            "Ajouter 2 'voleurs' sans ballon qui tentent de sortir les ballons.",
            "Imposer semelle uniquement pendant 1 minute."
        ],
        "variants_nl": [
            "Voeg 2 'dieven' zonder bal toe die ballen proberen weg te tikken.",
            "Verplicht enkel zool gedurende 1 minuut."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.4",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "cone", "pos": [10, 5]},
                {"type": "cone", "pos": [30, 5]},
                {"type": "cone", "pos": [10, 15]},
                {"type": "cone", "pos": [30, 15]},
                {"type": "cone", "pos": [20, 5]},
                {"type": "cone", "pos": [20, 15]},
                {"type": "cone", "pos": [10, 10]},
                {"type": "cone", "pos": [30, 10]},
                {"type": "player", "team": "red", "pos": [14, 8], "label": ""},
                {"type": "ball", "pos": [14, 8]},
                {"type": "player", "team": "red", "pos": [18, 12], "label": ""},
                {"type": "ball", "pos": [18, 12]},
                {"type": "player", "team": "red", "pos": [22, 7], "label": ""},
                {"type": "ball", "pos": [22, 7]},
                {"type": "player", "team": "red", "pos": [26, 13], "label": ""},
                {"type": "ball", "pos": [26, 13]},
                {"type": "player", "team": "red", "pos": [15, 13], "label": ""},
                {"type": "ball", "pos": [15, 13]},
                {"type": "player", "team": "red", "pos": [25, 8], "label": ""},
                {"type": "ball", "pos": [25, 8]}
            ]
        }
    },
    {
        "id": "wu-03",
        "category": "warmup",
        "subcategory": "passes",
        "age_range": "U11-Senior",
        "duration": 8,
        "players_min": 6,
        "intensity": "moyenne",
        "title_fr": "Passes par 2 — progression",
        "title_nl": "Passen per 2 — progressie",
        "objective_fr": "Qualité de passe au sol, orientation du corps, contrôle orienté vers l'avant.",
        "objective_nl": "Kwaliteit van grondpass, lichaamsoriëntatie, gerichte controle vooruit.",
        "setup_fr": "Paires face à face, 6 m d'écart. 1 ballon par paire. Couloir 15 m de long pour progresser.",
        "setup_nl": "Paren tegenover elkaar, 6 m uit elkaar. 1 bal per paar. Corridor 15 m lang om te vorderen.",
        "instructions_fr": [
            "30 s de passes statiques intérieur pied droit, puis 30 s pied gauche.",
            "Passe et va : après passe, appel pour recevoir en avançant de 1 m.",
            "Une-deux (mur) : joueur A passe à B, B remise en 1 touche, A avance 2 m.",
            "Progression jusqu'au bout du couloir, puis retour.",
            "Finale : passe en mouvement, contrôle orienté + 1 touche de passe."
        ],
        "instructions_nl": [
            "30 s statische passes binnenkant rechts, dan 30 s links.",
            "Pas-en-ga: na pass, loop in om 1 m vooruit te ontvangen.",
            "Een-twee (muurtje): A past op B, B 1-touch terug, A gaat 2 m vooruit.",
            "Progressie tot einde corridor, dan terug.",
            "Finale: pass in beweging, gerichte controle + 1-touch pass."
        ],
        "variants_fr": [
            "Imposer 2 touches max (contrôle + passe).",
            "Ajouter 1 cône central à contourner avant chaque passe."
        ],
        "variants_nl": [
            "Verplicht max 2 contacten (controle + pass).",
            "Voeg 1 middencone toe die omzeild moet worden voor elke pass."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.72",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "player", "team": "red", "pos": [10, 7], "label": "A"},
                {"type": "player", "team": "red", "pos": [16, 7], "label": "B"},
                {"type": "ball", "pos": [10, 7]},
                {"type": "arrow", "from": [10, 7], "to": [16, 7], "kind": "ball"},
                {"type": "arrow", "from": [10, 7], "to": [14, 7], "kind": "offense"},
                {"type": "player", "team": "red", "pos": [10, 13], "label": "C"},
                {"type": "player", "team": "red", "pos": [16, 13], "label": "D"},
                {"type": "ball", "pos": [10, 13]},
                {"type": "arrow", "from": [10, 13], "to": [16, 13], "kind": "ball"},
                {"type": "cone", "pos": [25, 7]},
                {"type": "cone", "pos": [25, 13]}
            ]
        }
    }
]

WARMUPS.extend([
    {
        "id": "wu-04",
        "category": "warmup",
        "subcategory": "coordination",
        "age_range": "U11-U17",
        "duration": 7,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Échelle de coordination",
        "title_nl": "Coördinatieladder",
        "objective_fr": "Vitesse d'appuis, pose de pied précise, coordination jambes/bras.",
        "objective_nl": "Snelheid van steunbenen, precieze voetplaatsing, coördinatie benen/armen.",
        "setup_fr": "Échelle de coordination (ou cônes au sol) 5 m de long. File indienne à 2 m de l'entrée.",
        "setup_nl": "Coördinatieladder (of kegels op de grond) 5 m lang. Rij op 2 m van de ingang.",
        "instructions_fr": [
            "Passage 1 : un pied par case, vitesse moyenne.",
            "Passage 2 : deux pieds par case, explosivité.",
            "Passage 3 : pas chassé latéral, bras actifs.",
            "Passage 4 : in-in-out-out (2 pieds dans, 2 pieds dehors).",
            "Passage 5 : sortie en accélération sur 5 m + tir ou conduite courte."
        ],
        "instructions_nl": [
            "Ronde 1: één voet per vak, gemiddeld tempo.",
            "Ronde 2: twee voeten per vak, explosief.",
            "Ronde 3: zijwaartse chassé, actieve armen.",
            "Ronde 4: in-in-out-out (2 voeten in, 2 voeten uit).",
            "Ronde 5: uitgang in versnelling over 5 m + schot of korte dribbel."
        ],
        "variants_fr": [
            "Finir chaque passage par une passe reçue d'un partenaire.",
            "Chronométrer les passages, classement par équipe."
        ],
        "variants_nl": [
            "Elke ronde afsluiten met een ontvangen pass van een medespeler.",
            "Rondes chronometreren, teamklassement."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), Warm-up appendix",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "cone", "pos": [2, 9]},
                {"type": "cone", "pos": [2, 11]},
                {"type": "cone", "pos": [3, 9]},
                {"type": "cone", "pos": [3, 11]},
                {"type": "cone", "pos": [4, 9]},
                {"type": "cone", "pos": [4, 11]},
                {"type": "cone", "pos": [5, 9]},
                {"type": "cone", "pos": [5, 11]},
                {"type": "cone", "pos": [6, 9]},
                {"type": "cone", "pos": [6, 11]},
                {"type": "player", "team": "red", "pos": [1, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [0.5, 10], "label": "2"},
                {"type": "arrow", "from": [1, 10], "to": [7, 10], "kind": "offense"}
            ]
        }
    },
    {
        "id": "wu-05",
        "category": "warmup",
        "subcategory": "rondo",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 7,
        "intensity": "moyenne",
        "title_fr": "Rondo 5v2 — mise en route",
        "title_nl": "Rondo 5v2 — opstart",
        "objective_fr": "Conservation 1-2 touches, prise d'information, pression adverse.",
        "objective_nl": "Balbezit 1-2 contacten, informatie opnemen, tegendruk.",
        "setup_fr": "Cercle de 8 m diamètre, 5 joueurs en périphérie, 2 au centre.",
        "setup_nl": "Cirkel 8 m doorsnede, 5 spelers buitenom, 2 in het midden.",
        "instructions_fr": [
            "5 passeurs extérieurs, 2 défenseurs au centre.",
            "Objectif : conserver en 2 touches max.",
            "Interception ou sortie de ballon → joueur responsable devient défenseur.",
            "Compter à voix haute les passes consécutives, record de groupe.",
            "Durée : 3 blocs de 2 min, 30 s récupération."
        ],
        "instructions_nl": [
            "5 buitenspelers, 2 verdedigers in het midden.",
            "Doel: balbezit houden met max 2 contacten.",
            "Onderschepping of bal uit → verantwoordelijke speler wordt verdediger.",
            "Tel hardop opeenvolgende passes, groepsrecord.",
            "Duur: 3 blokken van 2 min, 30 s rust."
        ],
        "variants_fr": [
            "Rondo 4v2 en carré pour progresser en triangulation.",
            "Imposer 1 seule touche pendant 30 s."
        ],
        "variants_nl": [
            "Rondo 4v2 in vierkant voor driehoekspel.",
            "1-touch verplicht gedurende 30 s."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.84",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [6.5, 14], "label": "1"},
                {"type": "player", "team": "red", "pos": [10, 13], "label": "2"},
                {"type": "player", "team": "red", "pos": [10, 7], "label": "3"},
                {"type": "player", "team": "red", "pos": [6.5, 6], "label": "4"},
                {"type": "player", "team": "red", "pos": [4, 10], "label": "5"},
                {"type": "player", "team": "blue", "pos": [7.5, 11], "label": "D"},
                {"type": "player", "team": "blue", "pos": [7.5, 9], "label": "D"},
                {"type": "ball", "pos": [6.5, 14]},
                {"type": "arrow", "from": [6.5, 14], "to": [10, 13], "kind": "ball"},
                {"type": "arrow", "from": [10, 13], "to": [10, 7], "kind": "ball"}
            ]
        }
    },
    {
        "id": "wu-06",
        "category": "warmup",
        "subcategory": "réactivité",
        "age_range": "U11-U17",
        "duration": 6,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Réactivité couleurs",
        "title_nl": "Kleurreactiviteit",
        "objective_fr": "Temps de réaction, prise de décision rapide sous signal visuel.",
        "objective_nl": "Reactietijd, snelle besluitvorming op visueel signaal.",
        "setup_fr": "4 cônes de couleurs différentes en carré (5 m de côté). Joueurs au centre.",
        "setup_nl": "4 kegels van verschillende kleuren in vierkant (5 m zijde). Spelers in het midden.",
        "instructions_fr": [
            "Coach annonce une couleur : joueurs sprintent toucher le cône correspondant.",
            "Retour en pas chassé au centre.",
            "Ajouter combinaisons : 'rouge-bleu' = toucher les 2 dans l'ordre.",
            "Variante réflexe : coach pointe avec la main sans parler.",
            "Finir par 2 x 15 s à vitesse max, récupération 30 s."
        ],
        "instructions_nl": [
            "Coach roept kleur: spelers sprinten om juiste kegel aan te raken.",
            "Terugkeer in chassé naar midden.",
            "Combinaties toevoegen: 'rood-blauw' = beide in volgorde aanraken.",
            "Reflexvariant: coach wijst met hand zonder te spreken.",
            "Afsluiten met 2 x 15 s max tempo, 30 s rust."
        ],
        "variants_fr": [
            "Version 'piège' : coach dit rouge mais pointe bleu — suivre la main.",
            "Ajouter ballon en conduite entre chaque sprint."
        ],
        "variants_nl": [
            "'Val'-variant: coach zegt rood maar wijst blauw — volg hand.",
            "Bal toevoegen tussen sprints door."
        ],
        "source": "RFEF — Escuela de entrenadores de fútbol sala, bloque físico",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "cone", "pos": [4, 12]},
                {"type": "cone", "pos": [9, 12]},
                {"type": "cone", "pos": [9, 7]},
                {"type": "cone", "pos": [4, 7]},
                {"type": "player", "team": "red", "pos": [6.5, 9.5], "label": "1"},
                {"type": "player", "team": "red", "pos": [7.5, 9.5], "label": "2"},
                {"type": "player", "team": "red", "pos": [6.5, 10.5], "label": "3"},
                {"type": "arrow", "from": [6.5, 9.5], "to": [4, 12], "kind": "offense"},
                {"type": "arrow", "from": [6.5, 9.5], "to": [9, 7], "kind": "offense"}
            ]
        }
    }
])

WARMUPS.extend([
    {
        "id": "wu-07",
        "category": "warmup",
        "subcategory": "triangulation",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 9,
        "intensity": "moyenne",
        "title_fr": "Triangulations à 3",
        "title_nl": "Driehoekjes met 3",
        "objective_fr": "Jeu en triangle, appuis décalés, qualité de passe en mouvement.",
        "objective_nl": "Driehoekspel, verspringende steunposities, kwaliteit pass in beweging.",
        "setup_fr": "3 joueurs par groupe en triangle équilatéral de 6 m. 1 ballon par groupe.",
        "setup_nl": "3 spelers per groep in gelijkzijdige driehoek van 6 m. 1 bal per groep.",
        "instructions_fr": [
            "Passe en 2 touches : contrôle orienté + passe.",
            "Après passe, le passeur remplace le receveur (rotation).",
            "Changer sens de rotation toutes les 45 s.",
            "Une-deux : joueur B remet en 1 touche vers C, A court au poste de B.",
            "Finale : 30 s à 1 touche max."
        ],
        "instructions_nl": [
            "Pass in 2 contacten: gerichte controle + pass.",
            "Na pass: passer vervangt ontvanger (rotatie).",
            "Richting wisselen elke 45 s.",
            "Een-twee: B 1-touch terug naar C, A loopt naar positie B.",
            "Finale: 30 s max 1 contact."
        ],
        "variants_fr": [
            "Ajouter 1 défenseur passif dans le triangle.",
            "Augmenter à 10 m de côté pour forcer longueur de passe."
        ],
        "variants_nl": [
            "Voeg 1 passieve verdediger toe in de driehoek.",
            "Vergroot tot 10 m zijde om pasafstand uit te rekken."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), p.88",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [4, 10], "label": "A"},
                {"type": "player", "team": "red", "pos": [9, 13], "label": "B"},
                {"type": "player", "team": "red", "pos": [9, 7], "label": "C"},
                {"type": "ball", "pos": [4, 10]},
                {"type": "arrow", "from": [4, 10], "to": [9, 13], "kind": "ball"},
                {"type": "arrow", "from": [9, 13], "to": [9, 7], "kind": "ball"},
                {"type": "arrow", "from": [9, 7], "to": [4, 10], "kind": "ball"},
                {"type": "arrow", "from": [4, 10], "to": [9, 13], "kind": "offense"}
            ]
        }
    },
    {
        "id": "wu-08",
        "category": "warmup",
        "subcategory": "tir",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "Tir progressif — circuit",
        "title_nl": "Progressief schot — circuit",
        "objective_fr": "Réveil musculaire orienté finition, précision et frappe du coup de pied.",
        "objective_nl": "Activerende opwarming gericht op afwerking, precisie en traptechniek.",
        "setup_fr": "Gardien en place. 2 files de 3 joueurs à 15 m du but, côtés opposés. 3 ballons par file.",
        "setup_nl": "Keeper staat. 2 rijen van 3 spelers op 15 m van doel, tegenover elkaar. 3 ballen per rij.",
        "instructions_fr": [
            "Tour 1 : conduite 5 m + tir placé en pied droit.",
            "Tour 2 : idem en pied gauche.",
            "Tour 3 : conduite + frappe de l'extérieur du pied.",
            "Tour 4 : 1-2 avec coach latéral avant tir.",
            "Récupération active en trottinant vers file opposée."
        ],
        "instructions_nl": [
            "Ronde 1: dribbel 5 m + geplaatst schot rechts.",
            "Ronde 2: idem links.",
            "Ronde 3: dribbel + schot met buitenkant voet.",
            "Ronde 4: een-twee met coach zijwaarts voor schot.",
            "Actief herstel joggend naar andere rij."
        ],
        "variants_fr": [
            "Ajouter un défenseur passif entre conduite et tir.",
            "Imposer contrôle en 1 touche avant tir."
        ],
        "variants_nl": [
            "Voeg passieve verdediger toe tussen dribbel en schot.",
            "Verplicht 1-touch controle voor schot."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.5",
        "diagram": {
            "pitch": "half",
            "elements": [
                {"type": "gk", "pos": [0.5, 10], "label": "GK"},
                {"type": "player", "team": "red", "pos": [15, 14], "label": "1"},
                {"type": "player", "team": "red", "pos": [17, 14], "label": "2"},
                {"type": "player", "team": "red", "pos": [15, 6], "label": "3"},
                {"type": "player", "team": "red", "pos": [17, 6], "label": "4"},
                {"type": "cone", "pos": [10, 14]},
                {"type": "cone", "pos": [10, 6]},
                {"type": "ball", "pos": [15, 14]},
                {"type": "ball", "pos": [15, 6]},
                {"type": "arrow", "from": [15, 14], "to": [10, 14], "kind": "offense"},
                {"type": "arrow", "from": [10, 14], "to": [0.5, 10], "kind": "ball"},
                {"type": "arrow", "from": [15, 6], "to": [10, 6], "kind": "offense"},
                {"type": "arrow", "from": [10, 6], "to": [0.5, 10], "kind": "ball"}
            ]
        }
    },
    {
        "id": "wu-09",
        "category": "warmup",
        "subcategory": "duels",
        "age_range": "U13-Senior",
        "duration": 7,
        "players_min": 6,
        "intensity": "élevée",
        "title_fr": "1v1 aller simple",
        "title_nl": "1v1 enkele passage",
        "objective_fr": "Mise en jambes duels, agressivité contrôlée, répétition des feintes.",
        "objective_nl": "Opwarmen duels, gecontroleerde agressie, herhaling van schijnbewegingen.",
        "setup_fr": "2 files face à face à 10 m, cône central. Attaquant d'un côté, défenseur de l'autre.",
        "setup_nl": "2 rijen tegenover elkaar op 10 m, middencone. Aanvaller aan één kant, verdediger aan andere.",
        "instructions_fr": [
            "Attaquant part en conduite, défenseur sort quand attaquant passe le cône.",
            "Objectif attaquant : franchir la ligne défenseur avec ballon.",
            "Rotation : attaquant devient défenseur, défenseur rejoint file attaque.",
            "Imposer une feinte obligatoire après 3 répétitions.",
            "8 répétitions par joueur maximum."
        ],
        "instructions_nl": [
            "Aanvaller vertrekt met bal, verdediger komt pas uit zodra aanvaller cone passeert.",
            "Doel aanvaller: lijn van verdediger doorkruisen met bal.",
            "Rotatie: aanvaller wordt verdediger, verdediger gaat naar aanvallersrij.",
            "Verplichte schijnbeweging na 3 herhalingen.",
            "Max 8 herhalingen per speler."
        ],
        "variants_fr": [
            "Limiter à 5 secondes par duel.",
            "Imposer pied faible uniquement."
        ],
        "variants_nl": [
            "Beperk tot 5 seconden per duel.",
            "Alleen zwakke voet verplicht."
        ],
        "source": "UEFA Futsal Coaching Manual (2020), Duel drills",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [2, 10], "label": "A"},
                {"type": "cone", "pos": [6.5, 10]},
                {"type": "player", "team": "blue", "pos": [11, 10], "label": "D"},
                {"type": "ball", "pos": [2, 10]},
                {"type": "arrow", "from": [2, 10], "to": [11, 10], "kind": "offense"},
                {"type": "arrow", "from": [11, 10], "to": [6.5, 10], "kind": "defense"}
            ]
        }
    },
    {
        "id": "wu-10",
        "category": "warmup",
        "subcategory": "possession",
        "age_range": "U13-Senior",
        "duration": 10,
        "players_min": 10,
        "intensity": "moyenne",
        "title_fr": "Possession 5v5 zones calmes",
        "title_nl": "Balbezit 5v5 rustige zones",
        "objective_fr": "Intégrer intensité progressive, reconnaissance espaces libres, transitions douces.",
        "objective_nl": "Progressieve intensiteit, herkenning van vrije ruimtes, zachte transities.",
        "setup_fr": "Terrain futsal complet ou moitié. 2 équipes de 5, jeu en 2 touches max. Pas de gardien.",
        "setup_nl": "Volledig futsalveld of helft. 2 teams van 5, max 2 contacten. Geen keeper.",
        "instructions_fr": [
            "Conserver la balle, objectif : 10 passes d'affilée = 1 point.",
            "Pas de tir, pas de duel dur, intensité 70 %.",
            "Privilégier décrochage et prise d'espace.",
            "Coach introduit progressivement la pression au bout de 4 min.",
            "Finir avec 2 min intensité match pour basculer vers la phase principale."
        ],
        "instructions_nl": [
            "Balbezit houden, doel: 10 passes op rij = 1 punt.",
            "Geen schot, geen hard duel, intensiteit 70 %.",
            "Focus op inzakken en ruimte innemen.",
            "Coach voert druk geleidelijk op na 4 min.",
            "Afsluiten met 2 min wedstrijdtempo om over te gaan op hoofdfase."
        ],
        "variants_fr": [
            "Réduire à 4v4 + 1 joker neutre qui aide le porteur.",
            "Ajouter règle : pas 2 passes de suite entre mêmes joueurs."
        ],
        "variants_nl": [
            "Verklein naar 4v4 + 1 neutrale joker die balbezitter helpt.",
            "Regel: geen 2 passes op rij tussen dezelfde spelers."
        ],
        "source": "FIFA Futsal Coaching Manual (2022), ch.6 — Possession",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "player", "team": "red", "pos": [10, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [14, 14], "label": "2"},
                {"type": "player", "team": "red", "pos": [14, 6], "label": "3"},
                {"type": "player", "team": "red", "pos": [18, 10], "label": "4"},
                {"type": "player", "team": "red", "pos": [8, 10], "label": "5"},
                {"type": "player", "team": "blue", "pos": [25, 10], "label": "1"},
                {"type": "player", "team": "blue", "pos": [28, 14], "label": "2"},
                {"type": "player", "team": "blue", "pos": [28, 6], "label": "3"},
                {"type": "player", "team": "blue", "pos": [32, 10], "label": "4"},
                {"type": "player", "team": "blue", "pos": [22, 10], "label": "5"},
                {"type": "ball", "pos": [14, 14]},
                {"type": "arrow", "from": [14, 14], "to": [18, 10], "kind": "ball"},
                {"type": "arrow", "from": [18, 10], "to": [14, 6], "kind": "ball"}
            ]
        }
    }
])
