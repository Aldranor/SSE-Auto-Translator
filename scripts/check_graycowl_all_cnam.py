import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p_ccquest = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(p_ccquest, 'r', encoding='utf-8') as f:
    d_ccquest = json.load(f)

graycowl_entries = [x for x in d_ccquest if 'ccbgssse020-graycowl.esl' in x.get('form_id', '').lower() and x.get('type') == 'QUST CNAM']
print(f"Total Graycowl QUST CNAM in CCQuest: {len(graycowl_entries)}")
for i, x in enumerate(graycowl_entries):
    print(f"[{i}] index={x.get('index')}")
    print(f"    orig: {x.get('original')[:80]}")
    print(f"    str : {x.get('string')[:80]}")
