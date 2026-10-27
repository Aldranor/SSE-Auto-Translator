import json

with open("lotd_deep_audit.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total semantic: {len(data['semantic_mismatches'])}")

# Filter out false positives from semantic mismatches
# Many might just be normal sentences containing both words
real_semantic = []
for x in data["semantic_mismatches"]:
    orig = x["orig"]
    trans = x["trans"]
    t = x["type"]
    if t.startswith("BOOK"):
        continue
    rule = x["rule"]
    real_semantic.append(x)

print(f"Non-book semantic: {len(real_semantic)}")
for x in real_semantic[:25]:
    print(f"[{x['type']}] Rule: {x['rule']} | FormID: {x['form_id']} | EDID: {x['edid']}")
    print(f"  Orig:  {x['orig']}")
    print(f"  Trans: {x['trans']}")
    print()
