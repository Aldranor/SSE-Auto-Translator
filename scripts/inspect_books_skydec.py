# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

for it in data:
    if it.get('type') == 'BOOK FULL':
        print(f"BOOK TITLE: {it.get('editor_id')} | {it.get('original')}")
    elif it.get('type') == 'BOOK DESC':
        print(f"BOOK DESC: {it.get('editor_id')} | Length: {len(it.get('original'))}")
        # print first 200 chars
        print(it.get('original')[:200])
        print("...")
