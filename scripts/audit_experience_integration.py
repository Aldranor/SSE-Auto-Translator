import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

f1 = 'data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json'
f2 = 'data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json'

for path in [f1, f2]:
    print(f"\n=======================================================")
    print(f"File: {path}")
    print(f"=======================================================")
    if not os.path.exists(path):
        print("DOES NOT EXIST")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    entries = [x for x in data if x.get('form_id') == '1D000F18|ccbgssse013-dawnfang.esl']
    print(f"Total Dawnfang 1D000F18 entries: {len(entries)}")
    for i, x in enumerate(entries):
        idx = x.get('index')
        typ = x.get('type')
        orig = str(x.get('original'))
        curr = str(x.get('string'))
        print(f"[{i}] index={idx} | type={typ}")
        print(f"     orig: {orig[:80]}")
        print(f"     curr: {curr[:80]}")
