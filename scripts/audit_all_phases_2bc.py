import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Clothes Patch
print("=== 1. CLOTHES PATCH ===")
p_clothes = 'data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json'
with open(p_clothes, 'r', encoding='utf-8') as f:
    d_clothes = json.load(f)

for x in d_clothes:
    if '0303C0F' in x.get('form_id', ''):
        print(f"ID: {x.get('form_id')} | Type: {x.get('type')} | Orig: {x.get('original')} | String: {x.get('string')}")

# 2. Check CCQuest Graycowl
print("\n=== 2. CCQUEST GRAYCOWL ===")
p_ccquest = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(p_ccquest, 'r', encoding='utf-8') as f:
    d_ccquest = json.load(f)

for x in d_ccquest:
    if 'ccbgssse020-graycowl.esl' in x.get('form_id', '').lower():
        print(f"ID: {x.get('form_id')} | Type: {x.get('type')} | Index: {x.get('index')} | Orig: {x.get('original')[:40]} | String: {x.get('string')[:40]}")

# 3. Check Eating Animations
print("\n=== 3. EATING ANIMATIONS ===")
p_eat = 'data/user/database/french/Eating Animations and Sounds SE.esp - French/eating animations and sounds se.esp.json'
if os.path.exists(p_eat):
    with open(p_eat, 'r', encoding='utf-8') as f:
        d_eat = json.load(f)
    print(f"Total entries in Eating Animations: {len(d_eat)}")
    for x in d_eat:
        # print if modified or check form_ids
        print(f"ID: {x.get('form_id')} | Type: {x.get('type')} | Index: {x.get('index')} | Orig: {x.get('original')} | String: {x.get('string')}")
else:
    print(f"File not found: {p_eat}")

# 4. Check Navigator
print("\n=== 4. NAVIGATOR ===")
p_nav = 'data/user/database/french/Navigator - NavMesh Fixes.esp - French/navigator - navmesh fixes.esp.json'
if os.path.exists(p_nav):
    with open(p_nav, 'r', encoding='utf-8') as f:
        d_nav = json.load(f)
    print(f"Total entries in Navigator: {len(d_nav)}")
    for x in d_nav:
        print(f"ID: {x.get('form_id')} | Type: {x.get('type')} | Index: {x.get('index')} | Orig: {x.get('original')} | String: {x.get('string')}")

# 5. Check Wintersun
print("\n=== 5. WINTERSUN ===")
p_wintersun = 'data/user/database/french/Wintersun - Faiths of Skyrim.esp - French/wintersun - faiths of skyrim.esp.json'
if os.path.exists(p_wintersun):
    with open(p_wintersun, 'r', encoding='utf-8') as f:
        d_w = json.load(f)
    # Check what was touched in phase 2b
    # Let's inspect apply_subphase_2b_fixes.py to know what was touched
