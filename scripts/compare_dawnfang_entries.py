import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

f_cc = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(f_cc, 'r', encoding='utf-8') as f:
    cc_data = json.load(f)

cc_dawn = {
    (x.get('type'), x.get('index')): (x.get('original'), x.get('string'))
    for x in cc_data if 'dawnfang' in x.get('form_id', '').lower()
}

f1 = 'data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json'
f2 = 'data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json'

for path in [f1, f2]:
    print(f"\nComparing {path} with CCQuest:")
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entries = [x for x in data if x.get('form_id') == '1D000F18|ccbgssse013-dawnfang.esl']
    print(f"Total entries: {len(entries)}")
    for x in entries:
        k = (x.get('type'), x.get('index'))
        if k not in cc_dawn:
            print(f"  NOT IN CC: {k}")
        else:
            orig_cc, str_cc = cc_dawn[k]
            orig_here = x.get('original')
            if orig_cc.strip() != orig_here.strip():
                print(f"  ORIG MISMATCH at {k}:\n    CC:   {repr(orig_cc)}\n    HERE: {repr(orig_here)}")
            else:
                pass
print("Comparison completed.")
