import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)

dawn = [x for x in d if 'dawnfang' in x.get('form_id', '').lower()]
print(f"Found {len(dawn)} dawnfang entries in ccquest:")
for x in dawn:
    print(f"type={x.get('type')} | index={x.get('index')}")
    print(f"  orig: {x.get('original')}")
    print(f"  str : {x.get('string')}")
