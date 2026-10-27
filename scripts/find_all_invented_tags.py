import json
import re
from collections import Counter

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

invented_tags_records = []

for s in data:
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    if not trans or trans == orig:
        continue
        
    orig_tags = set(re.findall(r"<[^>]+>", orig))
    trans_tags = set(re.findall(r"<[^>]+>", trans))
    
    # Filter out standard HTML tags like <br>, <b>, </b>, <i>, </i>, <p>, </p>, <font...>, </font>, <img...>
    html_tags = {r"^</?(b|i|u|p|br|font|img|span|div)(?:\s+[^>]*?)?/?>$"}
    
    invented = set()
    for t in trans_tags:
        # Check if t was in orig
        if t in orig_tags:
            continue
        # Check if it is a standard HTML tag that is safe
        is_html = any(re.match(pat, t, re.I) for pat in html_tags)
        if is_html:
            continue
        invented.add(t)
        
    if invented:
        invented_tags_records.append({
            "form_id": s.get("form_id"),
            "type": s.get("type"),
            "edid": s.get("editor_id"),
            "orig": orig,
            "trans": trans,
            "invented": list(invented)
        })

print(f"Total records with invented tags: {len(invented_tags_records)}")
all_invented = Counter()
for r in invented_tags_records:
    for inv in r["invented"]:
        all_invented[inv] += 1

print("\nAll invented tags and their frequency:")
for tag, count in all_invented.most_common():
    print(f"  {tag}: {count}")
