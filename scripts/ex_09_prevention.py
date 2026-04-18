"""Prevention (4) — prevention and activation."""

PREVENTION = [
    {
        "id": "pv-01",
        "category": "prevention",
        "subcategory": "chevilles",
        "age_range": "U11-Senior",
        "duration": 8,
        "players_min": 1,
        "intensity": "faible",
        "title_fr": "Proprioception chevilles",
        "title_nl": "Proprioceptie enkels",
        "objective_fr": "Prévenir entorses par renforcement neuromusculaire des chevilles.",
        "objective_nl": "Verstuikingen voorkomen door neuromusculaire versterking van enkels.",
        "setup_fr": "1 coussin ou bosu par joueur (ou surface instable). Mur à proximité pour appui.",
        "setup_nl": "1 kussen of bosu per speler (of onstabiel oppervlak). Muur dichtbij voor steun.",
        "instructions_fr": [
            "Appui 1 pied 30 s chaque côté, yeux ouverts.",
            "Idem yeux fermés.",
            "Appui 1 pied + lancer/rattraper ballon.",
            "Appui 1 pied + petites flexions genou.",
            "Progression : ajouter déséquilibre par partenaire."
        ],
        "instructions_nl": [
            "Sta op 1 voet 30 s elke kant, ogen open.",
            "Idem ogen dicht.",
            "1 voet + bal gooien/vangen.",
            "1 voet + kleine kniebuigingen.",
            "Progressie: partner verstoort balans."
        ],
        "variants_fr": [
            "Enchaîner 3 exercices sans poser pied.",
            "Faire en session récupération également."
        ],
        "variants_nl": [
            "3 oefeningen aan elkaar zonder voet neerzetten.",
            "Ook in hersteltraining opnemen."
        ],
        "source": "FIFA 11+ / UEFA Medical Committee",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "cone", "pos": [4, 10]},
                {"type": "cone", "pos": [7, 10]},
                {"type": "cone", "pos": [10, 10]},
                {"type": "player", "team": "red", "pos": [4, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [7, 10], "label": "2"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "3"}
            ]
        }
    },
    {
        "id": "pv-02",
        "category": "prevention",
        "subcategory": "core",
        "age_range": "U11-Senior",
        "duration": 10,
        "players_min": 1,
        "intensity": "moyenne",
        "title_fr": "Gainage dynamique 360°",
        "title_nl": "Dynamische core 360°",
        "objective_fr": "Renforcer ceinture abdo-lombaire pour stabilité dans duels.",
        "objective_nl": "Kern versterken voor stabiliteit in duels.",
        "setup_fr": "Tapis ou surface propre. 1 ballon optionnel.",
        "setup_nl": "Mat of schone ondergrond. 1 bal optioneel.",
        "instructions_fr": [
            "Planche frontale 30 s.",
            "Planche latérale gauche 30 s, puis droite.",
            "Planche + levée de bras alternée 30 s.",
            "Pont + extension jambe 30 s.",
            "2 tours complets, 30 s récupération entre tours."
        ],
        "instructions_nl": [
            "Voorwaartse plank 30 s.",
            "Zijplank links 30 s, dan rechts.",
            "Plank + afwisselend arm opheffen 30 s.",
            "Bruggetje + been strekken 30 s.",
            "2 volledige rondes, 30 s pauze tussen rondes."
        ],
        "variants_fr": [
            "Passer à 45 s par position.",
            "Ajouter ballon à bout de bras."
        ],
        "variants_nl": [
            "Verlengen naar 45 s per positie.",
            "Bal aan gestrekte armen toevoegen."
        ],
        "source": "FIFA 11+, Core module",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [4, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [7, 10], "label": "2"},
                {"type": "player", "team": "red", "pos": [10, 10], "label": "3"}
            ]
        }
    },
    {
        "id": "pv-03",
        "category": "prevention",
        "subcategory": "ischios",
        "age_range": "U13-Senior",
        "duration": 8,
        "players_min": 2,
        "intensity": "moyenne",
        "title_fr": "Nordic hamstring + activation",
        "title_nl": "Nordic hamstring + activatie",
        "objective_fr": "Prévenir blessures ischio-jambiers par travail excentrique.",
        "objective_nl": "Hamstringblessures voorkomen door excentrisch werk.",
        "setup_fr": "Paires, 1 joueur à genoux, 1 partenaire tient les chevilles.",
        "setup_nl": "Paren, 1 speler op knieën, 1 partner houdt enkels vast.",
        "instructions_fr": [
            "Joueur en position agenouillée, tronc droit.",
            "Se laisser tomber en avant en contrôlant la descente (excentrique).",
            "Rattraper avec mains le plus bas possible, revenir en poussant.",
            "5 répétitions, 3 séries.",
            "Compléter : 30 s étirements dynamiques ischios."
        ],
        "instructions_nl": [
            "Speler knielt, romp rechtop.",
            "Voorwaarts laten vallen met controle (excentrisch).",
            "Zo laag mogelijk met handen opvangen, duw terug omhoog.",
            "5 herhalingen, 3 series.",
            "Aanvullen: 30 s dynamische rek hamstrings."
        ],
        "variants_fr": [
            "Augmenter à 6-8 répétitions.",
            "Placer élastique pour assistance."
        ],
        "variants_nl": [
            "Verhogen naar 6-8 herhalingen.",
            "Elastiek ter ondersteuning."
        ],
        "source": "FIFA 11+ / Nordic hamstring exercise",
        "diagram": {
            "pitch": "third",
            "elements": [
                {"type": "player", "team": "red", "pos": [4, 10], "label": "A"},
                {"type": "player", "team": "red", "pos": [5.5, 10], "label": "B"},
                {"type": "player", "team": "red", "pos": [9, 10], "label": "C"},
                {"type": "player", "team": "red", "pos": [10.5, 10], "label": "D"}
            ]
        }
    },
    {
        "id": "pv-04",
        "category": "prevention",
        "subcategory": "activation neurale",
        "age_range": "U11-Senior",
        "duration": 6,
        "players_min": 4,
        "intensity": "moyenne",
        "title_fr": "Activation neuromusculaire pré-match",
        "title_nl": "Neuromusculaire activatie voor wedstrijd",
        "objective_fr": "Préparer tissu neural et musculaire pour l'effort à venir.",
        "objective_nl": "Neurologisch en musculair weefsel voorbereiden op inspanning.",
        "setup_fr": "Zone 20×10 m. Pas de ballon.",
        "setup_nl": "Zone 20×10 m. Geen bal.",
        "instructions_fr": [
            "Talons-fesses 20 m, aller-retour 2 fois.",
            "Montées de genoux 20 m, aller-retour 2 fois.",
            "Pas chassés latéraux 20 m, alterner côtés.",
            "Accélérations progressives 20 m : 50, 70, 85 % VMA.",
            "3 x 10 squats dynamiques."
        ],
        "instructions_nl": [
            "Hakken-billen 20 m, heen en terug 2 x.",
            "Knieheffen 20 m, heen en terug 2 x.",
            "Zijwaartse chassé 20 m, kanten afwisselen.",
            "Progressieve versnellingen 20 m: 50, 70, 85 % max.",
            "3 x 10 dynamische squats."
        ],
        "variants_fr": [
            "Ajouter 5 min FIFA 11+ si pré-match officiel.",
            "Terminer par 2 sprints max sur 15 m."
        ],
        "variants_nl": [
            "5 min FIFA 11+ bij officiële match.",
            "Afsluiten met 2 max sprints over 15 m."
        ],
        "source": "FIFA 11+ / UEFA pre-match activation",
        "diagram": {
            "pitch": "full",
            "elements": [
                {"type": "cone", "pos": [5, 10]},
                {"type": "cone", "pos": [25, 10]},
                {"type": "player", "team": "red", "pos": [3, 10], "label": "1"},
                {"type": "player", "team": "red", "pos": [3, 11], "label": "2"},
                {"type": "player", "team": "red", "pos": [3, 12], "label": "3"},
                {"type": "player", "team": "red", "pos": [3, 13], "label": "4"},
                {"type": "arrow", "from": [3, 10], "to": [25, 10], "kind": "offense"}
            ]
        }
    }
]
