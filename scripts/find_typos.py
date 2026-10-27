import json
import re

path = "data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json"
data = json.load(open(path, encoding="utf-8"))

typos = []
for idx, e in enumerate(data):
    s = e.get("string") or ""
    orig = e.get("original") or ""
    
    # Check coeur / soeur
    if re.search(r"\bcoeur", s, re.IGNORECASE):
        typos.append((idx, "LIGATURE_COEUR", orig, s))
    if re.search(r"\bsoeur", s, re.IGNORECASE):
        typos.append((idx, "LIGATURE_SOEUR", orig, s))
    
    # Check double spaces
    if "  " in s:
        typos.append((idx, "DOUBLE_SPACE", orig, s))
        
    # Check weird characters
    if "" in s:
        typos.append((idx, "MOJIBAKE", orig, s))

print(f"Typo/format findings: {len(typos)}")
for t in typos:
    print(f"[{t[1]}] #{t[0]}: {repr(t[2])} -> {repr(t[3])}")
