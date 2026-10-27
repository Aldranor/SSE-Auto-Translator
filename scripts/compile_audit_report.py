import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We gather the exact disk state for all records discussed in the audit

# 1. Experience Integration (19 records)
f1 = 'data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json'
with open(f1, 'r', encoding='utf-8') as f:
    d1 = json.load(f)

exp_entries = [x for x in d1 if x.get('form_id') == '1D000F18|ccbgssse013-dawnfang.esl']

# 2. Clothes Patch
f_clothes = 'data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json'
with open(f_clothes, 'r', encoding='utf-8') as f:
    d_clothes = json.load(f)

clothes_entries = [x for x in d_clothes if x.get('form_id') in ('0303C0F1|Dragonborn.esm', '0303C0F2|Dragonborn.esm')]

# 3. CCQuest Graycowl
f_cc = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(f_cc, 'r', encoding='utf-8') as f:
    d_cc = json.load(f)
cc_entries = [x for x in d_cc if x.get('form_id') == '1000080F|ccbgssse020-graycowl.esl' and x.get('type') == 'QUST CNAM']

print(f"Experience Integration records on disk: {len(exp_entries)}")
print(f"Clothes Patch records on disk: {len(clothes_entries)}")
print(f"CCQuest Graycowl QUST CNAM records on disk: {len(cc_entries)}")
