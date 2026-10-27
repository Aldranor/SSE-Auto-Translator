import json

with open("lotd_reset_audit_report.json", "r", encoding="utf-8") as f:
    rep = json.load(f)

print("=== 1. THE 3 OTHER MISMATCHED ENGLISH TEXTS ===")
for x in rep["other_mismatches"]:
    print(f"[{x['type']}] FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print()

print("\n=== 2. THE 9 GAMEPLAY NUMERIC DISCREPANCIES ===")
for x in rep["gameplay_num_diffs"]:
    print(f"[{x['type']}] FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print(f"  Nums:  Orig {x['orig_nums']} vs Trans {x['trans_nums']}")
    print()

print("\n=== 3. SAMPLE MISSING AUTHENTIC VARIABLES (First 10) ===")
for x in rep["missing_variables"][:10]:
    print(f"[{x['type']}] FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print(f"  Missing: {x['missing']}")
    print()

print("\n=== 4. SAMPLE BOGUS NUMBER TAGS (<10>, <25>, etc.) (First 10) ===")
for x in rep["bogus_tags_list"][:10]:
    print(f"[{x['type']}] FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print(f"  Bogus: {x['bogus']}")
    print()
