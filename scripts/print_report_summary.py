import json

with open('refined_audit_report.json', 'r', encoding='utf-8') as f:
    r = json.load(f)

print('=== FALSE FRIENDS ===')
for item in r['false_friends']:
    print(f"{item['mod']} :: {item['file']}: {item['original']} -> {item['current']} (Propos: {item['proposal']})")

print('\n=== SYNTAX CALQUES ===')
for item in r['syntax_calques']:
    print(f"{item['mod']} :: {item['file']}: {item['original']} -> {item['current']} (Propos: {item['proposal']})")

print('\n=== SAMPLE BROKEN VARIABLES WITH ILLEGAL NUMERICS ===')
illegal_num = [item for item in r['broken_variables'] if 'Balises numériques illégales' in item['reason']]
print(f"Total illegal numeric tags: {len(illegal_num)}")
for item in illegal_num[:5]:
    print(f"{item['mod']} :: {item['file']}:")
    print(f"  Orig: {item['original']}")
    print(f"  Trad: {item['current']}")
    print(f"  Propos: {item['proposal']}")

print('\n=== SAMPLE UNTRANSLATED IN PATCHES ===')
for item in r['untranslated_in_patches'][:10]:
    print(f"{item['mod']} :: {item['file']}: {item['original']} -> {item['current']}")

print('\n=== SAMPLE INTERNAL INCONSISTENCIES ===')
for item in r['mod_inconsistencies'][:10]:
    print(f"{item['mod']} :: {item['file']}: '{item['original']}' -> {item['variants']}")
