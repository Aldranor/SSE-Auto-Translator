import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
data = json.load(open(p, encoding='utf-8'))

graycowl_entries = [x for x in data if x.get('form_id') == '1000080F|ccbgssse020-graycowl.esl']
print(f"Total Gray Cowl entries: {len(graycowl_entries)}")
for i, x in enumerate(graycowl_entries):
    print(f"[{i}] index={x.get('index')} | type={x.get('type')}")
    print(f"     orig: {x.get('original')[:80]}")
    print(f"     curr: {x.get('string')[:80]}")
