import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = 'data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json'
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

matched = 0
for item in data:
    if (item.get('form_id') == '0303C0F2|Dragonborn.esm' and 
        item.get('type') == 'ARMO FULL' and 
        item.get('index') is None and 
        item.get('original') == "Miraak's Mask"):
        
        print(f"Found record to fix:")
        print(f"  FormID:   {item.get('form_id')}")
        print(f"  Type:     {item.get('type')}")
        print(f"  Index:    {item.get('index')}")
        print(f"  Original: {item.get('original')}")
        print(f"  Before:   {item.get('string')}")
        
        item['string'] = "Masque de Miraak"
        item['status'] = "TranslationComplete"
        print(f"  After:    {item.get('string')}")
        matched += 1

print(f"\nMatched and modified count: {matched}")
assert matched == 1, f"Expected 1 match, got {matched}"

with open(p, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved file successfully.")

# Post-verification on disk
with open(p, 'r', encoding='utf-8') as f:
    verify_data = json.load(f)

v_items = [x for x in verify_data if x.get('form_id') in ('0303C0F1|Dragonborn.esm', '0303C0F2|Dragonborn.esm')]
print("\n--- POST-VERIFICATION OF MIRAAK'S MASK ON DISK ---")
for x in v_items:
    print(f"{x.get('form_id')} | {x.get('type')} | {repr(x.get('original'))} -> {repr(x.get('string'))}")
