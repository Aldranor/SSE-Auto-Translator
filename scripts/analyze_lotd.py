import json
import re
from pathlib import Path

lotd_json = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")

with open(lotd_json, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total entries in LegacyoftheDragonborn.esm.json: {len(data)}")

# 1. Variables mismatch (<...>, %s, etc.)
VAR_PATTERNS = [
    r"<[a-zA-Z0-9_\-=]+>",
    r"\[[a-zA-Z0-9_\-]+\]",
    r"%[0-9]*[sdf]",
    r"\$[a-zA-Z0-9_]+",
]

var_mismatches = []
num_mismatches = []
untranslated = []
suspicious_mismatches = []

for s in data:
    orig = s.get("original") or ""
    trans = s.get("string") or ""
    t = s.get("type") or ""
    status = s.get("status") or ""
    form_id = s.get("form_id") or ""
    edid = s.get("editor_id") or ""
    
    # Check variables
    for pat in VAR_PATTERNS:
        orig_vars = set(re.findall(pat, orig))
        trans_vars = set(re.findall(pat, trans))
        if orig_vars != trans_vars:
            var_mismatches.append({
                "form_id": form_id,
                "type": t,
                "orig": orig,
                "trans": trans,
                "orig_vars": list(orig_vars),
                "trans_vars": list(trans_vars)
            })
            break
            
    # Check numbers (e.g. 50 in orig, 25 in trans or vice versa)
    orig_nums = set(re.findall(r"\b\d+(?:[\.,]\d+)?\b", orig))
    trans_nums = set(re.findall(r"\b\d+(?:[\.,]\d+)?\b", trans))
    # Filter out formatting differences like 1.5 vs 1,5
    normalized_orig_nums = {n.replace(",", ".") for n in orig_nums}
    normalized_trans_nums = {n.replace(",", ".") for n in trans_nums}
    if normalized_orig_nums != normalized_trans_nums and len(orig_nums) > 0:
        # Check if it's not just a date or roman numeral
        if any(w in orig.lower() for w in ["damage", "health", "magicka", "stamina", "increase", "reduce", "percent", "%", "points", "seconds", "level", "cost"]):
            num_mismatches.append({
                "form_id": form_id,
                "type": t,
                "orig": orig,
                "trans": trans,
                "orig_nums": list(orig_nums),
                "trans_nums": list(trans_nums)
            })
            
    # Check status
    if status in ("TranslationIncomplete", "TranslationRequired") or not trans or trans == orig:
        untranslated.append({
            "form_id": form_id,
            "type": t,
            "status": status,
            "orig": orig,
            "trans": trans
        })

print(f"Variable mismatches: {len(var_mismatches)}")
print(f"Number discrepancies (perks/spells/stats): {len(num_mismatches)}")
print(f"Untranslated or incomplete: {len(untranslated)}")

with open("lotd_mismatch_report.json", "w", encoding="utf-8") as out:
    json.dump({
        "var_mismatches": var_mismatches,
        "num_mismatches": num_mismatches,
        "untranslated": untranslated[:100]
    }, out, indent=2, ensure_ascii=False)
