# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

mgef_items = [it for it in data if it.get('type') in ('MGEF FULL', 'MGEF DNAM')]

for i in range(0, min(50, len(mgef_items))):
    it = mgef_items[i]
    print(f"[{it.get('type')}] {it.get('editor_id')} : {repr(it.get('original'))}")
