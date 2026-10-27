import json

path = "data/user/database/french/Sunthgat/Sunthgat.esp.json"
with open(path, "r", encoding="utf-8") as f:
    entries = json.load(f)

with open("sunthgat_analysis.txt", "w", encoding="utf-8") as out:
    for idx, e in enumerate(entries):
        out.write(f"=== Entry {idx} [{e.get('type')}] FormID: {e.get('form_id')} EDID: {e.get('editor_id')} Status: {e.get('status')} ===\n")
        out.write(f"ORIG: {e.get('original')}\n")
        out.write(f"TRAD: {e.get('string')}\n\n")

print(f"Dumped {len(entries)} entries to sunthgat_analysis.txt")
