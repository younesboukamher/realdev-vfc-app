"""
Futsal pitch renderer — produces 800x400 PNG diagrams from a simple DSL.
Pitch: 40m x 20m (standard futsal FIFA dimensions 38-42 x 18-22).
Coordinate system: x in [0,40], y in [0,20], origin bottom-left.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrow, Circle, Rectangle, Wedge, Arc
import numpy as np
from pathlib import Path

# ── Style constants ──────────────────────────────────────────────
PITCH_COLOR = '#1f7a3a'      # dark green
PITCH_EDGE  = '#f5f5f5'      # off-white lines
GOAL_AREA   = '#ffffff22'    # semi-transparent white
CENTER_MARK = '#f5f5f5'
RED_ATTACK  = '#e53935'      # attackers
BLUE_DEFEND = '#1976d2'      # defenders
YELLOW_NEUTRAL = '#fbc02d'   # neutrals / GK / bonus team
BALL_COLOR  = '#000000'
CONE_COLOR  = '#ff6f00'
ARROW_BALL  = '#000000'
ARROW_OFF   = '#e53935'
ARROW_DEF   = '#ffffff'
ZONE_COLOR  = '#ffeb3b22'    # light yellow zone

def draw_pitch(ax, half=False, third=False):
    """Draw the futsal pitch background."""
    if third:
        width = 40/3
    elif half:
        width = 20
    else:
        width = 40
    height = 20

    # Green background
    ax.add_patch(Rectangle((0, 0), width, height, facecolor=PITCH_COLOR, edgecolor='none', zorder=0))

    # Outer boundary
    ax.add_patch(Rectangle((0, 0), width, height, fill=False, edgecolor=PITCH_EDGE, linewidth=2, zorder=1))

    if not half and not third:
        # Halfway line
        ax.plot([20, 20], [0, 20], color=PITCH_EDGE, linewidth=1.5, zorder=1)
        # Center circle
        ax.add_patch(Circle((20, 10), 3, fill=False, edgecolor=PITCH_EDGE, linewidth=1.5, zorder=1))
        # Center spot
        ax.add_patch(Circle((20, 10), 0.2, facecolor=PITCH_EDGE, edgecolor='none', zorder=1))

    # Goal areas (6m semi-circle from goalposts — simplified as rectangle here for readability)
    goal_depth = 6
    goal_width = 3

    if not third or (third and width >= 20):
        # Left goal + goal area
        ax.add_patch(Rectangle((-1, 10 - goal_width/2), 1, goal_width, fill=False, edgecolor=PITCH_EDGE, linewidth=2, zorder=1))
        # 6m semi-circle
        ax.add_patch(Wedge((0, 10), 6, -90, 90, fill=False, edgecolor=PITCH_EDGE, linewidth=1.5, zorder=1))
        # 10m second penalty mark
        ax.add_patch(Circle((10, 10), 0.15, facecolor=PITCH_EDGE, zorder=1))

    if not half and not third:
        # Right goal + goal area
        ax.add_patch(Rectangle((40, 10 - goal_width/2), 1, goal_width, fill=False, edgecolor=PITCH_EDGE, linewidth=2, zorder=1))
        ax.add_patch(Wedge((40, 10), 6, 90, 270, fill=False, edgecolor=PITCH_EDGE, linewidth=1.5, zorder=1))
        ax.add_patch(Circle((30, 10), 0.15, facecolor=PITCH_EDGE, zorder=1))
    elif half:
        # half pitch — left half only, right side is the midline
        pass

    # Set limits with margin for goals
    margin_x = 1.5 if (not third or width >= 20) else 0.2
    ax.set_xlim(-margin_x, width + (1.5 if not half and not third else 0.2))
    ax.set_ylim(-0.5, height + 0.5)
    ax.set_aspect('equal')
    ax.axis('off')


def add_player(ax, x, y, team='red', label=None, size=0.9):
    """Add a player marker."""
    color = RED_ATTACK if team == 'red' else (BLUE_DEFEND if team == 'blue' else YELLOW_NEUTRAL)
    edge  = '#111' if team != 'blue' else '#fff'
    ax.add_patch(Circle((x, y), size, facecolor=color, edgecolor=edge, linewidth=1.5, zorder=5))
    if label:
        ax.text(x, y, str(label), ha='center', va='center',
                fontsize=10, fontweight='bold',
                color='#ffffff' if team == 'blue' else '#000000', zorder=6)


def add_gk(ax, x, y, label='GK'):
    """Goalkeeper — yellow with black outline."""
    add_player(ax, x, y, team='yellow', label=label, size=1.0)


def add_ball(ax, x, y, size=0.45):
    """Add a ball marker."""
    ax.add_patch(Circle((x, y), size, facecolor=BALL_COLOR, edgecolor='#ffffff', linewidth=1.5, zorder=7))
    # white pentagon hint
    ax.add_patch(Circle((x, y), size*0.4, facecolor='#ffffff', edgecolor='none', zorder=8))


def add_cone(ax, x, y):
    """Add a cone marker (small triangle)."""
    tri = plt.Polygon([(x, y+0.7), (x-0.5, y-0.4), (x+0.5, y-0.4)],
                      facecolor=CONE_COLOR, edgecolor='#000', linewidth=0.8, zorder=4)
    ax.add_patch(tri)


def add_arrow(ax, x1, y1, x2, y2, kind='ball', style='solid'):
    """
    Add an arrow.
    kind: 'ball' (black, solid), 'offense' (red, solid), 'defense' (white, dashed), 'pass' (black, dashed)
    """
    colors = {'ball': ARROW_BALL, 'offense': ARROW_OFF, 'defense': ARROW_DEF, 'pass': ARROW_BALL}
    styles = {'ball': 'solid', 'offense': 'solid', 'defense': (0, (4, 2)), 'pass': (0, (1.5, 1.5))}
    linestyle = styles.get(kind, 'solid')
    color = colors.get(kind, '#000')
    # calculate arrow
    dx = x2 - x1
    dy = y2 - y1
    length = (dx**2 + dy**2) ** 0.5
    if length < 0.1:
        return
    # shorten to avoid overlap with markers
    shrink = 1.0
    ux, uy = dx / length, dy / length
    x1b, y1b = x1 + ux * shrink, y1 + uy * shrink
    x2b, y2b = x2 - ux * shrink, y2 - uy * shrink
    ax.annotate('', xy=(x2b, y2b), xytext=(x1b, y1b),
                arrowprops=dict(arrowstyle='-|>', color=color, lw=2.2,
                                linestyle=linestyle,
                                mutation_scale=18),
                zorder=9)


def add_zone(ax, x, y, w, h, color=ZONE_COLOR, label=None):
    """Highlight a rectangular zone."""
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor='#ffeb3b', linewidth=1.5, linestyle=':', zorder=2))
    if label:
        ax.text(x + w/2, y + h/2, label, ha='center', va='center',
                fontsize=9, color='#ffeb3b', fontweight='bold', zorder=3)


def render_diagram(spec, output_path, title=None):
    """
    Render a diagram from a spec dict.
    spec = {
        'pitch': 'full' | 'half' | 'third',
        'elements': [
            {'type': 'player', 'team': 'red', 'pos': [x, y], 'label': 'A1'},
            {'type': 'gk', 'pos': [x, y], 'label': 'GK'},
            {'type': 'ball', 'pos': [x, y]},
            {'type': 'cone', 'pos': [x, y]},
            {'type': 'arrow', 'from': [x1, y1], 'to': [x2, y2], 'kind': 'ball'|'offense'|'defense'|'pass'},
            {'type': 'zone', 'pos': [x, y], 'size': [w, h], 'label': 'Zone A'},
        ]
    }
    """
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    pitch_type = spec.get('pitch', 'full')
    draw_pitch(ax, half=(pitch_type=='half'), third=(pitch_type=='third'))

    for el in spec.get('elements', []):
        t = el.get('type')
        if t == 'player':
            add_player(ax, el['pos'][0], el['pos'][1],
                      team=el.get('team', 'red'),
                      label=el.get('label'),
                      size=el.get('size', 0.9))
        elif t == 'gk':
            add_gk(ax, el['pos'][0], el['pos'][1], label=el.get('label', 'GK'))
        elif t == 'ball':
            add_ball(ax, el['pos'][0], el['pos'][1], size=el.get('size', 0.45))
        elif t == 'cone':
            add_cone(ax, el['pos'][0], el['pos'][1])
        elif t == 'arrow':
            add_arrow(ax, el['from'][0], el['from'][1], el['to'][0], el['to'][1],
                      kind=el.get('kind', 'ball'))
        elif t == 'zone':
            add_zone(ax, el['pos'][0], el['pos'][1],
                     el['size'][0], el['size'][1],
                     color=el.get('color', ZONE_COLOR),
                     label=el.get('label'))

    if title:
        ax.set_title(title, fontsize=11, fontweight='bold', color='#111', pad=4)

    fig.patch.set_facecolor('#ffffff')
    plt.tight_layout(pad=0.3)
    fig.savefig(output_path, dpi=100, bbox_inches='tight', facecolor='#ffffff', edgecolor='none')
    plt.close(fig)


if __name__ == '__main__':
    # Test with a sample diagram
    sample = {
        'pitch': 'full',
        'elements': [
            {'type': 'gk', 'pos': [0.5, 10], 'label': 'GK'},
            {'type': 'player', 'team': 'red', 'pos': [8, 6], 'label': 'F'},
            {'type': 'player', 'team': 'red', 'pos': [8, 14], 'label': 'F'},
            {'type': 'player', 'team': 'red', 'pos': [14, 10], 'label': 'A'},
            {'type': 'player', 'team': 'blue', 'pos': [25, 10], 'label': 'D'},
            {'type': 'player', 'team': 'blue', 'pos': [30, 7], 'label': 'D'},
            {'type': 'ball', 'pos': [1.5, 10]},
            {'type': 'arrow', 'from': [1.5, 10], 'to': [8, 6], 'kind': 'ball'},
            {'type': 'arrow', 'from': [8, 6], 'to': [14, 10], 'kind': 'offense'},
        ]
    }
    render_diagram(sample, '/tmp/realdev-vfc-app/exercises/_sample.png', title='Sample diagram')
    print('Sample rendered:', Path('/tmp/realdev-vfc-app/exercises/_sample.png').stat().st_size, 'bytes')
