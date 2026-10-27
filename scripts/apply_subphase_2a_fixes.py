import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

recap_2a = []

def process_file_modifications(filepath, mod_dict):
    """
    mod_dict: {(form_id, rec_type): (target_string, fix_nature)}
    """
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return 0
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified_count = 0
    for item in data:
        key = (item.get('form_id'), item.get('type'))
        if key in mod_dict:
            target_string, fix_nature = mod_dict[key]
            orig = item.get('original')
            old_str = item.get('string')
            if old_str != target_string:
                item['string'] = target_string
                item['status'] = 'TranslationComplete'
                modified_count += 1
                recap_2a.append({
                    'file': os.path.basename(filepath),
                    'form_id': item.get('form_id'),
                    'type': item.get('type'),
                    'original': orig,
                    'before': old_str,
                    'after': target_string,
                    'nature': fix_nature
                })
    
    if modified_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {modified_count} records in {os.path.basename(filepath)}")
    return modified_count

# 1. Clothes Patch
cp_file = 'data/user/database/french/Nolvus Awakening Clothes Patch.esp - French/nolvus awakening clothes patch.esp.json'
cp_mods = {
    ('0303C0F1|Dragonborn.esm', 'ARMO FULL'): ('Masque de Miraak', "Restauration du nom d'objet (écrasé par la description de l'enchantement)"),
    ('0303C0F2|Dragonborn.esm', 'ARMO DESC'): ('Augmente la résistance à la magie de <10> %. Confère l\'accès au Cri benthique.', "Conservation de la variable <10> conforme à l'original"),
    ('000AE087|Skyrim.esm', 'WEAP DESC'): ('<5> points de dégâts supplémentaires aux Nordiques.', "Conservation de la variable <5> conforme à l'original"),
    ('0010EB65|Skyrim.esm', 'ARMO FULL'): ('Bouclier de Solitude', "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"),
    ('0010EB64|Skyrim.esm', 'ARMO FULL'): ('Bouclier de Solitude', "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"),
    ('0010EB63|Skyrim.esm', 'ARMO FULL'): ('Bouclier de Solitude', "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"),
    ('0009E023|Skyrim.esm', 'ARMO FULL'): ('Bouclier de Solitude', "Canon Bethesda : Bouclier de Solitude (au lieu de Rondache)"),
    ('00013989|Skyrim.esm', 'WEAP FULL'): ('Épée d\'acier', "Canon Bethesda : Épée d'acier (au lieu de en acier)"),
    ('000139B1|Skyrim.esm', 'WEAP FULL'): ('Épée d\'ébonite', "Canon Bethesda : Épée d'ébonite (au lieu de en ébonite)"),
    ('0007947A|Skyrim.esm', 'CELL FULL'): ('Logements de Jorrvaskr', "Canon Bethesda : Logements de Jorrvaskr"),
    ('000457F7|Skyrim.esm', 'NPC_ FULL'): ('Elfe noire', "Accord de genre : PNJ féminin"),
    ('0201684C|Dawnguard.esm', 'NPC_ FULL'): ('Capitaine', "Canon Bethesda : Capitaine (Passeur)")
}
process_file_modifications(cp_file, cp_mods)

# 2. Clothes Balance Patch
cbp_file = 'data/user/database/french/Nolvus Awakening Clothes Balance Patch - French/nolvus awakening clothes balance patch.esp.json'
cbp_mods = {
    ('0100A317|Apachii_DivineEleganceStore.esm', 'ARMO FULL'): ('Armure en cuir de loup de Robin (PNJ)', "Traduction française de l'anglais résiduel Apachii"),
    ('0100A315|Apachii_DivineEleganceStore.esm', 'ARMO FULL'): ('Gants de Robin (PNJ)', "Traduction française de l'anglais résiduel Apachii"),
    ('0100A311|Apachii_DivineEleganceStore.esm', 'ARMO FULL'): ('Armure de Freja (PNJ)', "Traduction française de l'anglais résiduel Apachii")
}
process_file_modifications(cbp_file, cbp_mods)

# 3. Gourmet Integration
gourmet_file = 'data/user/database/french/Nolvus Awakening Gourmet Integration - French/nolvus awakening gourmet integration.esp.json'
gourmet_mods = {
    ('000D882D|Skyrim.esm', 'CONT FULL'): ('Coffre de receleur de la Guilde des voleurs', "Canon Bethesda : Traduction de Thieves Guild Fence Chest"),
    ('000D882E|Skyrim.esm', 'CONT FULL'): ('Coffre de receleur de la Guilde des voleurs', "Canon Bethesda : Traduction de Thieves Guild Fence Chest")
}
process_file_modifications(gourmet_file, gourmet_mods)

# 4. Seasonal Plant Mashup
plants_file = 'data/user/database/french/Nolvus Awakening Seasonal Plant Mashup - French/Nolvus Awakening Seasonal Plant Mashup.esp.json'
plants_mods = {
    ('000BB949|Skyrim.esm', 'TREE FULL'): ('Raisin jazbay', "Canon Bethesda : Traduction de Jazbay"),
    ('03010466|HearthFires.esm', 'TREE FULL'): ('Raisin jazbay', "Canon Bethesda : Traduction de Jazbay"),
    ('09000844|Nolvus Awakening Seasonal Plant Mashup.esp', 'TREE FULL'): ('Raisin jazbay', "Canon Bethesda : Traduction de Jazbay"),
    ('030110C8|HearthFires.esm', 'TREE FULL'): ('Racine de Nirn', "Canon Bethesda : Traduction de Nirnroot"),
    ('030110BE|HearthFires.esm', 'TREE FULL'): ('Mora tapinella', "Canon Bethesda : Traduction de Mora Tapinella")
}
process_file_modifications(plants_file, plants_mods)

# 5. AI Patch
ai_file = 'data/user/database/french/Nolvus Awakening AI Patch - French/Nolvus Awakening AI Patch.esp.json'
ai_mods = {
    ('00013B76|Skyrim.esm', 'NPC_ SHRT'): ('Léontius', "Accentuation officielle Skyrim"),
    ('00013B76|Skyrim.esm', 'NPC_ FULL'): ('Léontius Salvius', "Accentuation officielle Skyrim"),
    ('00065657|Skyrim.esm', 'NPC_ SHRT'): ('Érik', "Accentuation officielle Skyrim"),
    ('00013818|Skyrim.esm', 'CELL FULL'): ('Forteresse Froidepierre', "Canon Bethesda : Forteresse Froidepierre (Jarl's Longhouse Winterhold)"),
    ('0001365F|Skyrim.esm', 'NPC_ FULL'): ('Dravynea la Tisseuse de pierre', "Canon Bethesda : Suppression tirets superflus"),
    ('0001365F|Skyrim.esm', 'NPC_ SHRT'): ('Dravynea', "Canon Dunmer : Dravynea sans accent"),
    ('00013380|Skyrim.esm', 'NPC_ FULL'): ('Vekel l\'homme', "Typographie française : Vekel l'homme"),
    ('0001C196|Skyrim.esm', 'NPC_ FULL'): ('Brelyna Maryon', "Canon Dunmer : Brelyna sans accent"),
    ('0001C196|Skyrim.esm', 'NPC_ SHRT'): ('Brelyna', "Canon Dunmer : Brelyna sans accent"),
    ('0001413D|Skyrim.esm', 'NPC_ FULL'): ('Ravam Verethi', "Canon Dunmer : Ravam Verethi"),
    ('0001366B|Skyrim.esm', 'NPC_ FULL'): ('Sondas Drenim', "Canon Dunmer : Sondas Drenim"),
    ('0001413A|Skyrim.esm', 'NPC_ FULL'): ('Revyn Sadri', "Canon Dunmer : Revyn Sadri"),
    ('0001413A|Skyrim.esm', 'NPC_ SHRT'): ('Revyn', "Canon Dunmer : Revyn"),
    ('00014123|Skyrim.esm', 'NPC_ FULL'): ('Niranye', "Canon Altmer : Niranye sans tréma")
}
process_file_modifications(ai_file, ai_mods)

# 6. Combat Scaling Overhaul - Consistency Patch
cso_cons_file = 'data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - consistency patch.esp.json'
cso_cons_mods = {
    ('000BFB55|Skyrim.esm', 'NPC_ FULL'): ('Gardienne Carcette', "Canon Bethesda : Gardienne Carcette (Keeper Carcette)"),
    ('00023AB2|Skyrim.esm', 'NPC_ FULL'): ('Poney Exmoor', "Restauration race de monture : Poney Exmoor"),
    ('00068D5B|Skyrim.esm', 'NPC_ FULL'): ('Poney Exmoor', "Restauration race de monture : Poney Exmoor"),
    ('00068D07|Skyrim.esm', 'NPC_ FULL'): ('Poney fell noir', "Restauration race de monture : Poney fell noir"),
    ('00068CFA|Skyrim.esm', 'NPC_ FULL'): ('Poney fell noir', "Restauration race de monture : Poney fell noir"),
    ('00068D6E|Skyrim.esm', 'NPC_ FULL'): ('Cheval palomino', "Restauration race de monture : Cheval palomino"),
    ('00068D04|Skyrim.esm', 'NPC_ FULL'): ('Cheval palomino', "Restauration race de monture : Cheval palomino"),
    ('00068D6B|Skyrim.esm', 'NPC_ FULL'): ('Cheval gitan', "Restauration race de monture : Cheval gitan"),
    ('00068D02|Skyrim.esm', 'NPC_ FULL'): ('Cheval gitan', "Restauration race de monture : Cheval gitan"),
    ('00068D6D|Skyrim.esm', 'NPC_ FULL'): ('Poney fell gris', "Restauration race de monture : Poney fell gris"),
    ('00068D03|Skyrim.esm', 'NPC_ FULL'): ('Poney fell gris', "Restauration race de monture : Poney fell gris"),
    ('0001C196|Skyrim.esm', 'NPC_ FULL'): ('Brelyna Maryon', "Canon Dunmer : Brelyna sans accent"),
    ('0001C196|Skyrim.esm', 'NPC_ SHRT'): ('Brelyna', "Canon Dunmer : Brelyna sans accent"),
    ('040179C7|Dragonborn.esm', 'NPC_ FULL'): ('Ralis Sedarys', "Canon Dunmer : Ralis Sedarys sans accent")
}
process_file_modifications(cso_cons_file, cso_cons_mods)

# 7. Combat Scaling Overhaul - Enemy Level Mult & Enemy Level
cso_mult_file = 'data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - enemy level mult.esp.json'
cso_mult_mods = {
    ('000BFB55|Skyrim.esm', 'NPC_ FULL'): ('Gardienne Carcette', "Canon Bethesda : Gardienne Carcette"),
    ('0001365F|Skyrim.esm', 'NPC_ FULL'): ('Dravynea la Tisseuse de pierre', "Canon Bethesda : Dravynea"),
    ('00013B76|Skyrim.esm', 'NPC_ FULL'): ('Léontius Salvius', "Accentuation officielle Skyrim"),
    ('00013B76|Skyrim.esm', 'NPC_ SHRT'): ('Léontius', "Accentuation officielle Skyrim"),
    ('0002C925|Skyrim.esm', 'NPC_ FULL'): ('Sévério Pélagia', "Accentuation officielle Skyrim"),
    ('00016FF8|Skyrim.esm', 'NPC_ FULL'): ('Valkynaz drémora', "Canon Bethesda : Valkynaz drémora"),
    ('0007E87D|Skyrim.esm', 'NPC_ FULL'): ('Monarque de feu', "Canon Bethesda : Monarque de feu (Flame Thrall)"),
    ('0001C196|Skyrim.esm', 'NPC_ FULL'): ('Brelyna Maryon', "Canon Dunmer : Brelyna Maryon"),
    ('0001C196|Skyrim.esm', 'NPC_ SHRT'): ('Brelyna', "Canon Dunmer : Brelyna"),
    ('040179C7|Dragonborn.esm', 'NPC_ FULL'): ('Ralis Sedarys', "Canon Dunmer : Ralis Sedarys"),
    ('0401777C|Dragonborn.esm', 'NPC_ FULL'): ('Varona Nelas', "Canon Dunmer : Varona Nelas"),
    ('00014123|Skyrim.esm', 'NPC_ FULL'): ('Niranye', "Canon Altmer : Niranye"),
    ('0001413D|Skyrim.esm', 'NPC_ FULL'): ('Ravam Verethi', "Canon Dunmer : Ravam Verethi"),
    ('0001413A|Skyrim.esm', 'NPC_ FULL'): ('Revyn Sadri', "Canon Dunmer : Revyn Sadri"),
    ('0001413A|Skyrim.esm', 'NPC_ SHRT'): ('Revyn', "Canon Dunmer : Revyn")
}
process_file_modifications(cso_mult_file, cso_mult_mods)

cso_lvl_file = 'data/user/database/french/Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French/nolvus awakening combat scaling overhaul - enemy level.esp.json'
cso_lvl_mods = {
    ('000BFB55|Skyrim.esm', 'NPC_ FULL'): ('Gardienne Carcette', "Canon Bethesda : Gardienne Carcette"),
    ('00016FF8|Skyrim.esm', 'NPC_ FULL'): ('Valkynaz drémora', "Canon Bethesda : Valkynaz drémora"),
    ('0402C406|Dragonborn.esm', 'NPC_ FULL'): ('Garde Rédoran', "Canon Bethesda : Garde Rédoran"),
    ('0003BCC7|Skyrim.esm', 'NPC_ FULL'): ('Messager sombrage', "Canon Bethesda : Messager sombrage"),
    ('0001C196|Skyrim.esm', 'NPC_ FULL'): ('Brelyna Maryon', "Canon Dunmer : Brelyna Maryon"),
    ('0001C196|Skyrim.esm', 'NPC_ SHRT'): ('Brelyna', "Canon Dunmer : Brelyna"),
    ('040179C7|Dragonborn.esm', 'NPC_ FULL'): ('Ralis Sedarys', "Canon Dunmer : Ralis Sedarys"),
    ('00014123|Skyrim.esm', 'NPC_ FULL'): ('Niranye', "Canon Altmer : Niranye")
}
process_file_modifications(cso_lvl_file, cso_lvl_mods)

print(f"\nApplied total of {len(recap_2a)} precise corrections across Sub-phase 2A.")
with open('recap_phase2a_diffs.json', 'w', encoding='utf-8') as f:
    json.dump(recap_2a, f, ensure_ascii=False, indent=2)
