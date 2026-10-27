import json

with open("lotd_items_to_translate.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data["esm"]:
    t = item["type"]
    fid = item["form_id"]
    edid = item["edid"]
    orig = item["original"]
    print(f"[{t}] FormID: {fid} | EDID: {edid}")
    print(f"  Orig: {orig}\n")
