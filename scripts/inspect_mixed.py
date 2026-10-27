import json
from collections import Counter

with open("grouped_untranslatable_mods.json", "r", encoding="utf-8") as f:
    data = json.load(f)

mixed = data["mixed_untranslatable"]
print(f"Total mixed: {len(mixed)}")

for item in mixed[:25]:
    counts_str = ", ".join(f"{k}: {v}" for k, v in item['counts'].items())
    print(f"\n{item['mod']} / {item['file']} ({item['total_incomplete']} strings) -> [{counts_str}]")
    if 'sample_skipped' in item:
        for cat, samples in item['sample_skipped'].items():
            print(f"    {cat}: {samples}")
