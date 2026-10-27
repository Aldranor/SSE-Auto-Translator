import json

with open("lotd_deep_audit.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total untranslated_english: {len(data['untranslated_english'])}")
for x in data["untranslated_english"][:20]:
    print(f"[{x['type']}] FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig'][:120]}")
    print(f"  Trans: {x['trans'][:120]}")
    print()
