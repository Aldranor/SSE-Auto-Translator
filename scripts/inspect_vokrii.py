import json

with open('perks_spells_number_fixes.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for mod_name in ['Vokriinateur - Morceaux choisis', 'Vokrii - Atouts minimalistes', 'Ordonnateur - Atouts de Bordeciel']:
    sub = [x for x in items if mod_name in x['mod']]
    print(f"=== {mod_name} ({len(sub)}) ===")
    for x in sub[:5]:
        print(f"  EN: {x['original']}")
        print(f"  FR: {x['translation']}")
        print(f"  Nums: EN {x['orig_nums']} vs FR {x['trans_nums']}\n")
