import json
from pathlib import Path

p2_path = Path("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json")
p2_data = json.load(open(p2_path, encoding="utf-8"))

with open("p2_sample_check.txt", "w", encoding="utf-8") as out:
    for idx, e in enumerate(p2_data):
        out.write(f"=== Entry {idx} [{e.get('type')}] {e.get('form_id')} {e.get('editor_id')} idx={e.get('index')} ===\n")
        out.write(f"ORIG: {e.get('original')}\n")
        out.write(f"TRAD: {e.get('string')}\n\n")

print("Saved to p2_sample_check.txt")
