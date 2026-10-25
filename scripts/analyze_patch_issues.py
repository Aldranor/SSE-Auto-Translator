import json
from collections import Counter

with open('patch_gameplay_issues.json', 'r', encoding='utf-8') as f:
    issues = json.load(f)

print(f"Total patch gameplay issues: {len(issues)}")

types = Counter(x['issue'] for x in issues)
for t, c in types.most_common():
    print(f"  {t}: {c}")

mod_counts = Counter(x['mod'] for x in issues)
print("\nTop 15 patch mods with gameplay issues:")
for m, c in mod_counts.most_common(15):
    print(f"  {m}: {c}")

print("\nSample 20 concrete patch issues:")
for x in issues[:20]:
    print(f"[{x['mod']}] {x['file']} ({x['type']}) - {x['issue']}")
    print(f"  EN: {x['original']}")
    print(f"  FR: {x['translation']}")
    if 'en_nums' in x:
        print(f"  Diff nums: EN {x['en_nums']} vs FR {x['fr_nums']}")
    print("-" * 50)
