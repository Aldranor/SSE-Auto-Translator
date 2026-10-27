import json
from pathlib import Path

target_file = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")

with open(target_file, "r", encoding="utf-8") as f:
    data = json.load(f)

missing = []

for idx, s in enumerate(data):
    trans = s.get("string")
    status = s.get("status")
    orig = s.get("original") or ""
    
    # Needs translation if status is TranslationRequired, or string is None/empty, or string == orig and not proper name/variable
    if status == "TranslationRequired" or trans is None or trans == "":
        missing.append({
            "index_in_file": idx,
            "form_id": s.get("form_id"),
            "type": s.get("type"),
            "edid": s.get("editor_id"),
            "index": s.get("index"),
            "status": status,
            "original": orig,
            "current_string": trans
        })

print(f"Total TranslationRequired or empty strings: {len(missing)}")

# Also check other two files
smim_file = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/lotd_smim.esp.json")
with open(smim_file, "r", encoding="utf-8") as f:
    smim_data = json.load(f)
smim_missing = [s for s in smim_data if s.get("status") == "TranslationRequired" or not s.get("string")]
print(f"Total missing in lotd_smim: {len(smim_missing)}")

txt_file = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/interface/translations/legacyofthedragonborn_french.txt.json")
with open(txt_file, "r", encoding="utf-8") as f:
    txt_data = json.load(f)
txt_missing = [s for s in txt_data if s.get("status") == "TranslationRequired" or not s.get("string")]
print(f"Total missing in txt_file: {len(txt_missing)}")

with open("lotd_all_missing.json", "w", encoding="utf-8") as out:
    json.dump(missing, out, indent=2, ensure_ascii=False)
