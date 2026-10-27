import json
import re

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

english_markers = [
    r"\bthe\b", r"\band\b", r"\bwith\b", r"\bfrom\b", r"\bwhich\b", r"\bthey\b",
    r"\btheir\b", r"\bwhen\b", r"\bwould\b", r"\bcould\b", r"\bshould\b", r"\bthis\b",
    r"\byou\b", r"\byour\b"
]
en_regex = re.compile("|".join(english_markers), re.I)

non_book_english = []
for s in data:
    t = s.get("type") or ""
    if "BOOK" in t:
        continue
    trans = s.get("string") or ""
    orig = s.get("original") or ""
    if len(trans) < 15:
        continue
        
    words = trans.split()
    if len(words) < 4:
        continue
        
    en_matches = en_regex.findall(trans)
    # If several English markers in a short sentence
    if len(en_matches) >= 2 and len(en_matches) / len(words) >= 0.2:
        non_book_english.append({
            "form_id": s.get("form_id"),
            "edid": s.get("editor_id"),
            "type": t,
            "orig": orig,
            "trans": trans,
            "status": s.get("status")
        })

print(f"Total non-book English texts in LOTD translation: {len(non_book_english)}")
for x in non_book_english[:20]:
    print(f"[{x['type']}] ({x['form_id']}) Status: {x['status']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print()
