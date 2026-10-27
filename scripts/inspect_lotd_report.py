import json

with open("lotd_mismatch_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

print("=== SAMPLE VARIABLE MISMATCHES (first 10) ===")
for item in report["var_mismatches"][:10]:
    print(f"[{item['type']}] ({item['form_id']})")
    print(f"  Orig:  {item['orig']}")
    print(f"  Trans: {item['trans']}")
    print(f"  Orig Vars:  {item['orig_vars']}")
    print(f"  Trans Vars: {item['trans_vars']}")
    print()

print("=== SAMPLE NUMERIC MISMATCHES (first 10) ===")
for item in report["num_mismatches"][:10]:
    print(f"[{item['type']}] ({item['form_id']})")
    print(f"  Orig:  {item['orig']}")
    print(f"  Trans: {item['trans']}")
    print(f"  Orig Nums:  {item['orig_nums']}")
    print(f"  Trans Nums: {item['trans_nums']}")
    print()
