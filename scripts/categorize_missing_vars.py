import json
from collections import Counter

with open("lotd_reset_audit_report.json", "r", encoding="utf-8") as f:
    rep = json.load(f)

missing = rep["missing_variables"]
var_types = Counter()
for x in missing:
    for v in x["missing"]:
        var_types[v] += 1

print("Top missing variables in French translation:")
for v, c in var_types.most_common(20):
    print(f"  {v}: {c}")

print("\nSamples of missing variables:")
for x in missing[:10]:
    print(f"[{x['type']}] ({x['form_id']}) - Missing: {x['missing']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print()
