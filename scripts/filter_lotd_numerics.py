import json
import re

with open("lotd_deep_audit.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== REAL NUMERIC MISMATCHES (PERKS, SPELLS, ENCHANTMENTS, WEAPONS) ===")
real_num = []
for x in data["numeric_discrepancies"]:
    t = x["type"]
    if t.startswith("BOOK"):
        continue
    orig = x["orig"]
    trans = x["trans"]
    # Check if there are real differing numbers
    real_num.append(x)

print(f"Total non-book numeric discrepancies: {len(real_num)}")
for x in real_num[:20]:
    print(f"[{x['type']}] FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print(f"  Numbers: Orig {x['orig_nums']} vs Trans {x['trans_nums']}")
    print()
