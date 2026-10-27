# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

mgef_full = [it for it in data if it.get('type') == 'MGEF FULL']

for it in mgef_full:
    print(f"{it.get('editor_id')} | {repr(it.get('original'))}")
