import json
from collections import defaultdict

with open('english_and_poor_translations.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group by mod
by_mod = defaultdict(list)
for x in items:
    by_mod[x['mod']].append(x)

print(f"Total mods with untranslated English: {len(by_mod)}")
sorted_mods = sorted(by_mod.items(), key=lambda kv: len(kv[1]), reverse=True)
for mod_name, list_items in sorted_mods[:20]:
    print(f"Mod '{mod_name}': {len(list_items)} strings")
    for s in list_items[:3]:
        print(f"   [{s['type']}] {s['original']} -> {s['translation']}")
    print()
