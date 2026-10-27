import json
from pathlib import Path

esm_path = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")
txt_path = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/interface/translations/legacyofthedragonborn_french.txt.json")

with open(esm_path, "r", encoding="utf-8") as f:
    esm_data = json.load(f)

with open(txt_path, "r", encoding="utf-8") as f:
    txt_data = json.load(f)

esm_missing = []
for idx, s in enumerate(esm_data):
    if s.get("status") == "TranslationRequired" or not s.get("string"):
        esm_missing.append({
            "target": "esm",
            "index_in_file": idx,
            "form_id": s.get("form_id"),
            "type": s.get("type"),
            "edid": s.get("editor_id"),
            "index": s.get("index"),
            "original": s.get("original")
        })

txt_missing = []
for idx, s in enumerate(txt_data):
    if s.get("status") == "TranslationRequired" or not s.get("string"):
        txt_missing.append({
            "target": "txt",
            "index_in_file": idx,
            "mcm_id": s.get("mcm_id"),
            "original": s.get("original")
        })

print(f"ESM missing: {len(esm_missing)}, TXT missing: {len(txt_missing)}")

with open("lotd_items_to_translate.json", "w", encoding="utf-8") as f:
    json.dump({"esm": esm_missing, "txt": txt_missing}, f, indent=2, ensure_ascii=False)
