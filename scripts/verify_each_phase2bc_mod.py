import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will check every single modification recorded in recap_2b and recap_2c

with open('scripts/apply_subphase_2b_fixes.py', 'r', encoding='utf-8') as f:
    text_2b = f.read()

with open('scripts/apply_subphase_2c_fixes.py', 'r', encoding='utf-8') as f:
    text_2c = f.read()

print("Verifying 2B and 2C modifications on disk...")

# 1. CCQuest
p = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)
matches = [x for x in d if x.get('form_id') == '1000080F|ccbgssse020-graycowl.esl']
print(f"\nCCQuest Graycowl: total {len(matches)} entries.")
for x in matches:
    print(f"  type={x.get('type')} index={x.get('index')} orig={x.get('original')[:30]} -> {x.get('string')[:30]}")

# 2. Eating Animations DOS
p = 'data/user/database/french/Eating Animations and Sounds - Patch Collection - French/taberu animation - dawn of skyrim patch.esp.json'
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)
dos_fids = ['02020D57|Dawn of Skyrim.esp', '02020D54|Dawn of Skyrim.esp', '0201DE7F|Dawn of Skyrim.esp', 
            '0201DE83|Dawn of Skyrim.esp', '0201DE85|Dawn of Skyrim.esp', '0201DE87|Dawn of Skyrim.esp', 
            '0201DE7A|Dawn of Skyrim.esp', '0201DE81|Dawn of Skyrim.esp']
print(f"\nEating Animations DOS:")
for fid in dos_fids:
    m = [x for x in d if x.get('form_id') == fid]
    print(f"  {fid}: count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")

# 3. Eating Animations Cheesemod
p = 'data/user/database/french/Eating Animations and Sounds - Patch Collection - French/taberu animation - cheesemod patch.esp.json'
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)
cheese_fids = ['02003782|yumcheese.esp', '02003786|yumcheese.esp']
print(f"\nEating Animations Cheese:")
for fid in cheese_fids:
    m = [x for x in d if x.get('form_id') == fid]
    print(f"  {fid}: count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")

# 4. Navigator
for nav_p in ['data/user/database/french/Navigator - Navmesh Fixes/navigator-navfixes.esl.json',
              'data/user/database/french/Navigator - Navmesh Fixes - French/Navigator-NavFixes.esl.json']:
    if os.path.exists(nav_p):
        with open(nav_p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        nav_fids = ['0001529F|Skyrim.esm', '000466CB|Skyrim.esm', '0002164A|Skyrim.esm']
        print(f"\nNavigator ({nav_p}):")
        for fid in nav_fids:
            m = [x for x in d if x.get('form_id') == fid]
            print(f"  {fid}: count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")

# 5. Wintersun
p = 'data/user/database/french/Wintersun - Tribunal Integration/wintersun - gott patch.esp.json'
if os.path.exists(p):
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    w_fids = ['05000849|Wintersun - GotT Patch.esp', '05000879|Wintersun - GotT Patch.esp', '0406AD19|Wintersun - Faiths of Skyrim.esp']
    print(f"\nWintersun:")
    for fid in w_fids:
        m = [x for x in d if x.get('form_id') == fid]
        print(f"  {fid}: count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")

# 6. CCOR ISC
p = 'data/user/database/french/Complete Crafting Overhaul Remastered - Immersive Sounds Patch - French/ImmersiveSoundsCompendium_CCOR_Patch.esp.json'
if os.path.exists(p):
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    ccor_fids = ['000F6904|Skyrim.esm', '000F690D|Skyrim.esm', '000F690E|Skyrim.esm', '000F690F|Skyrim.esm', '000F6910|Skyrim.esm', '000F6911|Skyrim.esm']
    print(f"\nCCOR ISC:")
    for fid in ccor_fids:
        m = [x for x in d if x.get('form_id') == fid]
        print(f"  {fid}: count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")

# 7. Water for ENB
for wp in ['data/user/database/french/Water for ENB [4K] - French/Water for ENB (Shades of Skyrim).esp.json',
           'data/user/database/french/Water for ENB [4K]/water for enb (shades of skyrim).esp.json']:
    if os.path.exists(wp):
        with open(wp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        wfids = ['0001529F|Skyrim.esm', '00015265|Skyrim.esm', '0002BCD7|Skyrim.esm', '0005554A|Skyrim.esm']
        print(f"\nWater for ENB ({wp}):")
        for fid in wfids:
            m = [x for x in d if x.get('form_id') == fid]
            print(f"  {fid}: count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")

# 8. Embers XD
p = 'data/user/database/french/Embers XD - French/Embers XD.esp.json'
if os.path.exists(p):
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    m = [x for x in d if x.get('form_id') == '00015224|Skyrim.esm']
    print(f"\nEmbers XD: count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")

# 9. Lux patches
lux_hub_dir = 'data/user/database/french/Lux - Patch Hub - French'
lux_checks = [
    ("Lux - JK's Mistveil Keep patch.esp.json", '0003B87D|Skyrim.esm'),
    ("Lux - JK's Temple of Dibella patch.esp.json", '0003EA9D|Skyrim.esm'),
    ("Lux - Distinct Interiors patch.esp.json", '00013A71|Skyrim.esm'),
    ("Lux - JK's College patch.esp.json", '0002BCD7|Skyrim.esm'),
    ("Lux - JK's College patch.esp.json", '00013810|Skyrim.esm'),
    ("Lux - Anga's Mill COTN patch.esp.json", '00016209|Skyrim.esm')
]
print(f"\nLux Patches:")
for lfile, fid in lux_checks:
    lp = os.path.join(lux_hub_dir, lfile)
    if os.path.exists(lp):
        with open(lp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        m = [x for x in d if x.get('form_id') == fid]
        print(f"  {lfile} ({fid}): count={len(m)} -> {[(x.get('type'), x.get('index'), x.get('original'), x.get('string')) for x in m]}")
