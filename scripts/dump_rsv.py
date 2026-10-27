import json

path = r'data/user/database/french/Racial Skin Variance - SPID_french.txt - French/interface/translations/Racial Skin Variance - SPID_french.txt.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('rsv_entries_dump.txt', 'w', encoding='utf-8') as out:
    for i, entry in enumerate(data):
        out.write(f"=== Entry {i} | Status: {entry.get('status')} | Key: {entry.get('mcm_id')} ===\n")
        out.write(f"ORIG: {entry.get('original')}\n")
        out.write(f"TRAN: {entry.get('string')}\n\n")

print(f"Dumped {len(data)} entries successfully")
