# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")

categories = {
    'books': [],
    'alch': [],
    'misc_residue': [],
    'misc_tools': [],
    'mgef_dnam': [],
    'mgef_full': [],
    'special': []
}

for i, it in enumerate(data):
    t = it.get('type')
    orig = it.get('original')
    edid = it.get('editor_id')
    
    if t in ('BOOK FULL', 'BOOK DESC'):
        categories['books'].append((i, it))
    elif t == 'ALCH FULL':
        categories['alch'].append((i, it))
    elif t == 'MISC FULL':
        if 'Residue' in orig:
            categories['misc_residue'].append((i, it))
        else:
            categories['misc_tools'].append((i, it))
    elif t == 'MGEF DNAM':
        categories['mgef_dnam'].append((i, it))
    elif t == 'MGEF FULL':
        categories['mgef_full'].append((i, it))
    else:
        categories['special'].append((i, it))

for k, v in categories.items():
    print(f"Category '{k}': {len(v)} items")
