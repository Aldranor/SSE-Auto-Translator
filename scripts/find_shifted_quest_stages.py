import json
import re

with open("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Analyze all QUST CNAM and other quest stages
quest_mismatches = []

for s in data:
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    t = s.get("type") or ""
    form_id = s.get("form_id") or ""
    edid = s.get("editor_id") or ""
    
    if not trans or trans == orig:
        continue
        
    # Check if trans is in English (detected English sentence)
    is_trans_english = bool(re.search(r"\b(the|and|with|from|which|they|their|when|would|could|should|this|that|have|been)\b", trans, re.I))
    
    # Check if orig and trans talk about completely different entities/events
    # If both are in English, compare words
    if is_trans_english and len(orig.split()) > 5 and len(trans.split()) > 5:
        orig_words = set(re.findall(r"\b[a-zA-Z]{4,}\b", orig.lower()))
        trans_words = set(re.findall(r"\b[a-zA-Z]{4,}\b", trans.lower()))
        overlap = orig_words & trans_words
        
        # If very little word overlap between two English sentences for the same record
        if len(orig_words) > 0 and len(overlap) / len(orig_words) < 0.2:
            quest_mismatches.append({
                "form_id": form_id,
                "type": t,
                "edid": edid,
                "orig": orig,
                "trans": trans,
                "overlap": list(overlap),
                "is_trans_english": is_trans_english
            })

print(f"Shifted/mismatched English-on-English records: {len(quest_mismatches)}")
for m in quest_mismatches:
    print(f"\n[{m['type']}] {m['form_id']} ({m['edid']})")
    print(f"  ORIG:  {m['orig']}")
    print(f"  TRANS: {m['trans']}")
