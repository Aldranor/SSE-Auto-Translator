# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== MGEF FULL & DNAM ===")
with open("mgef_dump.txt", "w", encoding="utf-8") as out:
    for it in data:
        t = it.get('type')
        if t in ('MGEF FULL', 'MGEF DNAM'):
            out.write(f"[{t}] {it.get('editor_id')} ({it.get('form_id')})\n")
            out.write(f"{repr(it.get('original'))}\n\n")

print("Dumped MGEF to mgef_dump.txt")
