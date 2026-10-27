import subprocess
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

files_to_stage = [
    # Documentation & Registries
    'PLAN_RELECTURE_FINALE.md',
    'TRADUCTIONS_VERIFIEES.md',
    'AUDIT_IMPACT_PHASES_2BC.md',
    'recap_modifications_phase1.md',
    'recap_modifications_phase2a.md',
    'recap_modifications_phase2b.md',
    'recap_modifications_phase2c.md',
    'recap_modifications_phase2d.md',
    'recap_modifications_phase2e.md',
    'phase0_global_scan_results.json',
    'audit_results_verified.json',
    'recap_phase2a_diffs.json',
    'recap_phase2d_diffs.json',
    'recap_phase2e_diffs.json',
    
    # Tracked DB files
    'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json',
    'data/user/database/french/Nolvus Awakening Armors Balance Patch.esp - French/nolvus awakening armors balance patch.esp.json',
    'data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - consistency patch.esp.json',
    'data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - enemy level mult.esp.json',
    'data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - enemy level.esp.json',
    'data/user/database/french/Nolvus Awakening Crafting Patch - French/nolvus awakening crafting patch.esp.json',
    'data/user/database/french/Nolvus Awakening Weapons Balance Patch.esp - French/nolvus awakening weapons balance patch.esp.json',
    'data/user/database/french/Nolvus Awakening Weapons Patch - French/nolvus awakening weapons patch.esp.json',

    # Untracked DB files from Phase 2 (use -f)
    'data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json',
    'data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json',
    'data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json',
    'data/user/database/french/Eating Animations and Sounds - Patch Collection - French/taberu animation - dawn of skyrim patch.esp.json',
    'data/user/database/french/Eating Animations and Sounds - Patch Collection - French/taberu animation - cheesemod patch.esp.json',
    'data/user/database/french/Navigator - Navmesh Fixes/navigator-navfixes.esl.json',
    'data/user/database/french/Wintersun - Tribunal Integration/wintersun - gott patch.esp.json',
    'data/user/database/french/Complete Crafting Overhaul Remastered - Immersive Sounds Patch - French/ImmersiveSoundsCompendium_CCOR_Patch.esp.json',
    'data/user/database/french/Water for ENB [4K] - French/Water for ENB (Shades of Skyrim).esp.json',
    'data/user/database/french/Embers XD - French/Embers XD.esp.json',
    'data/user/database/french/Lux - Patch Hub - French/Lux - JK\'s Mistveil Keep patch.esp.json',
    'data/user/database/french/Lux - Patch Hub - French/Lux - JK\'s Temple of Dibella patch.esp.json',
    'data/user/database/french/Lux - Patch Hub - French/Lux - Distinct Interiors patch.esp.json',
    'data/user/database/french/Lux - Patch Hub - French/Lux - JK\'s College patch.esp.json',
    'data/user/database/french/Lux - Patch Hub - French/Lux - Anga\'s Mill COTN patch.esp.json',
    'data/user/database/french/Modpocalypse NPCs - Patch Collection - French/[xPatch] Modpocalypse NPCs (v3) SSE - AI Overhaul.esp.json',
    'data/user/database/french/DIbella\'s Blessing - RSV Exclusion Patches - French/DIbella\'s Blessing - RSV Exclusion Patch.esp.json',
    'data/user/database/french/Fanatical Enemies - Patches - French/fanatical enemies - modpocalypse patch.esp.json',
    'data/user/database/french/AI Overhaul - Nithi NPC Enhancements Patch Hub - French/NITHI NPCs - Whiterun - Complete - AI Overhaul.esp.json',
    'data/user/database/french/True Sons of Skyrim Refined - French/TSOS_AI_Overall_Patch.esp.json',
    'data/user/database/french/AttackoDaedra.esp - French/attackodaedra.esp.json',
    'data/user/database/french/YOT - Clockwork.esp - French/yot - clockwork.esp.json',

    # Scripts
    'scripts/run_phase0_global_scan.py',
    'scripts/apply_phase1_nolvus_fixes.py',
    'scripts/apply_subphase_2a_fixes.py',
    'scripts/apply_subphase_2b_fixes.py',
    'scripts/apply_subphase_2c_fixes.py',
    'scripts/apply_subphase_2d_fixes.py',
    'scripts/apply_subphase_2e_fixes.py',
    'scripts/restore_experience_integration.py',
    'scripts/fix_clothes_miraak.py',
    'scripts/generate_verified_audit_table.py',
    'scripts/generate_audit_impact_markdown.py',
    'scripts/verify_and_generate_recap_2d.py',
    'scripts/verify_and_generate_recap_2e.py'
]

missing = [f for f in files_to_stage if not os.path.exists(f)]
if missing:
    print(f"Missing files ({len(missing)}):", missing)
    sys.exit(1)

print(f"All {len(files_to_stage)} files exist. Staging with git add...")
for f in files_to_stage:
    cmd = ['git', 'add', '-f', f]
    subprocess.run(cmd, check=True)

print("Staged successfully!")
