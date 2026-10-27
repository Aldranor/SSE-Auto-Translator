import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = 'data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json'
data = json.load(open(p, encoding='utf-8'))
for x in data:
    orig = str(x.get('original'))
    fid = str(x.get('form_id'))
    if 'Miraak' in orig or '0303C0F' in fid:
        print(f"{fid} | {x.get('type')} | index={x.get('index')}")
        print(f"   orig: {orig}")
        print(f"   curr: {x.get('string')}")
