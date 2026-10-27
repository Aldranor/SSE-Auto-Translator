import json

cc_data = json.load(open("data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json", encoding="utf-8"))
p2_data = json.load(open("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json", encoding="utf-8"))
cc_by_orig = {e["original"]: e["string"] for e in cc_data if e.get("string")}

non_cc = [e for e in p2_data if e.get("original") not in cc_by_orig]
print(f"Non-CC entries count: {len(non_cc)}")

with open("exp_non_cc.txt", "w", encoding="utf-8") as out:
    for e in non_cc:
        out.write(f"[{e.get('type')}] ({e.get('form_id')}) {e.get('editor_id')} idx={e.get('index')}\n")
        out.write(f"  ORIG: {repr(e.get('original'))}\n")
        out.write(f"  TRAD: {repr(e.get('string'))}\n\n")

print("Saved to exp_non_cc.txt")
