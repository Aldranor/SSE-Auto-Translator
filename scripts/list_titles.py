import json

p2_data = json.load(open("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json", encoding="utf-8"))

titles = [e for e in p2_data if e.get("type") == "QUST FULL"]
print(f"Total QUST FULL: {len(titles)}")
for t in titles:
    print(f"[{t.get('editor_id')}] ({t.get('form_id')})")
    print(f"  ORIG: {t.get('original')}")
    print(f"  TRAD: {t.get('string')}")
