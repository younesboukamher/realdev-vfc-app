#\!/usr/bin/env python3
"""
Build script: generates exercises/*.png (80 diagrams) and data/exercises.json.
"""
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pitch_renderer import render_diagram
from ex_01_warmup import WARMUPS
from ex_02_technique import TECHNIQUE
from ex_03_tactique import TACTIQUE
from ex_04_ssg import SSG
from ex_05_finition import FINITION
from ex_06_setpieces import SETPIECES
from ex_07_defense import DEFENSE
from ex_08_gardien import GARDIEN
from ex_09_prevention import PREVENTION

ALL = WARMUPS + TECHNIQUE + TACTIQUE + SSG + FINITION + SETPIECES + DEFENSE + GARDIEN + PREVENTION

ROOT = Path('/tmp/realdev-vfc-app')
EX_DIR = ROOT / 'exercises'
DATA_DIR = ROOT / 'data'
EX_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)


def main():
    print(f'Total exercises: {len(ALL)}')
    assert len(ALL) == 80, f'Expected 80 exercises, got {len(ALL)}'

    # Check IDs are unique
    ids = [e['id'] for e in ALL]
    assert len(ids) == len(set(ids)), 'Duplicate IDs'

    # Generate PNG for each exercise
    generated = 0
    for ex in ALL:
        ex_id = ex['id']
        diagram = ex.get('diagram')
        if not diagram:
            print(f'  [skip] {ex_id}: no diagram spec')
            continue
        png_path = EX_DIR / f'{ex_id}.png'
        try:
            render_diagram(diagram, str(png_path), title=ex.get('title_fr'))
            generated += 1
        except Exception as e:
            print(f'  [error] {ex_id}: {e}')

    print(f'Generated {generated} PNG files in {EX_DIR}')

    # Build exercises.json (without diagram specs — those are build-time only)
    json_items = []
    for ex in ALL:
        item = {
            'id': ex['id'],
            'category': ex['category'],
            'subcategory': ex.get('subcategory', ''),
            'age_range': ex.get('age_range', ''),
            'duration': ex['duration'],
            'players_min': ex['players_min'],
            'intensity': ex.get('intensity', ''),
            'title_fr': ex['title_fr'],
            'title_nl': ex['title_nl'],
            'objective_fr': ex['objective_fr'],
            'objective_nl': ex['objective_nl'],
            'setup_fr': ex['setup_fr'],
            'setup_nl': ex['setup_nl'],
            'instructions_fr': ex['instructions_fr'],
            'instructions_nl': ex['instructions_nl'],
            'variants_fr': ex.get('variants_fr', []),
            'variants_nl': ex.get('variants_nl', []),
            'source': ex.get('source', ''),
            'image_url': f'exercises/{ex["id"]}.png',
        }
        json_items.append(item)

    # Build categories metadata
    categories = [
        {'key': 'warmup', 'label_fr': 'Échauffement', 'label_nl': 'Opwarming'},
        {'key': 'technique', 'label_fr': 'Technique', 'label_nl': 'Techniek'},
        {'key': 'tactique', 'label_fr': 'Tactique', 'label_nl': 'Tactiek'},
        {'key': 'ssg', 'label_fr': 'Jeu réduit', 'label_nl': 'Klein spel'},
        {'key': 'finition', 'label_fr': 'Finition', 'label_nl': 'Afwerking'},
        {'key': 'setpieces', 'label_fr': 'Coups arrêtés', 'label_nl': 'Standaardsituaties'},
        {'key': 'defense', 'label_fr': 'Défense', 'label_nl': 'Verdediging'},
        {'key': 'gardien', 'label_fr': 'Gardien', 'label_nl': 'Keeper'},
        {'key': 'prevention', 'label_fr': 'Prévention', 'label_nl': 'Preventie'},
    ]

    payload = {
        'version': '1.0.0',
        'generated_count': len(json_items),
        'categories': categories,
        'exercises': json_items,
    }

    json_path = DATA_DIR / 'exercises.json'
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Wrote {json_path} ({json_path.stat().st_size} bytes)')

    # Stats per category
    from collections import Counter
    stats = Counter(e['category'] for e in ALL)
    print('\nPer category:')
    for cat, n in sorted(stats.items()):
        print(f'  {cat:15s} {n}')


if __name__ == '__main__':
    main()
