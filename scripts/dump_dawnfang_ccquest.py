import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
d = json.load(open(p, encoding='utf-8'))
dawnfang_ccquest = [x for x in d if 'dawnfang' in x.get('form_id', '').lower()]

for x in dawnfang_ccquest:
    print(f"FormID: {x['form_id']} | Type: {x['type']} | Index: {x.get('index')}")
    print(f"  ORIG: {x['original']}")
    print(f"  STR:  {x['string']}")
    print("-" * 50)
