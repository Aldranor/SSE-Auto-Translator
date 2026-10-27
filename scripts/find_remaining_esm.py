import json
from pathlib import Path

esm_file = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")

with open(esm_file, "r", encoding="utf-8") as f:
    esm_data = json.load(f)

still_missing = [s for s in esm_data if s.get("status") == "TranslationRequired" or not s.get("string")]
print(f"Remaining missing in ESM: {len(still_missing)}")
for s in still_missing:
    print(f"[{s.get('type')}] ({s.get('form_id')}) {s.get('editor_id')}: {repr(s.get('original'))}")
