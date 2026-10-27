import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Re-run or check target mods directly
target_mods = [
    'Nolvus Awakening Gourmet Integration - French',
    'Nolvus Awakening Stances Perk System.esp - French',
    'Nolvus Awakening Ashes of War Stance Framework.esp - French',
    'Nolvus Awakening Seasonal Plant Mashup - French',
    'Nolvus Awakening Custom Outfits.esp - French',
    'Nolvus Awakening Lighting Patch - French',
    'Nolvus Awakening Clothes Balance Patch - French'
]

base_dir = 'data/user/database/french'

for mod in target_mods:
    mod_dir = os.path.join(base_dir, mod)
    if not os.path.exists(mod_dir):
        continue
    files = [f for f in os.listdir(mod_dir) if f.endswith('.json')]
    for fn in files:
        fp = os.path.join(mod_dir, fn)
        data = json.load(open(fp, encoding='utf-8'))
        print(f"\n--- {mod} / {fn} ({len(data)} entries) ---")
        for item in data:
            orig = item.get('original') or ''
            curr = item.get('string') or ''
            fid = item.get('form_id') or ''
            typ = item.get('type') or ''
            # Check untranslated, suspicious, or brackets
            if orig == curr and len(orig) > 3 and not typ.startswith('NPC_'):
                print(f"  [IDENTICAL] {fid} ({typ}): {orig}")
            if any(k in curr.lower() for k in ['endurance', 'mana', 'montagne rouge']):
                print(f"  [LORE/TERM] {fid} ({typ}): {curr}")
            if '[' in curr and ']' in curr and '[' not in orig:
                print(f"  [BRACKET] {fid} ({typ}): {curr}")
