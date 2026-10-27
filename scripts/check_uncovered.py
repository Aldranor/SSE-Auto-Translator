import json

with open("lotd_items_to_translate.json", "r", encoding="utf-8") as f:
    items = json.load(f)["esm"]

with open("lotd_generated_translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)["esm"]

uncovered = []
for item in items:
    orig = item["original"]
    edid = item["edid"]
    if orig not in translations and edid not in translations:
        uncovered.append(item)

print(f"Uncovered items: {len(uncovered)}")
for u in uncovered:
    print(f"[{u['type']}] ({u['form_id']}) {u['edid']}: {repr(u['original'])}")
