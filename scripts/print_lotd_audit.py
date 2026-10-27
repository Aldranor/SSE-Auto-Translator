import json

with open("lotd_deep_audit.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== 1. BROKEN / CORRUPTED VARIABLES (Top 12) ===")
for x in data["broken_vars"][:12]:
    print(f"[{x['type']}] FormID: {x['form_id']} (EDID: {x['edid']})")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    if x['missing_vars']:
        print(f"  --> MANQUE variable: {x['missing_vars']}")
    if x['bogus_tags']:
        print(f"  --> BALISES INVENTEES: {x['bogus_tags']}")
    print()

print("\n=== 2. NUMERIC DISCREPANCIES IN GAMEPLAY (Top 12) ===")
for x in data["numeric_discrepancies"][:12]:
    print(f"[{x['type']}] FormID: {x['form_id']} (EDID: {x['edid']})")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print(f"  --> Orig: {x['orig_nums']} vs Trans: {x['trans_nums']}")
    print()

print("\n=== 3. SEMANTIC INVERSIONS (Top 12) ===")
for x in data["semantic_mismatches"][:12]:
    print(f"[{x['type']}] {x['rule']} | FormID: {x['form_id']} (EDID: {x['edid']})")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print()

print("\n=== 4. UNTRANSLATED ENGLISH (Top 12) ===")
for x in data["untranslated_english"][:12]:
    print(f"[{x['type']}] FormID: {x['form_id']} (EDID: {x['edid']})")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print()
