import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect all touched files in 2B and 2C

files_to_audit = [
    # 2B
    ('CCQuest', 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'),
    ('Eat DOS', 'data/user/database/french/Eating Animations and Sounds - Patch Collection - French/taberu animation - dawn of skyrim patch.esp.json'),
    ('Eat Cheese', 'data/user/database/french/Eating Animations and Sounds - Patch Collection - French/taberu animation - cheesemod patch.esp.json'),
    ('Navigator 1', 'data/user/database/french/Navigator - Navmesh Fixes/navigator-navfixes.esl.json'),
    ('Navigator 2', 'data/user/database/french/Navigator - Navmesh Fixes - French/Navigator-NavFixes.esl.json'),
    ('Wintersun', 'data/user/database/french/Wintersun - Tribunal Integration/wintersun - gott patch.esp.json'),
    ('CCOR ISC', 'data/user/database/french/Complete Crafting Overhaul Remastered - Immersive Sounds Patch - French/ImmersiveSoundsCompendium_CCOR_Patch.esp.json'),
    # 2C
    ('Water 1', 'data/user/database/french/Water for ENB [4K] - French/Water for ENB (Shades of Skyrim).esp.json'),
    ('Water 2', 'data/user/database/french/Water for ENB [4K]/water for enb (shades of skyrim).esp.json'),
    ('Embers XD', 'data/user/database/french/Embers XD - French/Embers XD.esp.json'),
    ('Lux Mistveil', "data/user/database/french/Lux - Patch Hub - French/Lux - JK's Mistveil Keep patch.esp.json"),
    ('Lux Dibella', "data/user/database/french/Lux - Patch Hub - French/Lux - JK's Temple of Dibella patch.esp.json"),
    ('Lux Distinct', "data/user/database/french/Lux - Patch Hub - French/Lux - Distinct Interiors patch.esp.json"),
    ('Lux College', "data/user/database/french/Lux - Patch Hub - French/Lux - JK's College patch.esp.json"),
    ('Lux Anga', "data/user/database/french/Lux - Patch Hub - French/Lux - Anga's Mill COTN patch.esp.json"),
    # Clothes patch
    ('Clothes Patch', 'data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json'),
    # Experience Integration
    ('Exp Int 1', 'data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json'),
    ('Exp Int 2', 'data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json'),
]

for label, fpath in files_to_audit:
    print(f"\n==========================================")
    print(f"FILE: {label} -> {fpath}")
    print(f"==========================================")
    if not os.path.exists(fpath):
        print("FILE NOT FOUND!")
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Total entries: {len(data)}")
    
    # Check for duplicate FormIDs in this file
    form_id_counts = {}
    for item in data:
        fid = item.get('form_id')
        form_id_counts[fid] = form_id_counts.get(fid, 0) + 1
    
    multi_fids = {fid: c for fid, c in form_id_counts.items() if c > 1}
    print(f"FormIDs appearing multiple times: {len(multi_fids)}")
    for fid, c in list(multi_fids.items())[:10]:
        types = [x.get('type') for x in data if x.get('form_id') == fid]
        indices = [x.get('index') for x in data if x.get('form_id') == fid]
        print(f"   {fid}: {c} times | types={types} | indices={indices}")
