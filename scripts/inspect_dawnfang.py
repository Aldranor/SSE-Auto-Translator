import json

path = "data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json"
data = json.load(open(path, encoding="utf-8"))

dawnfang = [e for e in data if "ccbgssse013" in e.get("form_id", "").lower() or e.get("editor_id") == "ccBGSSSE013_AquisitionQuest"]
print(f"Total Dawnfang entries: {len(dawnfang)}")
for idx, e in enumerate(dawnfang):
    print(f"[{idx}] type={e.get('type')} idx={e.get('index')}")
    print(f"  ORIG: {repr(e.get('original'))}")
    print(f"  TRAD: {repr(e.get('string'))}")
    print(f"  STAT: {e.get('status')}")
