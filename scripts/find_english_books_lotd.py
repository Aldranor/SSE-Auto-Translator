import json
import re

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

english_markers = [
    r"\bthe\b", r"\band\b", r"\bwith\b", r"\bfrom\b", r"\bwhich\b", r"\bthey\b",
    r"\btheir\b", r"\bwhen\b", r"\bwould\b", r"\bcould\b", r"\bshould\b", r"\bthis\b"
]
en_regex = re.compile("|".join(english_markers), re.I)

english_books = []
for s in data:
    t = s.get("type") or ""
    if "BOOK" not in t:
        continue
    trans = s.get("string") or ""
    orig = s.get("original") or ""
    if len(trans) < 100:
        continue
    
    # Strip HTML tags
    clean_trans = re.sub(r"<[^>]+>", " ", trans)
    clean_trans = clean_trans.replace("[pagebreak]", " ")
    
    words = clean_trans.split()
    if not words:
        continue
        
    en_matches = en_regex.findall(clean_trans)
    en_ratio = len(en_matches) / len(words)
    
    # If more than 10% of words are common English stop words, it's definitely in English!
    if en_ratio > 0.08 and len(en_matches) > 10:
        english_books.append({
            "form_id": s.get("form_id"),
            "edid": s.get("editor_id"),
            "type": t,
            "orig_title": s.get("original")[:60],
            "trans_sample": clean_trans[:150].strip(),
            "en_ratio": round(en_ratio, 3),
            "en_matches": len(en_matches),
            "word_count": len(words)
        })

print(f"Total English books in LOTD translation: {len(english_books)}")
for b in english_books[:15]:
    print(f"- [{b['edid']}] ({b['form_id']}) words: {b['word_count']}, en_ratio: {b['en_ratio']}")
    print(f"  Snippet: {b['trans_sample'][:100]}...")
