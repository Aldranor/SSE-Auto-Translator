# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

dnam_edids = set(it.get('editor_id') for it in data if it.get('type') == 'MGEF DNAM')
print("Total with DNAM:", len(dnam_edids))

for it in data:
    if it.get('type') == 'MGEF FULL':
        ed = it.get('editor_id')
        orig = it.get('original')
        has_dnam = ed in dnam_edids
        if not has_dnam:
            print(f"Internal / Hidden MGEF: {ed} -> {repr(orig)}")
