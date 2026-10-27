# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== ALCH FULL ===")
for it in data:
    if it.get('type') == 'ALCH FULL':
        print(f"{it.get('editor_id')}: {repr(it.get('original'))}")

print("\n=== MISC FULL ===")
for it in data:
    if it.get('type') == 'MISC FULL':
        print(f"{it.get('editor_id')}: {repr(it.get('original'))}")
