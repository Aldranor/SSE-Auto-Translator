import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

f_cc = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(f_cc, 'r', encoding='utf-8') as f:
    cc_data = json.load(f)

# Extract translations from CCQuest
dawnfang_map = {}
for x in cc_data:
    if 'dawnfang' in x.get('form_id', '').lower():
        k = (x.get('type'), x.get('index'), x.get('original'))
        dawnfang_map[k] = x.get('string')

print(f"Loaded {len(dawnfang_map)} Dawnfang reference entries from CCQuest.")

files_to_restore = [
    'data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json',
    'data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json'
]

log_changes = []

for filepath in files_to_restore:
    print(f"\nProcessing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified_count = 0
    unchanged_105_count = 0
    
    for item in data:
        if item.get('form_id') == '1D000F18|ccbgssse013-dawnfang.esl':
            typ = item.get('type')
            idx = item.get('index')
            orig = item.get('original')
            old_str = item.get('string')
            k = (typ, idx, orig)
            
            if typ == 'QUST CNAM' and idx == 105:
                print(f"  [KEEP] Index 105 journal stage kept as: {old_str[:60]}...")
                unchanged_105_count += 1
                continue
            
            if k in dawnfang_map:
                new_str = dawnfang_map[k]
                item['string'] = new_str
                item['status'] = 'TranslationComplete'
                modified_count += 1
                log_changes.append({
                    'file': os.path.basename(filepath),
                    'form_id': item.get('form_id'),
                    'type': typ,
                    'index': idx,
                    'original': orig,
                    'before': old_str,
                    'after': new_str
                })
            else:
                print(f"  [ERROR] Key {k} not found in dawnfang_map!")
                sys.exit(1)
    
    print(f"Summary for {os.path.basename(filepath)}: Modified {modified_count} entries, kept {unchanged_105_count} (index 105).")
    assert modified_count == 18, f"Expected 18 modified, got {modified_count}"
    assert unchanged_105_count == 1, f"Expected 1 kept, got {unchanged_105_count}"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved {filepath}.")

print("\n--- POST-VERIFICATION OF WRITTEN FILES ON DISK ---")
for filepath in files_to_restore:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    entries = [x for x in data if x.get('form_id') == '1D000F18|ccbgssse013-dawnfang.esl']
    print(f"\n{os.path.basename(filepath)} has {len(entries)} entries:")
    unique_strings = set(x.get('string') for x in entries)
    print(f"  Number of unique strings: {len(unique_strings)} (must be 19)")
    assert len(unique_strings) == 19, "Entries still have duplicate strings!"
    for x in entries:
        print(f"  type={x.get('type'):10} | idx={str(x.get('index')):5} | str={x.get('string')[:50]}")

print("\nAll Experience Integration Dawnfang entries restored and verified successfully!")
