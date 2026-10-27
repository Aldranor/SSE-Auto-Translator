import json
from collections import Counter

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

incomplete = [s for s in data if s.get("status") == "TranslationIncomplete"]
required = [s for s in data if s.get("status") == "TranslationRequired"]

print(f"TranslationIncomplete: {len(incomplete)}")
inc_types = Counter(s.get("type") for s in incomplete)
for t, c in inc_types.most_common(10):
    print(f"  {t}: {c}")

print(f"\nTranslationRequired: {len(required)}")
req_types = Counter(s.get("type") for s in required)
for t, c in req_types.most_common(10):
    print(f"  {t}: {c}")

print("\nSample TranslationRequired (first 10):")
for s in required[:10]:
    print(f"[{s.get('type')}] ({s.get('form_id')}) {s.get('editor_id')}: {s.get('original')[:80]}")

print("\nSample TranslationIncomplete (first 10):")
for s in incomplete[:10]:
    print(f"[{s.get('type')}] ({s.get('form_id')}) {s.get('editor_id')}: Orig='{s.get('original')[:40]}' -> Trans='{s.get('string')[:40]}'")
