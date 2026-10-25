import json
from pathlib import Path

db_dir = Path('data/user/database/french')

patch_realignments = {
    # UCLA - Zim's - WACCF Patch
    ("UCLA - Zim's - WACCF Patch.esp.json", "Increases Magic Resistance by <10>%.  Gives access to Benthic Scream."):
        "Augmente la résistance à la magie de <10> %. Donne accès au Cri benthique.",

    # LOTD - Creation Club Lord's Mail Patch
    ("DBM_CC_LordsMailPatchV2.esp.json", "Opponents in melee range have <5> points of health absorbed per second.  Increases Poison and Disease Resistance by <50>%.  Increases Magic Resistance by <15>%."):
        "Les adversaires au corps à corps subissent une absorption de santé de <5> points par seconde. Augmente la résistance au poison et aux maladies de <50> %. Augmente la résistance à la magie de <15> %.",

    # Nolvus Awakening Crafting Patch
    ("nolvus awakening crafting patch.esp.json", "There is a <25>% chance of creating a duplicate potion when using the alchemy skill."):
        "Vous avez <25> % de chances de créer une potion ou un poison supplémentaire lors de l'utilisation de l'alchimie.",

    # Nolvus Awakening Vokriinator Black Integration
    ("nolvus awakening vokriinator black integration.esp.json", "Power attacks with a war axe have a 25% chance to grant 15% extra attack damage for 30 seconds. This effect stacks."):
        "Les attaques puissantes à la hache de guerre ont 25 % de chances d'octroyer 15 % de dégâts d'attaque supplémentaires pendant 30 secondes. Cet effet est cumulable.",
    ("nolvus awakening vokriinator black integration.esp.json", "Power attacks with a war axe smash through a block, causing the target to drop their shield and take a critical strike that deals 3 times critical damage."):
        "Les attaques puissantes à la hache de guerre brisent la parade, forçant la cible à lâcher son bouclier et infligeant un coup critique à 3 fois les dégâts critiques.",
    ("nolvus awakening vokriinator black integration.esp.json", "One-handed power attacks have 25% chance to disarm targets, inflicting a critical strike for 2 times critical damage."):
        "Les attaques puissantes à une main ont 25 % de chances de désarmer la cible, infligeant un coup critique à 2 fois les dégâts critiques.",

    # Vokrii - Apply Spell Conditions Fix
    ("vokrii - apply spell conditions fix.esp.json", "Power attacks with a war axe smash through a shield, inflicting a critical strike for 5 times critical damage and forcing them to drop their shield."):
        "Les attaques puissantes à la hache de guerre brisent les boucliers, infligeant un coup critique à 5 fois les dégâts critiques et forçant la cible à lâcher son bouclier.",
    ("vokrii - apply spell conditions fix.esp.json", "Power attacks with a warhammer interrupt spellcasting, inflicting a critical strike for 3 times critical damage, silencing and immobilizing the target for 5 seconds."):
        "Les attaques puissantes au marteau de guerre interrompent les sorts, infligeant un coup critique à 3 fois les dégâts critiques, tout en réduisant la cible au silence et en l'immobilisant pendant 5 secondes.",
    ("vokrii - apply spell conditions fix.esp.json", "Ranged weapons knock targets down if they are sprinting, inflicting a critical strike for 2 times critical damage."):
        "Les armes à distance renversent les cibles qui sprintent, infligeant un coup critique à 2 fois les dégâts critiques.",
    ("vokrii - apply spell conditions fix.esp.json", "Ranged weapons interrupt power attacks, knocking the attacker back and inflicting a critical strike for 2 times critical damage."):
        "Les armes à distance interrompent les attaques puissantes, repoussant l'assaillant et infligeant un coup critique à 2 fois les dégâts critiques.",
    ("vokrii - apply spell conditions fix.esp.json", "Power attacks with a dagger bleed the living for 30 seconds, inflicting a critical strike for 3 times critical damage."):
        "Les attaques puissantes à la dague font saigner les vivants pendant 30 secondes, infligeant un coup critique à 3 fois les dégâts critiques.",

    # USSEP Vampire and Artifact Rebalances
    ("unofficial skyrim special edition patch.esp.json", "Your Vampiric blood gives you <40>% weakness to Fire."):
        "Votre sang vampirique vous octroie une vulnérabilité de <40> % au feu.",
    ("unofficial skyrim special edition patch.esp.json", "Your Vampiric blood gives you <30>% weakness to Fire."):
        "Votre sang vampirique vous octroie une vulnérabilité de <30> % au feu.",
    ("unofficial skyrim special edition patch.esp.json", "<20> points damage, increases to <50> points if powered with dreams collected from sleeping people."):
        "Inflige <20> points de dégâts, montant à <50> points en cas d'utilisation de rêves récoltés sur des dormeurs.",

    # Bloodskal Blade Enhancements
    ("Bloodskal Blade - Tweaks and Enhancements.esp.json", "Bloodskal Strike is currently on cooldown."):
        "La Frappe de Sangskaal est actuellement en cours de recharge.",
    ("Bloodskal Blade - Tweaks and Enhancements.esp.json", "Bloodskal Strike Cooldown"):
        "Temps de recharge de la Frappe de Sangskaal",
    ("Bloodskal Blade - Tweaks and Enhancements.esp.json", "BloodSkal Blade Control Spell"):
        "Sort de contrôle de la Lame des Sangskaals",

    # Angelic Standing Stones Patches (Stone Amulets)
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Apprentice Stone Amulet"): "Amulette de la pierre de l'Apprenti",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Atronach Stone Amulet"): "Amulette de la pierre de l'Atronach",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Lady Stone Amulet"): "Amulette de la pierre de la Dame",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Lord Stone Amulet"): "Amulette de la pierre du Seigneur",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Mage Stone Amulet"): "Amulette de la pierre du Mage",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Ritual Stone Amulet"): "Amulette de la pierre du Rituel",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Serpent Stone Amulet"): "Amulette de la pierre du Serpent",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Shadow Stone Amulet"): "Amulette de la pierre de l'Ombre",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Steed Stone Amulet"): "Amulette de la pierre du Destrier",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Thief Stone Amulet"): "Amulette de la pierre du Voleur",
    ("Angelic Standing Stones - Amulets Patch.esp.json", "Tower Stone Amulet"): "Amulette de la pierre de la Tour",
    
    # Quests Award Perk Points (QAPP Patches)
    ("qapp", "Quests Award Perk Points"): "Points d'atout en récompense de quête",
}

updated_strings = 0
updated_files = 0

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    file_name = p.name
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        file_modified = False
        for s in items:
            orig = (s.get('original') or '').strip()
            
            # Match specific file + original
            for (target_file, target_orig), new_trans in patch_realignments.items():
                match_file = (target_file == file_name) or (target_file in file_name.lower())
                if match_file and target_orig == orig:
                    if 'string' in s:
                        s['string'] = new_trans
                    if 'translation' in s:
                        s['translation'] = new_trans
                    s['status'] = 'TranslationComplete'
                    file_modified = True
                    updated_strings += 1
                    print(f"[{file_name}] {orig[:35]} -> {new_trans[:35]}")
                    
        if file_modified:
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            updated_files += 1
    except Exception:
        pass

print(f"\nSuccessfully applied patch realignments to {updated_strings} strings across {updated_files} files.")
