import json
from pathlib import Path

p2_path = Path("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json")
p2_data = json.load(open(p2_path, encoding="utf-8"))

print(f"Total entries in p2: {len(p2_data)}")

# Let's check for obvious mismatches:
# For example, if original mentions X (e.g. Degaine / beggar) and French translation mentions Y (e.g. Senna / Hamal)
suspects = []

for idx, e in enumerate(p2_data):
    orig = e.get("original") or ""
    trad = e.get("string") or ""
    status = e.get("status")
    fid = e.get("form_id")
    qtype = e.get("type")
    stage_idx = e.get("index")
    edid = e.get("editor_id")
    
    # Check if empty
    if not trad or status == "TranslationRequired":
        suspects.append((idx, "EMPTY", e))
        continue
        
    # Check English remaining in translation (heuristic: English stopwords or common untranslated strings)
    # Check if trad is identical to orig
    if orig.lower() == trad.lower() and len(orig.split()) > 2:
        suspects.append((idx, "UNTRANSLATED", e))
        continue

print(f"Suspects (empty or untranslated): {len(suspects)}")
for s in suspects:
    print(s[0], s[1], s[2].get("original")[:40], "->", s[2].get("string"))
