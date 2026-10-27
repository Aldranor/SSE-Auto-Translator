import json

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Find QUST CNAM for Shattered Legacy
shattered = [s for s in data if s.get("form_id") == "05121573|LegacyoftheDragonborn.esm" and s.get("type") == "QUST CNAM"]
print(f"Shattered legacy QUST CNAM entries: {len(shattered)}")
for s in shattered[:10]:
    print(f"Index: {s.get('index')}")
    print(f"  Orig:  {s.get('original')}")
    print(f"  Trans: {s.get('string')}")
    print(f"  Status: {s.get('status')}")
    print()
