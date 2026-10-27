import json

txt_path = r"data/user/database/french/ImmersiveHunting_french.txt - French/interface/translations/ImmersiveHunting_french.txt.json"
with open(txt_path, "r", encoding="utf-8") as f:
    txt_data = json.load(f)

with open("ih_txt_dump.txt", "w", encoding="utf-8") as out:
    for i, e in enumerate(txt_data):
        out.write(f"=== Entry {i} | Key: {e.get('mcm_id')} | Status: {e.get('status')} ===\n")
        out.write(f"ORIG: {e.get('original')}\n")
        out.write(f"CURR: {e.get('string')}\n\n")

print("Dumped 72 entries successfully.")
