# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

with open("skydec_dump.txt", "w", encoding="utf-8") as out:
    for i, it in enumerate(data):
        out.write(f"[{i+1}] {it.get('type')} | {it.get('editor_id')} | {it.get('form_id')}\n")
        out.write(f"ORIG: {it.get('original')}\n\n")

print(f"Dumped {len(data)} items to skydec_dump.txt")
