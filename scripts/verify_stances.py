import json

base_path = r'data/user/database/french/Stances - Dynamic Animation Sets/stances - dynamic weapon movesets se.esp.json'
addon_path = r'data/user/database/french/Stances - Add-On.esp - French/stances - add-on.esp.json'

with open(base_path, 'r', encoding='utf-8') as f:
    base = json.load(f)
with open(addon_path, 'r', encoding='utf-8') as f:
    addon = json.load(f)

print(f"=== BASE MOD ({len(base)} entries) ===")
assert all(e['status'] == 'TranslationComplete' for e in base)
for i, e in enumerate(base):
    print(f"[{i:2d}] {e['type']:9s} | {str(e['editor_id']):30s} | {repr(e['string'][:60])}")

print(f"\n=== ADDON MOD ({len(addon)} entries) ===")
assert all(e['status'] == 'TranslationComplete' for e in addon)
for i, e in enumerate(addon):
    print(f"[{i:2d}] {e['type']:9s} | {str(e['editor_id']):30s} | {repr(e['string'][:60])}")

print("\nALL ENTRIES VERIFIED AND COMPLETE (100%)!")
