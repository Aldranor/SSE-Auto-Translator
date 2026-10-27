# -*- coding: utf-8 -*-
"""
Script de traduction complète pour SkyDecoction.esp.json (299 entrées)
"""

import json

ESP_PATH = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"

# Noms de base des 19 familles de décoctions
DECOCTION_NAMES = {
    'Cat': ('Chat', 'm'),
    'Dragonmaw': ('Gueule de dragon', 'f'),
    'Hyphalosaurus': ('Hyphalosaure', 'm'),
    'Thunderstorm': ('Tempête', 'f'),
    'Testudo': ('Testudo', 'f'),
    'Termination': ('Terminaison', 'f'),
    'Equipartition': ('Équipartition', 'f'),
    'Rosmontis': ('Rosmontis', 'f'),
    'Strigiformes': ('Strigiformes', 'mp'),
    'Prism': ('Prisme', 'm'),
    'Herculiani': ('Herculiani', 'mp'),
    'Ioviani': ('Ioviani', 'mp'),
    'Exploratores': ('Exploratores', 'mp'),
    'Healer': ('Guérisseur', 'm'),
    'Sober': ('Lucidité', 'f'),
    'Eucles': ('Euclès', 'm'),
    'Defensores': ('Defensores', 'mp'),
    'Rejuvenation': ('Rajeunissement', 'm'),
    'Craftsman': ('Artisan', 'm'),
}

def get_tier_name(base_en, tier):
    """
    tier: 'base', 'enhanced', 'superior'
    """
    fr_name, gender = DECOCTION_NAMES[base_en]
    if tier == 'base':
        return f"Décoction : {fr_name}"
    elif tier == 'enhanced':
        adj = 'amélioré' if gender == 'm' else ('améliorée' if gender == 'f' else 'améliorés')
        return f"Décoction : {fr_name} {adj}"
    elif tier == 'superior':
        adj = 'supérieur' if gender == 'm' else ('supérieure' if gender == 'f' else 'supérieurs')
        return f"Décoction : {fr_name} {adj}"

def get_residue_name(base_en, tier):
    fr_name, gender = DECOCTION_NAMES[base_en]
    if tier == 'base':
        return f"Résidu : {fr_name}"
    elif tier == 'enhanced':
        adj = 'amélioré' if gender == 'm' else ('améliorée' if gender == 'f' else 'améliorés')
        return f"Résidu : {fr_name} {adj}"
    elif tier == 'superior':
        adj = 'supérieur' if gender == 'm' else ('supérieure' if gender == 'f' else 'supérieurs')
        return f"Résidu : {fr_name} {adj}"

print("Helper defined.")
