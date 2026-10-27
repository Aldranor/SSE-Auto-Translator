import json

with open("lotd_generated_translations.json", "r", encoding="utf-8") as f:
    esm_translations = json.load(f)["esm"]

with open("lotd_items_to_translate.json", "r", encoding="utf-8") as f:
    esm_items = json.load(f)["esm"]

not_in_t = []
for item in esm_items:
    orig = item["original"]
    if orig not in esm_translations:
        not_in_t.append(item)

print(f"Items not in esm_translations: {len(not_in_t)}")
for it in not_in_t:
    print(f"[{it['type']}] ({it['form_id']}) {it['edid']}: {repr(it['original'])}")
