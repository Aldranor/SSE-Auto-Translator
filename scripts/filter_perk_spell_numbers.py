import json
import re

with open('real_numeric_discrepancies.json', 'r', encoding='utf-8') as f:
    discrepancies = json.load(f)

perks_spells_rebalance = []

for d in discrepancies:
    rec_type = d.get('type') or ''
    # Only keep descriptions of perks, spells, magic effects, enchantments, actor values
    if any(t in rec_type for t in ['PERK', 'SPEL', 'MGEF', 'ENCH']):
        # Filter out cases where French just wrote "5 000" with a space which caused "5" and "000"
        o_nums = d['orig_nums']
        t_nums = d['trans_nums']
        if '000' in t_nums:
            continue
        # Also skip if translation is just missing or English
        if d['original'] == d['translation']:
            continue
        perks_spells_rebalance.append(d)

print(f"Total Perks/Spells with rebalanced/divergent numbers: {len(perks_spells_rebalance)}")

with open('perks_spells_number_fixes.json', 'w', encoding='utf-8') as f:
    json.dump(perks_spells_rebalance, f, indent=2, ensure_ascii=False)

for item in perks_spells_rebalance[:25]:
    print(f"[{item['mod']}] {item['file']} ({item['type']})")
    print(f"  EN: {item['original']}")
    print(f"  FR: {item['translation']}")
    print(f"  Diff: EN {item['orig_nums']} vs FR {item['trans_nums']}")
    print()
