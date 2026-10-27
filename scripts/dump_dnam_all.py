# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

dnam_items = [it for it in data if it.get('type') == 'MGEF DNAM']

with open("dnam_all.txt", "w", encoding="utf-8") as f:
    for i, it in enumerate(dnam_items):
        f.write(f"[{i+1}] {it.get('editor_id')} ({it.get('form_id')})\n")
        f.write(f"{it.get('original')}\n")
        f.write("="*50 + "\n")

print(f"Dumped {len(dnam_items)} DNAM items to dnam_all.txt")
