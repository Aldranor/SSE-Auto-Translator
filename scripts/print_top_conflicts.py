import json

with open('name_consistency_conflicts.json', 'r', encoding='utf-8') as f:
    conflicts = json.load(f)

with open('top_conflicts_report.txt', 'w', encoding='utf-8') as out:
    for cat_name in ['Locations', 'Perks_Skills', 'Spells_Magic']:
        out.write(f"\n==================== TOP CONFLICTS: {cat_name} ====================\n")
        # Sort by number of variants and total occurrences
        sorted_items = sorted(
            conflicts[cat_name],
            key=lambda x: sum(v['count'] for v in x['variants']),
            reverse=True
        )
        for item in sorted_items[:30]:
            total = sum(v['count'] for v in item['variants'])
            out.write(f"EN: '{item['original']}' (Total: {total})\n")
            for v in item['variants']:
                mods_str = ", ".join(v['mods'][:3])
                out.write(f"   -> [{v['count']}x] '{v['translation']}' in ({mods_str})\n")
            out.write("\n")

print("Generated top_conflicts_report.txt")
