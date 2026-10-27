import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

subphase_2b_mods = [
    'CCQuest - Experience Patch.esp - French',
    'Nolvus Awakening Experience Integration - French',
    'Lucien - Creation Club Patch',
    'Vokrii - Apply Spell Conditions Fix.esp - French',
    'Wintersun - Description Fixes',
    'Wintersun - Tribunal Integration',
    'Complete Crafting Overhaul Remastered - Immersive Sounds Patch - French',
    'Creation Club Crossbow Integration - French',
    'Navigator - Navmesh Fixes',
    'Eating Animations and Sounds - Patch Collection - French'
]

base_dir = 'data/user/database/french'

# Quick analysis of active files and strings
print("=== Sous-phase 2B : Inventaire des Fichiers & Chaînes ===")
total_records = 0
for mod in subphase_2b_mods:
    mod_dir = os.path.join(base_dir, mod)
    if not os.path.exists(mod_dir):
        print(f"Directory not found: {mod}")
        continue
    files = [f for f in os.listdir(mod_dir) if f.endswith('.json')]
    mod_tot = 0
    for fn in files:
        data = json.load(open(os.path.join(mod_dir, fn), encoding='utf-8'))
        mod_tot += len(data)
    total_records += mod_tot
    print(f" - {mod} : {len(files)} fichier(s), {mod_tot} chaînes")

print(f"\nTotal Sous-phase 2B : {total_records} enregistrements.")
