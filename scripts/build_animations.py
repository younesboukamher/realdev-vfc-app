#!/usr/bin/env python3
"""
RealDev Vilvoorde - Animation builder (Phase 1.5)

Reads `animation` field from data/exercises.json and emits one SVG per
selected exo to data/animations/{id}.svg.

Run modes:
    python build_animations.py --inject   # write ANIMATIONS into exercises.json
    python build_animations.py --generate # read exercises.json, write SVGs
    python build_animations.py --all      # inject then generate

SVG format: viewBox 1200 x 680 (pitch 1200x600 + legend strip 80px below).
CSS @keyframes drive a 5 s infinite loop:
  0-10% rest, 10-25% arrows draw, 25-55% players/ball translate,
  55-75% zone pulse + hold, 75-85% fade back, 85-100% rest.
Respects prefers-reduced-motion: reduce (static final state, no animation).
"""
import json, math, os, sys, argparse, html as _html

def xe(s):
    """Escape text for XML content/attributes."""
    if s is None: return ''
    return _html.escape(str(s), quote=True)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXOS_JSON = os.path.join(ROOT, 'data', 'exercises.json')
OUT_DIR = os.path.join(ROOT, 'data', 'animations')

# Pitch -> SVG (40 m x 20 m pitch, 1200 x 600 px)
W, H, S = 1200, 600, 30
def sx(x): return x * S
def sy(y): return H - y * S

PITCH_DARK = '#0c6b3a'
PITCH_ALT  = '#0d7340'
RED_C      = '#c62828'
BLUE_C     = '#1565c0'
YELLOW_C   = '#f9a825'
NEUTRAL_C  = '#6a1b9a'  # jokers
TEXT_DARK  = '#1a1a1a'

ZONE_COLORS = {
    'red':    RED_C,
    'blue':   BLUE_C,
    'yellow': YELLOW_C,
    'neutral': NEUTRAL_C,
}

# ==== ANIMATION SEQUENCES (21 exos) ============================================
# Pitch coord: x in [0..40] (length), y in [0..20] (width). y=0 is "south"
# (bottom of SVG), y=20 is "north" (top of SVG).

ANIMATIONS = {
  # --- TACTIQUE (9) ---
  'ta-01': {
    'duration_ms': 5000,
    'caption_fr': "Rotation losange: chaque joueur passe et court vers le sommet suivant.",
    'caption_nl': "Ruiten-rotatie: passen en lopen naar volgende hoek.",
    'players': [
      {'team':'blue','label':'1','from':[15,10],'to':[20,15]},
      {'team':'blue','label':'2','from':[20,15],'to':[25,10]},
      {'team':'blue','label':'3','from':[25,10],'to':[20,5]},
      {'team':'blue','label':'4','from':[20,5],'to':[15,10]},
    ],
    'ball': {'from':[15,10],'to':[20,15]},
    'arrows':[
      {'kind':'run','from':[15,10],'to':[20,15],'rad':0.18,'color':'blue'},
      {'kind':'run','from':[20,15],'to':[25,10],'rad':0.18,'color':'blue'},
      {'kind':'run','from':[25,10],'to':[20,5],'rad':0.18,'color':'blue'},
      {'kind':'run','from':[20,5],'to':[15,10],'rad':0.18,'color':'blue'},
      {'kind':'pass','from':[15,10],'to':[20,15],'rad':-0.10,'color':'yellow'},
    ],
  },
  'ta-02': {
    'duration_ms': 5000,
    'caption_fr': "2v1: l'appui fixe le defenseur, passe decisive, finition.",
    'caption_nl': "2v1: aanspeelpunt bindt verdediger, pass, afwerking.",
    'players': [
      {'team':'blue','label':'1','from':[10,10],'to':[22,10]},
      {'team':'blue','label':'2','from':[10,15],'to':[26,8]},
      {'team':'red','label':'D','from':[28,10],'to':[23,10]},
      {'team':'red','label':'G','from':[38,10]},
    ],
    'ball': {'from':[10,10],'to':[26,8]},
    'arrows':[
      {'kind':'run','from':[10,10],'to':[22,10],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[10,15],'to':[26,8],'rad':-0.15,'color':'blue'},
      {'kind':'pass','from':[22,10],'to':[26,8],'rad':-0.05,'color':'yellow'},
    ],
  },
  'ta-03': {
    'duration_ms': 5000,
    'caption_fr': "3v2: pivot au centre, courses en largeur + profondeur, passe decalee.",
    'caption_nl': "3v2: pivot centraal, diepte+breedte looplijnen, doorgeefpass.",
    'players': [
      {'team':'blue','label':'1','from':[15,10]},
      {'team':'blue','label':'2','from':[15,5],'to':[25,3]},
      {'team':'blue','label':'3','from':[15,15],'to':[25,17]},
      {'team':'red','label':'D','from':[25,8]},
      {'team':'red','label':'D','from':[25,12]},
    ],
    'ball': {'from':[15,10],'to':[25,17]},
    'arrows':[
      {'kind':'run','from':[15,5],'to':[25,3],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[15,15],'to':[25,17],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[15,10],'to':[25,17],'rad':0.2,'color':'yellow'},
    ],
  },
  'ta-04': {
    'duration_ms': 5000,
    'caption_fr': "Bloc 2-2: le quatuor defensif glisse ensemble pour garder la compacite.",
    'caption_nl': "Blok 2-2: viertal schuift samen om compact te blijven.",
    'players': [
      {'team':'blue','label':'1','from':[25,7],'to':[28,7]},
      {'team':'blue','label':'2','from':[25,13],'to':[28,13]},
      {'team':'blue','label':'3','from':[32,7],'to':[35,7]},
      {'team':'blue','label':'4','from':[32,13],'to':[35,13]},
      {'team':'red','label':'A','from':[15,10]},
      {'team':'red','label':'A','from':[15,17]},
    ],
    'ball': {'from':[15,10],'to':[15,17]},
    'arrows':[
      {'kind':'run','from':[25,7],'to':[28,7],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[25,13],'to':[28,13],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[32,7],'to':[35,7],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[32,13],'to':[35,13],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[15,10],'to':[15,17],'rad':0.0,'color':'yellow'},
    ],
  },
  'ta-05': {
    'duration_ms': 5000,
    'caption_fr': "Pressing haut 4v4+GK: rotation rouge, piege au 1er poteau, passe contrainte.",
    'caption_nl': "Hoge press 4v4+GK: rode rotatie, val bij 1e paal, passe gedwongen.",
    'zones':[
      {'type':'polygon','points':[[23.5,0.3],[33.5,0.3],[30.5,8],[23.5,8]],
       'color':'red','label':'PIEGE','pulse':True},
    ],
    'players': [
      # blue static
      {'team':'blue','label':'GK','from':[38,10]},
      {'team':'blue','label':'4','from':[31,10]},
      {'team':'blue','label':'2','from':[27.5,16]},
      {'team':'blue','label':'3','from':[27.5,4]},
      {'team':'blue','label':'1','from':[22,10]},
      # red animated
      {'team':'red','label':'GK','from':[2,10]},
      {'team':'red','label':'4','from':[26,10],'to':[29.3,10]},
      {'team':'red','label':'2','from':[22,15],'to':[25.3,15.3]},
      {'team':'red','label':'3','from':[22,5],'to':[26.3,4.3]},
      {'team':'red','label':'1','from':[17,10],'to':[20.3,10]},
    ],
    'ball': {'from':[31.2,9.4],'to':[27.5,4.7]},
    'arrows':[
      {'kind':'run','from':[26,10],'to':[29.3,10],'rad':0.08,'color':'red'},
      {'kind':'run','from':[22,5],'to':[26.3,4.3],'rad':-0.22,'color':'red'},
      {'kind':'run','from':[22,15],'to':[25.3,15.3],'rad':0.12,'color':'red'},
      {'kind':'run','from':[17,10],'to':[20.3,10],'rad':0.10,'color':'red'},
      {'kind':'pass','from':[31.2,9.4],'to':[27.5,4.7],'rad':-0.18,'color':'yellow'},
    ],
  },
  'ta-07': {
    'duration_ms': 5000,
    'caption_fr': "Transition: apres perte, 1 rouge en retard -> 4v3 favorable pour bleu.",
    'caption_nl': "Omschakeling: 1 rood te laat -> 4v3 voor blauw.",
    'players': [
      {'team':'blue','label':'1','from':[15,10],'to':[25,10]},
      {'team':'blue','label':'2','from':[15,5],'to':[28,5]},
      {'team':'blue','label':'3','from':[15,15],'to':[28,15]},
      {'team':'blue','label':'4','from':[10,10]},
      {'team':'red','label':'1','from':[20,10],'to':[15,10]},
      {'team':'red','label':'2','from':[22,5],'to':[18,5]},
      {'team':'red','label':'3','from':[22,15],'to':[18,15]},
      {'team':'red','label':'4','from':[25,10]},
    ],
    'ball': {'from':[20,10],'to':[27,10]},
    'arrows':[
      {'kind':'run','from':[15,10],'to':[25,10],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[15,5],'to':[28,5],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[15,15],'to':[28,15],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[20,10],'to':[15,10],'rad':0.0,'color':'red'},
      {'kind':'pass','from':[20,10],'to':[27,10],'rad':0.0,'color':'yellow'},
    ],
  },
  'ta-11': {
    'duration_ms': 5000,
    'caption_fr': "Para (pick & roll): bloc de 2, porteur passe l'ecran, rolleur plonge au but.",
    'caption_nl': "Para (pick & roll): blok, balvoerder gaat langs scherm, roller duikt naar goal.",
    'players': [
      {'team':'blue','label':'1','from':[15,8],'to':[25,8]},
      {'team':'blue','label':'2','from':[20,12],'to':[30,13]},
      {'team':'red','label':'D','from':[25,12]},
    ],
    'ball': {'from':[15,8],'to':[30,13]},
    'arrows':[
      {'kind':'run','from':[15,8],'to':[25,8],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[20,12],'to':[30,13],'rad':-0.10,'color':'blue'},
      {'kind':'pass','from':[25,8],'to':[30,13],'rad':0.10,'color':'yellow'},
    ],
  },
  'ta-12': {
    'duration_ms': 5000,
    'caption_fr': "Relance 4v3: decrochages lateraux, triangle pour sortir du pressing.",
    'caption_nl': "Opbouw 4v3: lateraal terugzakken, driehoek om pressing te omzeilen.",
    'players': [
      {'team':'blue','label':'GK','from':[3,10]},
      {'team':'blue','label':'1','from':[6,10],'to':[5,7]},
      {'team':'blue','label':'2','from':[10,6],'to':[12,4]},
      {'team':'blue','label':'3','from':[10,14]},
      {'team':'red','label':'P','from':[10,10]},
      {'team':'red','label':'P','from':[12,6]},
      {'team':'red','label':'P','from':[12,14]},
    ],
    'ball': {'from':[3,10],'to':[12,4]},
    'arrows':[
      {'kind':'run','from':[6,10],'to':[5,7],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[10,6],'to':[12,4],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[3,10],'to':[5,7],'rad':0.0,'color':'yellow'},
      {'kind':'pass','from':[5,7],'to':[12,4],'rad':-0.05,'color':'yellow'},
    ],
  },
  'ta-15': {
    'duration_ms': 5000,
    'caption_fr': "Power play 5v4: rotation peripherique, B3 plonge pour ouvrir l'angle.",
    'caption_nl': "Power play 5v4: buitenrotatie, B3 duikt om hoek te openen.",
    'players': [
      {'team':'blue','label':'1','from':[15,10]},
      {'team':'blue','label':'2','from':[20,5]},
      {'team':'blue','label':'3','from':[20,15],'to':[28,15]},
      {'team':'blue','label':'4','from':[25,5],'to':[28,5]},
      {'team':'blue','label':'J','from':[25,15]},
      {'team':'red','label':'D','from':[30,5]},
      {'team':'red','label':'D','from':[30,15]},
      {'team':'red','label':'D','from':[33,10]},
      {'team':'red','label':'GK','from':[38,10]},
    ],
    'ball': {'from':[15,10],'to':[28,15]},
    'arrows':[
      {'kind':'run','from':[20,15],'to':[28,15],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[25,5],'to':[28,5],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[15,10],'to':[28,15],'rad':0.15,'color':'yellow'},
    ],
  },

  # --- SSG (4) ---
  'sg-01': {
    'duration_ms': 5000,
    'caption_fr': "4v4 3 zones: ball-vers-l'avant oblige les porteurs a accompagner.",
    'caption_nl': "4v4 3 zones: bal vooruit dwingt ballvoerders mee te schuiven.",
    'zones':[
      {'type':'polygon','points':[[0,0],[13.3,0],[13.3,20],[0,20]],
       'color':'blue','label':'DEF','pulse':False},
      {'type':'polygon','points':[[26.7,0],[40,0],[40,20],[26.7,20]],
       'color':'red','label':'ATT','pulse':False},
    ],
    'players': [
      {'team':'blue','label':'1','from':[8,10],'to':[14,10]},
      {'team':'blue','label':'2','from':[18,7],'to':[22,7]},
      {'team':'blue','label':'3','from':[18,13],'to':[22,13]},
      {'team':'blue','label':'4','from':[30,10]},
    ],
    'ball': {'from':[8,10],'to':[30,10]},
    'arrows':[
      {'kind':'run','from':[8,10],'to':[14,10],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[8,10],'to':[18,7],'rad':0.1,'color':'yellow'},
      {'kind':'pass','from':[18,7],'to':[30,10],'rad':0.0,'color':'yellow'},
    ],
  },
  'sg-03': {
    'duration_ms': 5000,
    'caption_fr': "3v3 + 2 jokers: toujours 4v3 offensif via les jokers neutres.",
    'caption_nl': "3v3 + 2 jokers: altijd 4v3 aanvallend dankzij neutrale jokers.",
    'players': [
      {'team':'blue','label':'1','from':[10,10]},
      {'team':'blue','label':'2','from':[15,5]},
      {'team':'blue','label':'3','from':[15,15]},
      {'team':'red','label':'D','from':[25,10]},
      {'team':'red','label':'D','from':[30,5]},
      {'team':'red','label':'D','from':[30,15]},
      {'team':'neutral','label':'J','from':[20,6]},
      {'team':'neutral','label':'J','from':[20,14]},
    ],
    'ball': {'from':[10,10],'to':[15,5]},
    'arrows':[
      {'kind':'pass','from':[10,10],'to':[20,6],'rad':-0.1,'color':'yellow'},
      {'kind':'pass','from':[20,6],'to':[15,5],'rad':0.0,'color':'yellow'},
    ],
  },
  'sg-06': {
    'duration_ms': 5000,
    'caption_fr': "Zone interdite de tir: trouver l'appui exterieur, renversement + frappe.",
    'caption_nl': "Schietzone verboden: buitenaanspeelpunt, overspelen + schot.",
    'zones':[
      {'type':'polygon','points':[[15,5],[30,5],[30,15],[15,15]],
       'color':'red','label':'NO TIR','pulse':True},
    ],
    'players': [
      {'team':'blue','label':'1','from':[22,10]},
      {'team':'blue','label':'2','from':[8,10]},
      {'team':'red','label':'D','from':[25,10]},
      {'team':'red','label':'GK','from':[38,10]},
    ],
    'ball': {'from':[22,10],'to':[8,10]},
    'arrows':[
      {'kind':'pass','from':[22,10],'to':[8,10],'rad':0.0,'color':'yellow'},
      {'kind':'pass','from':[8,10],'to':[34,10],'rad':0.0,'color':'yellow'},
    ],
  },
  'sg-07': {
    'duration_ms': 5000,
    'caption_fr': "Regle des couloirs: switch droite -> gauche par relais central.",
    'caption_nl': "Zone-regel: switch rechts -> links via centrale relais.",
    'zones':[
      {'type':'polygon','points':[[0,0],[40,0],[40,7],[0,7]],
       'color':'yellow','label':'','pulse':False},
      {'type':'polygon','points':[[0,13],[40,13],[40,20],[0,20]],
       'color':'yellow','label':'','pulse':False},
    ],
    'players': [
      {'team':'blue','label':'1','from':[15,4]},
      {'team':'blue','label':'2','from':[20,10]},
      {'team':'blue','label':'3','from':[15,16]},
      {'team':'blue','label':'4','from':[28,10]},
    ],
    'ball': {'from':[15,4],'to':[15,16]},
    'arrows':[
      {'kind':'pass','from':[15,4],'to':[20,10],'rad':0.0,'color':'yellow'},
      {'kind':'pass','from':[20,10],'to':[15,16],'rad':0.0,'color':'yellow'},
    ],
  },

  # --- SET PIECES (3) ---
  'sp-01': {
    'duration_ms': 5000,
    'caption_fr': "Corner combine 1er poteau: runner coupe devant, decoy tire le 2e poteau.",
    'caption_nl': "Hoekcombinatie 1e paal: korte loper snijdt, decoy op 2e paal.",
    'players': [
      {'team':'blue','label':'K','from':[39.5,0.5]},
      {'team':'blue','label':'R','from':[35,5],'to':[37.5,2.5]},
      {'team':'blue','label':'D','from':[35,15],'to':[37.5,17]},
      {'team':'red','label':'D','from':[36,5]},
      {'team':'red','label':'D','from':[36,15]},
      {'team':'red','label':'GK','from':[39.5,10]},
    ],
    'ball': {'from':[39.5,0.5],'to':[37.5,2.5]},
    'arrows':[
      {'kind':'run','from':[35,5],'to':[37.5,2.5],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[35,15],'to':[37.5,17],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[39.5,0.5],'to':[37.5,2.5],'rad':-0.10,'color':'yellow'},
    ],
  },
  'sp-02': {
    'duration_ms': 5000,
    'caption_fr': "CFI: passe courte au pivot, remise en une touche au joueur lance.",
    'caption_nl': "Indirecte vrije trap: korte pass naar pivot, one-touch afhandeling.",
    'players': [
      {'team':'blue','label':'K','from':[25,2]},
      {'team':'blue','label':'P','from':[25,10]},
      {'team':'blue','label':'R','from':[30,5],'to':[33,7]},
      {'team':'red','label':'M','from':[28,2]},
      {'team':'red','label':'M','from':[28,3.3]},
      {'team':'red','label':'M','from':[28,4.6]},
      {'team':'red','label':'GK','from':[39.5,10]},
    ],
    'ball': {'from':[25,2],'to':[33,7]},
    'arrows':[
      {'kind':'run','from':[30,5],'to':[33,7],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[25,2],'to':[25,10],'rad':0.0,'color':'yellow'},
      {'kind':'pass','from':[25,10],'to':[33,7],'rad':0.0,'color':'yellow'},
    ],
  },
  'sp-06': {
    'duration_ms': 5000,
    'caption_fr': "Mur defensif: 4 joueurs alignes, GK couvre le poteau decouvert.",
    'caption_nl': "Defensieve muur: 4 op een lijn, GK dekt onbeschermde paal.",
    'zones':[
      {'type':'polygon','points':[[24,7.5],[26,7.5],[26,12.5],[24,12.5]],
       'color':'blue','label':'MUR','pulse':True},
    ],
    'players': [
      {'team':'red','label':'K','from':[20,10]},
      {'team':'blue','label':'M','from':[25,8],'to':[25,7.8]},
      {'team':'blue','label':'M','from':[25,9.3],'to':[25,9.1]},
      {'team':'blue','label':'M','from':[25,10.7],'to':[25,10.5]},
      {'team':'blue','label':'M','from':[25,12],'to':[25,11.8]},
      {'team':'blue','label':'GK','from':[38,6]},
    ],
    'arrows':[
      {'kind':'pass','from':[20,10],'to':[35,12],'rad':0.15,'color':'red'},
    ],
  },

  # --- FINITION (3) ---
  'fi-02': {
    'duration_ms': 5000,
    'caption_fr': "Appui-remise: passe au pivot, course du passeur, retour, frappe.",
    'caption_nl': "Aanspeel-teruggave: pass pivot, loop, retour, schot.",
    'players': [
      {'team':'blue','label':'1','from':[10,10],'to':[20,10]},
      {'team':'blue','label':'P','from':[22,10]},
      {'team':'red','label':'GK','from':[38,10]},
    ],
    'ball': {'from':[10,10],'to':[33,10]},
    'arrows':[
      {'kind':'run','from':[10,10],'to':[20,10],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[10,10],'to':[22,10],'rad':0.10,'color':'yellow'},
      {'kind':'pass','from':[22,10],'to':[33,10],'rad':-0.10,'color':'yellow'},
    ],
  },
  'fi-03': {
    'duration_ms': 5000,
    'caption_fr': "Centre arme et reprise 2e poteau: timing, le runner arrive lance.",
    'caption_nl': "Voorzet naar 2e paal: timing, loper komt in vol loop.",
    'players': [
      {'team':'blue','label':'C','from':[30,18]},
      {'team':'blue','label':'R','from':[32,5],'to':[37,2.5]},
      {'team':'red','label':'D','from':[34,8]},
      {'team':'red','label':'GK','from':[39,10]},
    ],
    'ball': {'from':[30,18],'to':[37,2.5]},
    'arrows':[
      {'kind':'run','from':[32,5],'to':[37,2.5],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[30,18],'to':[37,2.5],'rad':-0.25,'color':'yellow'},
    ],
  },
  'fi-06': {
    'duration_ms': 5000,
    'caption_fr': "Combinaison 3 joueurs: deux passes, appel de rupture, finition.",
    'caption_nl': "Driehoek met 3 spelers: twee passen, diepteloop, afwerking.",
    'players': [
      {'team':'blue','label':'1','from':[10,10]},
      {'team':'blue','label':'2','from':[18,15]},
      {'team':'blue','label':'3','from':[25,8],'to':[32,8]},
      {'team':'red','label':'GK','from':[39,10]},
    ],
    'ball': {'from':[10,10],'to':[32,8]},
    'arrows':[
      {'kind':'run','from':[25,8],'to':[32,8],'rad':0.0,'color':'blue'},
      {'kind':'pass','from':[10,10],'to':[18,15],'rad':0.0,'color':'yellow'},
      {'kind':'pass','from':[18,15],'to':[32,8],'rad':-0.10,'color':'yellow'},
    ],
  },

  # --- DEFENSE (1) ---
  'df-03': {
    'duration_ms': 5000,
    'caption_fr': "Coulissage ligne de 3: tous glissent du meme pas pour suivre le ballon.",
    'caption_nl': "Schuiven met 3: lijn beweegt synchroon met de bal.",
    'players': [
      {'team':'blue','label':'1','from':[10,5],'to':[10,3]},
      {'team':'blue','label':'2','from':[10,10],'to':[10,8]},
      {'team':'blue','label':'3','from':[10,15],'to':[10,13]},
      {'team':'red','label':'A','from':[3,7],'to':[8,3]},
    ],
    'ball': {'from':[3,7],'to':[8,3]},
    'arrows':[
      {'kind':'run','from':[10,5],'to':[10,3],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[10,10],'to':[10,8],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[10,15],'to':[10,13],'rad':0.0,'color':'blue'},
      {'kind':'run','from':[3,7],'to':[8,3],'rad':0.0,'color':'red'},
    ],
  },

  # --- GARDIEN (1) ---
  'gk-04': {
    'duration_ms': 5000,
    'caption_fr': "Sortie 1v1: GK sort tot pour fermer l'angle, attaquant arrive face.",
    'caption_nl': "1v1 uitkomst: GK sluit de hoek, aanvaller komt frontaal.",
    'players': [
      {'team':'red','label':'A','from':[15,10],'to':[30,10]},
      {'team':'blue','label':'GK','from':[38,10],'to':[32,10]},
    ],
    'ball': {'from':[15,10],'to':[30,10]},
    'arrows':[
      {'kind':'run','from':[15,10],'to':[30,10],'rad':0.0,'color':'red'},
      {'kind':'run','from':[38,10],'to':[32,10],'rad':0.0,'color':'blue'},
    ],
  },
}

# ==== SVG RENDERER =============================================================

def curve_path(x1, y1, x2, y2, rad=0.0):
    """Quadratic bezier in pitch coords -> SVG path d string."""
    sx1, sy1 = sx(x1), sy(y1)
    sx2, sy2 = sx(x2), sy(y2)
    mx, my = (sx1 + sx2) / 2, (sy1 + sy2) / 2
    dx, dy = sx2 - sx1, sy2 - sy1
    L = math.hypot(dx, dy) or 1.0
    nx, ny = -dy / L, dx / L
    off = rad * L
    cx, cy = mx + nx * off, my + ny * off
    return f'M {sx1:.1f} {sy1:.1f} Q {cx:.1f} {cy:.1f} {sx2:.1f} {sy2:.1f}', L * (1.0 + abs(rad) * 0.6)


def pitch_bands_svg():
    return ''.join(
        f'<rect x="{i*W/5:.1f}" y="0" width="{W/5:.1f}" height="{H}" fill="{PITCH_ALT if i%2 else PITCH_DARK}"/>'
        for i in range(5)
    )

def pitch_lines_svg():
    cx, cy = W/2, H/2
    return (
        f'<rect x="0" y="0" width="{W}" height="{H}" fill="none" stroke="white" stroke-width="3"/>'
        f'<line x1="{cx}" y1="0" x2="{cx}" y2="{H}" stroke="white" stroke-width="2.5"/>'
        f'<circle cx="{cx}" cy="{cy}" r="90" fill="none" stroke="white" stroke-width="2.5"/>'
        f'<circle cx="{cx}" cy="{cy}" r="6" fill="white"/>'
        f'<path d="M 0 {cy-180} A 180 180 0 0 1 0 {cy+180}" fill="none" stroke="white" stroke-width="2.5"/>'
        f'<path d="M {W} {cy-180} A 180 180 0 0 0 {W} {cy+180}" fill="none" stroke="white" stroke-width="2.5"/>'
        f'<circle cx="{sx(6)}" cy="{cy}" r="5" fill="white"/>'
        f'<circle cx="{sx(10)}" cy="{cy}" r="5" fill="white"/>'
        f'<circle cx="{sx(34)}" cy="{cy}" r="5" fill="white"/>'
        f'<circle cx="{sx(30)}" cy="{cy}" r="5" fill="white"/>'
        f'<rect x="-17" y="{cy-45}" width="17" height="90" fill="white" opacity="0.9"/>'
        f'<rect x="{W}" y="{cy-45}" width="17" height="90" fill="white" opacity="0.9"/>'
    )

def player_svg(x, y, label, team, anim_class=None):
    fill = {'red': RED_C, 'blue': BLUE_C, 'neutral': NEUTRAL_C}.get(team, BLUE_C)
    text_col = 'white'
    cls_attr = f' class="{anim_class}"' if anim_class else ''
    return (
        f'<g{cls_attr}>'
        f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="33" fill="white" opacity="0.25"/>'
        f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="26" fill="{fill}" stroke="white" stroke-width="2.5"/>'
        f'<text x="{sx(x):.1f}" y="{sy(y):.1f}" fill="{text_col}" font-family="DejaVu Sans, Arial, sans-serif" '
        f'font-size="20" font-weight="700" text-anchor="middle" dominant-baseline="central">{label}</text>'
        f'</g>'
    )

def render_svg(exo_id, exo_meta, anim):
    """Return SVG string for one exo animation."""
    title = exo_meta.get('title_fr', exo_id)
    caption = anim.get('caption_fr', '')
    dur = anim.get('duration_ms', 5000) / 1000.0

    # --- CSS parts ---
    css_parts = [
        'svg{font-family:"DejaVu Sans",Arial,sans-serif}',
        f'.arrow{{fill:none;stroke-linecap:round}}',
        f'.arrow-run{{stroke-width:4}}',
        f'.arrow-pass{{stroke-width:4;stroke-dasharray:10 8}}',
        f'.arrow-alt{{stroke-width:3;stroke-dasharray:5 6;opacity:0.6}}',
    ]

    # Generate per-player translate keyframes
    for i, p in enumerate(anim.get('players', [])):
        if 'to' not in p: continue
        dx = sx(p['to'][0]) - sx(p['from'][0])
        dy = sy(p['to'][1]) - sy(p['from'][1])
        css_parts.append(
          f'.p{i}{{animation:p{i}-mv {dur}s ease-in-out infinite}}'
          f'@keyframes p{i}-mv{{'
          f'0%{{transform:translate(0,0)}}'
          f'10%{{transform:translate(0,0)}}'
          f'45%{{transform:translate({dx:.0f}px,{dy:.0f}px)}}'
          f'75%{{transform:translate({dx:.0f}px,{dy:.0f}px)}}'
          f'85%{{transform:translate(0,0)}}'
          f'100%{{transform:translate(0,0)}}}}'
        )

    # Ball keyframes
    ball = anim.get('ball')
    if ball:
        bdx = sx(ball['to'][0]) - sx(ball['from'][0])
        bdy = sy(ball['to'][1]) - sy(ball['from'][1])
        css_parts.append(
          f'.ball{{animation:bfly {dur}s ease-in-out infinite}}'
          f'@keyframes bfly{{'
          f'0%{{transform:translate(0,0)}}'
          f'20%{{transform:translate(0,0)}}'
          f'45%{{transform:translate({bdx:.0f}px,{bdy:.0f}px)}}'
          f'75%{{transform:translate({bdx:.0f}px,{bdy:.0f}px)}}'
          f'85%{{transform:translate(0,0)}}'
          f'100%{{transform:translate(0,0)}}}}'
        )

    # Arrow keyframes (draw-in + hold + fade)
    for i, a in enumerate(anim.get('arrows', [])):
        _, L = curve_path(a['from'][0], a['from'][1], a['to'][0], a['to'][1], a.get('rad', 0))
        css_parts.append(
          f'.a{i}{{stroke-dasharray:{L:.0f};stroke-dashoffset:{L:.0f};opacity:0;'
          f'animation:a{i}-dr {dur}s ease-in-out infinite}}'
          f'@keyframes a{i}-dr{{'
          f'0%{{stroke-dashoffset:{L:.0f};opacity:0}}'
          f'15%{{stroke-dashoffset:{L:.0f};opacity:0}}'
          f'18%{{opacity:1}}'
          f'45%{{stroke-dashoffset:0;opacity:1}}'
          f'75%{{stroke-dashoffset:0;opacity:1}}'
          f'85%{{stroke-dashoffset:0;opacity:0}}'
          f'100%{{stroke-dashoffset:{L:.0f};opacity:0}}}}'
        )

    # Zone keyframes (pulse)
    for i, z in enumerate(anim.get('zones', [])):
        if z.get('pulse'):
            css_parts.append(
              f'.z{i}{{animation:z{i}-ps {dur}s ease-in-out infinite}}'
              f'@keyframes z{i}-ps{{'
              f'0%{{opacity:0.08}}'
              f'35%{{opacity:0.08}}'
              f'45%{{opacity:0.45}}'
              f'70%{{opacity:0.45}}'
              f'85%{{opacity:0.12}}'
              f'100%{{opacity:0.08}}}}'
            )
            css_parts.append(
              f'.zl{i}{{animation:zl{i}-ps {dur}s ease-in-out infinite}}'
              f'@keyframes zl{i}-ps{{'
              f'0%{{opacity:0}}'
              f'40%{{opacity:0}}'
              f'50%{{opacity:1}}'
              f'75%{{opacity:1}}'
              f'85%{{opacity:0}}'
              f'100%{{opacity:0}}}}'
            )

    # Reduced motion override: no animation, show final state
    css_parts.append(
      '@media(prefers-reduced-motion:reduce){'
      '*,*::before,*::after{animation:none !important;transition:none !important}'
      '.ball,[class^="p"],[class*=" p"]{transform:none !important}'
      '[class^="a"]{stroke-dashoffset:0 !important;opacity:1 !important}'
      '[class^="z"]{opacity:0.35 !important}'
      '[class^="zl"]{opacity:1 !important}'
      '}'
    )

    css = '\n'.join(css_parts)

    # --- Body parts ---
    body = []
    body.append(pitch_bands_svg())
    body.append(pitch_lines_svg())

    # Zones
    for i, z in enumerate(anim.get('zones', [])):
        pts = ' '.join(f'{sx(x):.1f},{sy(y):.1f}' for x, y in z['points'])
        zc = ZONE_COLORS.get(z.get('color', 'yellow'), YELLOW_C)
        pulse_cls = f'z{i}' if z.get('pulse') else ''
        op = '0.08' if z.get('pulse') else '0.22'
        body.append(f'<polygon class="{pulse_cls}" points="{pts}" fill="{zc}" opacity="{op}"/>')
        lbl = z.get('label', '')
        if lbl:
            lx, ly = z['points'][0]
            body.append(
              f'<g class="zl{i}">'
              f'<rect x="{sx(lx)+4:.0f}" y="{sy(ly)-26:.0f}" width="{max(64, 11*len(lbl)):.0f}" height="22" '
              f'fill="white" stroke="{zc}" stroke-width="1.8" rx="5"/>'
              f'<text x="{sx(lx)+4+max(64,11*len(lbl))/2:.0f}" y="{sy(ly)-10:.0f}" '
              f'fill="{zc}" font-size="13" font-weight="700" text-anchor="middle">{lbl}</text>'
              f'</g>'
            )

    # Arrows
    for i, a in enumerate(anim.get('arrows', [])):
        d, _ = curve_path(a['from'][0], a['from'][1], a['to'][0], a['to'][1], a.get('rad', 0))
        color_key = a.get('color', 'red')
        stroke_c = ZONE_COLORS.get(color_key, RED_C) if color_key != 'yellow' else TEXT_DARK
        marker = {
          'red': 'arrowhead-red',
          'blue': 'arrowhead-blue',
          'yellow': 'arrowhead-dark',
          'neutral': 'arrowhead-gray',
        }.get(color_key, 'arrowhead-red')
        kind_cls = {'run':'arrow-run','pass':'arrow-pass','alt':'arrow-alt'}.get(a.get('kind','run'), 'arrow-run')
        body.append(
          f'<path class="arrow {kind_cls} a{i}" d="{d}" '
          f'stroke="{stroke_c}" marker-end="url(#{marker})"/>'
        )

    # Players (static label 'GK' gets yellow pill)
    for i, p in enumerate(anim.get('players', [])):
        label = p.get('label', '?')
        team = p['team']
        is_gk = label.upper() == 'GK'
        if is_gk:
            # render separately with yellow fill
            anim_cls = f'p{i}' if 'to' in p else None
            cls_attr = f' class="{anim_cls}"' if anim_cls else ''
            x, y = p['from']
            body.append(
              f'<g{cls_attr}>'
              f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="33" fill="white" opacity="0.25"/>'
              f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="26" fill="{YELLOW_C}" stroke="white" stroke-width="2.5"/>'
              f'<text x="{sx(x):.1f}" y="{sy(y):.1f}" fill="{TEXT_DARK}" font-family="DejaVu Sans, Arial, sans-serif" '
              f'font-size="15" font-weight="700" text-anchor="middle" dominant-baseline="central">GK</text>'
              f'</g>'
            )
        else:
            anim_cls = f'p{i}' if 'to' in p else None
            body.append(player_svg(p['from'][0], p['from'][1], label, team, anim_cls))

    # Ball (last, on top)
    if ball:
        bx, by = ball['from']
        body.append(
          f'<g class="ball">'
          f'<circle cx="{sx(bx):.1f}" cy="{sy(by):.1f}" r="14" fill="white" stroke="{TEXT_DARK}" stroke-width="2"/>'
          f'<circle cx="{sx(bx):.1f}" cy="{sy(by):.1f}" r="6" fill="{TEXT_DARK}"/>'
          f'</g>'
        )

    # Watermark
    body.append(
      f'<text x="{W-20}" y="{H-15}" fill="white" opacity="0.5" '
      f'font-size="14" font-style="italic" text-anchor="end">RealDev Vilvoorde</text>'
    )

    # --- Defs (markers + style) ---
    defs = (
      '<defs>'
      f'<marker id="arrowhead-red" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
      f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{RED_C}"/></marker>'
      f'<marker id="arrowhead-blue" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
      f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{BLUE_C}"/></marker>'
      f'<marker id="arrowhead-dark" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
      f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{TEXT_DARK}"/></marker>'
      f'<marker id="arrowhead-gray" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
      f'<path d="M 0 0 L 10 5 L 0 10 z" fill="#666"/></marker>'
      f'<style><![CDATA[\n{css}\n]]></style>'
      '</defs>'
    )

    # --- Assemble (pitch 600 + caption strip 80) ---
    tot_h = H + 80
    svg = (
      f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {tot_h}" '
      f'width="{W}" height="{tot_h}" preserveAspectRatio="xMidYMid meet" role="img" '
      f'aria-label="{xe(title)}">'
      f'{defs}'
      f'<g>{ "".join(body) }</g>'
      f'<g transform="translate(0,{H})">'
      f'<rect x="0" y="0" width="{W}" height="80" fill="#f5f5f7"/>'
      f'<text x="20" y="32" fill="{TEXT_DARK}" font-size="22" font-weight="700">{xe(title)}</text>'
      f'<text x="20" y="60" fill="#555" font-size="14" font-style="italic">{xe(caption)}</text>'
      f'</g>'
      f'</svg>'
    )
    return svg

# ==== MAIN =====================================================================

def inject_animations(path=EXOS_JSON):
    """Write ANIMATIONS dict into exercises.json 'animation' field."""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    injected = 0
    for ex in data['exercises']:
        if ex['id'] in ANIMATIONS:
            ex['animation'] = ANIMATIONS[ex['id']]
            injected += 1
        elif 'animation' not in ex:
            ex['animation'] = None
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'Injected {injected} animations into {path}')

def generate_svgs(src=EXOS_JSON, dst_dir=OUT_DIR):
    os.makedirs(dst_dir, exist_ok=True)
    with open(src, 'r', encoding='utf-8') as f:
        data = json.load(f)
    n = 0
    for ex in data['exercises']:
        if not ex.get('animation'):
            continue
        svg = render_svg(ex['id'], ex, ex['animation'])
        out = os.path.join(dst_dir, f'{ex["id"]}.svg')
        with open(out, 'w', encoding='utf-8') as f:
            f.write(svg)
        n += 1
        print(f'  {ex["id"]}: {len(svg)} bytes')
    print(f'Wrote {n} SVGs to {dst_dir}')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--inject', action='store_true')
    ap.add_argument('--generate', action='store_true')
    ap.add_argument('--all', action='store_true')
    args = ap.parse_args()
    if args.all or args.inject:
        inject_animations()
    if args.all or args.generate:
        generate_svgs()
    if not any([args.all, args.inject, args.generate]):
        print('Usage: build_animations.py --inject | --generate | --all')

if __name__ == '__main__':
    main()
