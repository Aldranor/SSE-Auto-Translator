# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for it in data:
    if it.get('type') == 'BOOK DESC':
        print(f"=== BOOK DESC: {it.get('editor_id')} ===")
        print(it.get('original'))
        print("\n" + "="*60 + "\n")
