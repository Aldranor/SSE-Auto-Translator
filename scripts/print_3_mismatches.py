import json

with open("lotd_reset_audit_report.json", "r", encoding="utf-8") as f:
    rep = json.load(f)

for i, x in enumerate(rep["other_mismatches"]):
    print(f"--- MATCH {i+1} ---")
    print(f"Type: {x['type']} | FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"Orig: {x['orig'][:300]}")
    print(f"Trans: {x['trans'][:300]}")
    print()
