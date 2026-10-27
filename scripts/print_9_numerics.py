import json

with open("lotd_reset_audit_report.json", "r", encoding="utf-8") as f:
    rep = json.load(f)

for i, x in enumerate(rep["gameplay_num_diffs"]):
    print(f"--- NUMERIC {i+1} ---")
    print(f"Type: {x['type']} | FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print(f"  Orig nums:  {x['orig_nums']}")
    print(f"  Trans nums: {x['trans_nums']}")
    print()
