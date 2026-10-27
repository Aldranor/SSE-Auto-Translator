# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

dnam_items = [it for it in data if it.get('type') == 'MGEF DNAM']
print(f"Total DNAM items: {len(dnam_items)}")
for i, it in enumerate(dnam_items):
    print(f"[{i+1}] {it.get('editor_id')} ({it.get('form_id')})")
    print(it.get('original'))
    print("-" * 40)
