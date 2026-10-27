import json
from collections import defaultdict

with open("lotd_all_missing.json", "r", encoding="utf-8") as f:
    items = json.load(f)

by_type = defaultdict(list)
for x in items:
    by_type[x["type"]].append(x)

print(f"Total: {len(items)}")
for t, group in sorted(by_type.items(), key=lambda x: -len(x[1])):
    print(f"\n=== {t} ({len(group)} items) ===")
    for item in group:
        print(f"[{item['form_id']}] ({item['edid']}): {repr(item['original'][:120])}")
