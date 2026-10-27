# -*- coding: utf-8 -*-
import json

path = r"data/user/database/french/SkyDecoctionEN3.0 fr/SkyDecoction.esp.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")
statuses = {}
for item in data:
    st = item.get("status")
    statuses[st] = statuses.get(st, 0) + 1
print("Statuses:", statuses)

print("\n--- All entries ---")
for i, item in enumerate(data):
    form_id = item.get("form_id")
    editor_id = item.get("editor_id")
    record_type = item.get("type")
    orig = item.get("original")
    string = item.get("string")
    status = item.get("status")
    print(f"[{i+1}] {status} | {record_type} | {editor_id} | FormID: {form_id}")
    print(f"   EN: {repr(orig)}")
    print(f"   FR: {repr(string)}")
