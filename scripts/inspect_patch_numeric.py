import json

with open('patch_gameplay_issues.json', 'r', encoding='utf-8') as f:
    issues = json.load(f)

numeric_issues = [x for x in issues if x['issue'] == 'Numeric discrepancy in patch gameplay text']
print(f"Total numeric issues in patches: {len(numeric_issues)}\n")

for x in numeric_issues:
    # Filter out book pages or logs if not perk/spell
    if any(t in (x.get('type') or '') for t in ['PERK', 'SPEL', 'MGEF', 'ENCH', 'ALCH', 'AVIF', 'WEAP', 'ARMO']):
        print(f"[{x['mod']}] {x['file']} ({x['type']})")
        print(f"  EN ({x['en_nums']}): {x['original']}")
        print(f"  FR ({x['fr_nums']}): {x['translation']}")
        print("-" * 50)
