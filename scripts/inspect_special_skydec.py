# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== SPECIAL RECORDS ===")
for it in data:
    t = it.get('type')
    if t in ('BOOK FULL', 'BOOK DESC', 'FLOR FULL', 'FLOR RNAM', 'FURN FULL', 'SPEL FULL', 'PERK FULL', 'MESG DESC', 'CELL FULL'):
        print(f"[{t}] {it.get('editor_id')} ({it.get('form_id')}):")
        print(it.get('original'))
        print("="*40)
