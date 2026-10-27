import json
import re
from pathlib import Path

db = Path("data/user/database/french")

def fix_json_file(file_path: Path, fixes_dict: dict, label: str):
    """
    fixes_dict is a mapping of form_id (or form_id|type) -> new_translation_string
    or callable(item) -> new_string
    """
    if not file_path.is_file():
        print(f"File not found: {file_path}")
        return 0
        
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    items = data if isinstance(data, list) else data.get("strings", [])
    count = 0
    
    for item in items:
        fid = item.get("form_id")
        orig = item.get("original")
        current_trans = item.get("string") or item.get("translation")
        rec_type = item.get("type", "")
        
        # Check by composite key or form_id
        key1 = f"{fid}|{rec_type}"
        key2 = fid
        
        new_val = None
        if key1 in fixes_dict:
            new_val = fixes_dict[key1]
        elif key2 in fixes_dict:
            new_val = fixes_dict[key2]
            
        if callable(new_val):
            new_val = new_val(item)
            
        if new_val is not None and new_val != current_trans:
            item["string"] = new_val
            item["status"] = "TranslationComplete"
            count += 1
            
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"[{label}] Updated {count} entries in {file_path.name}")
    return count

def main():
    total_updated = 0
    
    # -------------------------------------------------------------
    # 1. Nolvus Awakening Armors Balance Patch
    # -------------------------------------------------------------
    p_armors_bal = db / "Nolvus Awakening Armors Balance Patch.esp - French" / "nolvus awakening armors balance patch.esp.json"
    armors_fixes = {
        # Black Mage Armor corrupt tags
        "870008BF|Black Mage Armor SE.esp": "Réduit de 15 % le coût des sorts de destruction et de guérison et augmente de 100 % la régénération de magie.",
        "870008C9|Black Mage Armor SE.esp": "Réduit de 15 % le coût des sorts de destruction et de guérison et augmente de 100 % la régénération de magie.",
        "870008C1|Black Mage Armor SE.esp": "Réduit de 15 % le coût des sorts de destruction et de guérison et augmente de 100 % la régénération de magie.",
        "870008C7|Black Mage Armor SE.esp": "Réduit de 15 % le coût des sorts de destruction et de guérison et augmente de 100 % la régénération de magie.",
        "870008CB|Black Mage Armor SE.esp": "Réduit de 15 % le coût des sorts de destruction et de guérison et augmente de 100 % la régénération de magie.",
        
        # Soul Hunter Armor corrupt tags
        "6B000861|Soul Hunter Armor.esp": "Tous les sorts coûtent 25 % de moins et la magie se régénère 250 % plus vite. La réserve de magie augmente de 85 points.",
        
        # Drifter Armor brackets
        "2B00081B|DrifterArmorAndOutfitByXtudo.esp": "Gantelets métalliques de vagabond du pugiliste",
        "2B00081E|DrifterArmorAndOutfitByXtudo.esp": "Gantelets métalliques légers de vagabond du pugiliste",
        "2B000805|DrifterArmorAndOutfitByXtudo.esp": "Gantelets d'acier de vagabond du pugiliste",
        "4000080F|DrifterArmorAndOutfitByXtudo.esp": "Gantelets d'acier légers de vagabond du pugiliste",
        
        # Legendary Alpha Shields distinctions
        "7100082F|Legendary Alpha Shields.esp": "Bouclier d'acier ouvragé II",
        "71000831|Legendary Alpha Shields.esp": "Bouclier d'acier ouvragé II A",
        "71000833|Legendary Alpha Shields.esp": "Bouclier d'acier ouvragé II B",
        "71000835|Legendary Alpha Shields.esp": "Bouclier d'acier ouvragé II C",
        "71000837|Legendary Alpha Shields.esp": "Bouclier d'acier ouvragé II D",
        "71000839|Legendary Alpha Shields.esp": "Bouclier d'acier ouvragé II E",
        "71000823|Legendary Alpha Shields.esp": "Bouclier celtique II",
        
        # Hermit Hoods
        "5800087E|Hermit Armor.esp": "Capuchon d'ermite noir 1",
        "58000880|Hermit Armor.esp": "Capuchon d'ermite noir 2",
        "580008ED|Hermit Armor.esp": "Capuchon d'ermite noir 3",
        "580008EF|Hermit Armor.esp": "Capuchon d'ermite noir 4",
        "5800087D|Hermit Armor.esp": "Capuchon d'ermite blanc 1",
        "5800087F|Hermit Armor.esp": "Capuchon d'ermite blanc 2",
        "58000881|Hermit Armor.esp": "Capuchon d'ermite blanc 3",
        "580008EE|Hermit Armor.esp": "Capuchon d'ermite blanc 4",
    }
    total_updated += fix_json_file(p_armors_bal, armors_fixes, "Armors Balance")

    # -------------------------------------------------------------
    # 2. Nolvus Awakening Weapons Balance Patch
    # -------------------------------------------------------------
    p_weap_bal = db / "Nolvus Awakening Weapons Balance Patch.esp - French" / "nolvus awakening weapons balance patch.esp.json"
    weap_fixes = {
        "28000800|[TDarce] Black Silence Durandal.esp": "Inflige 10 points de dégâts de saignement pendant 5 secondes.",
        "38000D69|Swords 2-5.esp": "Traqueur",
        "38000D66|Swords 2-5.esp": "Justice",
        "38000D68|Swords 2-5.esp": "Traître",
        "17000D64|FGCAegeanSentinelHalberd.esp": "Hallebarde de sentinelle égéenne +1",
        "17000D65|FGCAegeanSentinelHalberd.esp": "Hallebarde de sentinelle égéenne +2",
        "17000D66|FGCAegeanSentinelHalberd.esp": "Hallebarde de sentinelle égéenne +3",
        "17000D67|FGCAegeanSentinelHalberd.esp": "Hallebarde de sentinelle égéenne +4",
        "17000D68|FGCAegeanSentinelHalberd.esp": "Hallebarde de sentinelle égéenne +5",
        "24000D67|Elexorien.esp": "Elexorien (deux mains)",
        "2C000805|Luciendar.esp": "Luciendar (Espadon)",
    }
    total_updated += fix_json_file(p_weap_bal, weap_fixes, "Weapons Balance")

    # -------------------------------------------------------------
    # 3. Nolvus Awakening Weapons Patch (Dragonbane clean strings)
    # -------------------------------------------------------------
    p_weap_patch = db / "Nolvus Awakening Weapons Patch - French" / "nolvus awakening weapons patch.esp.json"
    weap_patch_fixes = {
        "000F1AC1|Skyrim.esm": "Inflige 20 points de dégâts supplémentaires aux dragons et 10 points de dégâts de foudre aux autres ennemis.",
        "000F71CD|Skyrim.esm": "Inflige 25 points de dégâts supplémentaires aux dragons et 10 points de dégâts de foudre aux autres ennemis.",
        "000F71CE|Skyrim.esm": "Inflige 30 points de dégâts supplémentaires aux dragons et 10 points de dégâts de foudre aux autres ennemis.",
        "000F71CF|Skyrim.esm": "Inflige 35 points de dégâts supplémentaires aux dragons et 10 points de dégâts de foudre aux autres ennemis.",
        "000F71D0|Skyrim.esm": "Inflige 40 points de dégâts supplémentaires aux dragons et 10 points de dégâts de foudre aux autres ennemis.",
    }
    total_updated += fix_json_file(p_weap_patch, weap_patch_fixes, "Weapons Patch")

    # -------------------------------------------------------------
    # 4. Nolvus Awakening Clothes Balance Patch
    # -------------------------------------------------------------
    p_clothes_bal = db / "Nolvus Awakening Clothes Balance Patch - French" / "nolvus awakening clothes balance patch.esp.json"
    clothes_fixes = {
        "0102D990|Apachii_DivineEleganceStore.esm": "Immunité contre les maladies et les poisons.",
        "0102D989|Apachii_DivineEleganceStore.esm": "Le crochetage, l'archerie et l'alchimie sont 20 % plus efficaces.",
        "0102D98B|Apachii_DivineEleganceStore.esm": "Augmente la magie de 50 points. Les sorts de destruction et de guérison coûtent 20 % de moins.",
        "0102D98E|Apachii_DivineEleganceStore.esm": "Les prix sont 20 % plus avantageux, la capacité d'emport augmente de 20 points et vous pouvez respirer sous l'eau.",
    }
    total_updated += fix_json_file(p_clothes_bal, clothes_fixes, "Clothes Balance")

    # -------------------------------------------------------------
    # 5. Nolvus Awakening Clothes Patch
    # -------------------------------------------------------------
    p_clothes_patch = db / "Nolvus Awakening Clothes Patch.esp - French" / "nolvus awakening clothes patch.esp.json"
    clothes_patch_fixes = {
        "000AE087|Skyrim.esm": "5 points de dégâts supplémentaires aux Nordiques.",
        "0303C0F1|Dragonborn.esm": "Augmente la résistance à la magie de 10 %. Confère l'accès au Cri benthique.",
        "0303C0F2|Dragonborn.esm": "Augmente la résistance à la magie de 10 %. Confère l'accès au Cri benthique.",
    }
    total_updated += fix_json_file(p_clothes_patch, clothes_patch_fixes, "Clothes Patch")

    # -------------------------------------------------------------
    # 6. Nolvus Awakening DLC Patch
    # -------------------------------------------------------------
    p_dlc_patch = db / "Nolvus Awakening DLC Patch - French" / "nolvus awakening dlc patch.esp.json"
    dlc_fixes = {
        "07125B04|LegacyoftheDragonborn.esm": "La résistance à la magie, à la foudre et au poison est augmentée de 20 %.",
        "000AE087|Skyrim.esm": "5 points de dégâts supplémentaires aux Nordiques.",
        "071253C0|LegacyoftheDragonborn.esm": "Inflige 30 points de dégâts de foudre. Ces dégâts ne peuvent pas être évités.",
    }
    total_updated += fix_json_file(p_dlc_patch, dlc_fixes, "DLC Patch")

    # -------------------------------------------------------------
    # 7. Nolvus Awakening Crafting Patch
    # -------------------------------------------------------------
    p_craft_patch = db / "Nolvus Awakening Crafting Patch - French" / "nolvus awakening crafting patch.esp.json"
    craft_fixes = {
        "0010BF09|Skyrim.esm": "50 % de chances de produire une potion ou un poison supplémentaire avec la même quantité d’ingrédients.",
    }
    total_updated += fix_json_file(p_craft_patch, craft_fixes, "Crafting Patch")

    # -------------------------------------------------------------
    # 8. Nolvus Awakening Creatures Patch
    # -------------------------------------------------------------
    p_creat_patch = db / "Nolvus Awakening Creatures Patch - French" / "Nolvus Awakening Creatures Patch.esp.json"
    creat_fixes = {
        "11000837|mihailgrummite.esp": "Invoque un grummite maniaque briseur des marais pendant <dur> secondes.",
    }
    total_updated += fix_json_file(p_creat_patch, creat_fixes, "Creatures Patch")

    # -------------------------------------------------------------
    # 9. Nolvus Awakening Experience Integration (Untranslated Quest)
    # -------------------------------------------------------------
    p_exp_patch = db / "Nolvus Awakening Experience Integration - French" / "Nolvus Awakening Experience Integration.esp.json"
    p_exp_patch2 = db / "Nolvus Awakening Experience Integration.esp - French" / "nolvus awakening experience integration.esp.json"
    exp_fixes = {
        "1D000F18|ccbgssse013-dawnfang.esl": "Après avoir suivi l'apparition, je me suis retrouvé dans un caveau abandonné. Une épée mystérieuse flotte, suspendue dans un champ magique au cœur de la salle. À en juger par l'état des lieux, personne n'y a pénétré depuis une éternité. Si je m'avance, je trouverai peut-être des réponses et un moyen de libérer l'épée.",
    }
    total_updated += fix_json_file(p_exp_patch, exp_fixes, "Experience Integration 1")
    total_updated += fix_json_file(p_exp_patch2, exp_fixes, "Experience Integration 2")

    # -------------------------------------------------------------
    # 10. Nolvus Awakening Combat Scaling Overhaul - Enemy Level (English NPC)
    # -------------------------------------------------------------
    p_combat_enemy = db / "Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French" / "nolvus awakening combat scaling overhaul - enemy level.esp.json"
    p_combat_enemy_mult = db / "Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French" / "nolvus awakening combat scaling overhaul - enemy level mult.esp.json"
    cso_fixes = {
        "D5AEA346|The Restless Dead.esp": "Romanov le garde royal",
    }
    total_updated += fix_json_file(p_combat_enemy, cso_fixes, "CSO Enemy Level")
    total_updated += fix_json_file(p_combat_enemy_mult, cso_fixes, "CSO Enemy Level Mult")

    # -------------------------------------------------------------
    # 11. Nolvus Awakening Vokriinator Black Integration
    # Align all 41 perks rebalanced by Nolvus with literary and Lore-accurate French
    # -------------------------------------------------------------
    p_vok_nolvus = db / "Nolvus Awakening Vokriinator Black Integration.esp - French" / "nolvus awakening vokriinator black integration.esp.json"
    vok_fixes = {
        # SPERG war axes
        "0103A15B|SPERG-SSE.esp": "Les attaques à la hache de guerre infligent 25 % de dégâts critiques supplémentaires. Les attaques avec toutes les armes ont 5 % de chances en plus de porter un coup critique. Incompatible avec Brise-os ou Fine lame.",
        # SPERG critical damage 1H
        "01027727|SPERG-SSE.esp": "Les dégâts critiques augmentent de 10 % lorsque vous maniez une ou plusieurs armes à une main.",
        # Ordinator sword bleed
        "04002E07|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à l'épée font saigner la cible pendant 10 secondes. Lorsque sa santé passe sous les 25 %, vos attaques contre elle deviennent des frappes critiques infligeant 25 % de dégâts critiques supplémentaires.",
        # Ordinator warhammers armor reduction 60
        "04003911|Ordinator - Perks of Skyrim.esp": "Les attaques au marteau de guerre réduisent la valeur d'armure des ennemis protégés de 60 points pendant 10 secondes.",
        # Disciplined Fighter 1H
        "0003AF81|Skyrim.esm": "Les dégâts des attaques puissantes augmentent de 0,05 % par point de vigueur (requiert Combattant discipliné).",
        # Greatsword destabilize 15%
        "04003E7B|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à l'espadon déstabilisent la cible, augmentant les dégâts de vos attaques ordinaires contre elle de 15 % pendant 4 secondes.",
        # Battleaxe sweep 20%
        "040043F3|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à la hache d'armes fauchent toutes les cibles devant vous, infligeant 20 % de dégâts supplémentaires pour chaque ennemi situé à moins de 2,5 mètres.",
        # Dual wielding damage 20%
        "00106257|Skyrim.esm": "Les attaques avec deux armes infligent 20 % de dégâts supplémentaires.",
        # Two-handed power attack per stamina
        "00052D52|Skyrim.esm": "Les dégâts des attaques puissantes avec les armes à deux mains augmentent de 0,05 % par point de vigueur.",
        # Dual wielding damage 10%
        "00106256|Skyrim.esm": "Les attaques avec deux armes infligent 10 % de dégâts supplémentaires.",
        # War axe block break 50%
        "0400497F|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à la hache de guerre brisent la parade en forçant la cible à lâcher son bouclier, lui assénant une frappe critique qui inflige 50 % de dégâts critiques supplémentaires.",
        # Empty hand 30% less attack damage taken
        "04000D63|Ordinator - Combat Styles.esp": "Vous subissez 30 % de dégâts en moins lors d'une attaque puissante si vous maniez une arme à une main et avez l'autre main vide.",
        # Mace smite 20% / 45%
        "04003E74|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à la masse délivrent une frappe critique qui inflige 20 % de dégâts critiques supplémentaires (45 % contre les morts-vivants). Ne peut frapper une même cible par Châtiment qu'une fois toutes les 30 secondes.",
        # Greatsword destabilize 25% for 4s
        "04003E7C|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à l'espadon déstabilisent la cible, augmentant les dégâts de vos attaques ordinaires contre elle de 25 % pendant 4 secondes.",
        # Warhammer armor reduction 30
        "0400390F|Ordinator - Perks of Skyrim.esp": "Les attaques au marteau de guerre réduisent la valeur d'armure des ennemis protégés de 30 points pendant 10 secondes.",
        # Mace stagger 10%, ignore 15% armor
        "0103A15C|SPERG-SSE.esp": "Les attaques à la masse ont 10 % de chances de déstabiliser la cible. Les attaques avec toutes les armes ignorent 15 % de l'armure. Incompatible avec Fendre et tailler.",
        # Empty hand 15% less damage taken
        "04000D62|Ordinator - Combat Styles.esp": "Vous subissez 15 % de dégâts en moins lors d'une attaque puissante si vous maniez une arme à une main et avez l'autre main vide.",
        # Warhammer daze 30%, ignore 25% armor
        "0103A161|SPERG-SSE.esp": "Les attaques puissantes au marteau de guerre ont 30 % de chances d'étourdir la cible. Les attaques avec toutes les armes ignorent 25 % de l'armure. Incompatible avec Démembrement.",
        # Dagger paralyze 15% for 3s, 50% crit
        "040B0D40|Ordinator - Perks of Skyrim.esp": "Toucher une cible avec une attaque puissante à la dague a 15 % de chances de la paralyser pendant 3 secondes. Vos attaques contre la cible paralysée sont des frappes critiques infligeant 50 % de dégâts critiques supplémentaires.",
        # Battleaxe 25% crit, 10% chance
        "0103A160|SPERG-SSE.esp": "Les attaques à la hache d'armes infligent 25 % de dégâts critiques supplémentaires. Les attaques puissantes avec toutes les armes ont 10 % de chances en plus de porter un coup critique. Incompatible avec Brise-crâne.",
        # Warhammer armor reduction 40
        "04003910|Ordinator - Perks of Skyrim.esp": "Les attaques au marteau de guerre réduisent la valeur d'armure des ennemis protégés de 40 points pendant 10 secondes.",
        # Winding up attack critical strike
        "04103870|Ordinator - Perks of Skyrim.esp": "Lorsque vous maniez une arme à une main avec l'autre main libre, frapper l'adversaire pendant qu'il arme son attaque ou bande son arc délivre une frappe critique.",
        # Dagger power attack 25% distracting wounds
        "040B0D3F|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à la dague ont 25 % de chances d'infliger des blessures distrayantes, drainant 75 points de magie et de vigueur et interrompant leur régénération pendant 5 secondes.",
        # Mace armor reduction 20 points for 5s
        "07003380|Ordinator - Perks of Skyrim.esp": "Les attaques à la masse réduisent la valeur d'armure des ennemis protégés de 20 points pendant 5 secondes.",
        # Mace armor reduction 30 points for 5s
        "07003381|Ordinator - Perks of Skyrim.esp": "Les attaques à la masse réduisent la valeur d'armure des ennemis protégés de 30 points pendant 5 secondes.",
        # Mace armor reduction 50 points for 5s
        "07003382|Ordinator - Perks of Skyrim.esp": "Les attaques à la masse réduisent la valeur d'armure des ennemis protégés de 50 points pendant 5 secondes.",
        # Greatsword reduce attack damage 10%
        "07003909|Ordinator - Perks of Skyrim.esp": "Les attaques à l'espadon réduisent les dégâts d'attaque de la cible de 10 % pendant 3 secondes.",
        # Greatsword reduce attack damage 15%
        "0700390A|Ordinator - Perks of Skyrim.esp": "Les attaques à l'espadon réduisent les dégâts d'attaque de la cible de 15 % pendant 3 secondes.",
        # Greatsword reduce attack damage 20%
        "0700390B|Ordinator - Perks of Skyrim.esp": "Les attaques à l'espadon réduisent les dégâts d'attaque de la cible de 20 % pendant 3 secondes.",
        # Mace smite 40% / 55%
        "07003E75|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à la masse délivrent une frappe critique qui inflige 40 % de dégâts critiques supplémentaires (55 % contre les morts-vivants). Ne peut frapper une même cible par Châtiment qu'une fois toutes les 30 secondes.",
        # Warhammer 15% chance, 75% crit damage
        "07003E7F|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes au marteau de guerre ont 15 % de chances d'infliger une frappe critique. Tous les coups critiques au marteau de guerre infligent 75 % de dégâts critiques supplémentaires.",
        # Warhammer 25% chance, 75% crit damage
        "07003E80|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes au marteau de guerre ont 25 % de chances d'infliger une frappe critique. Tous les coups critiques au marteau de guerre infligent 75 % de dégâts critiques supplémentaires.",
        # Greatsword bash follow up 50%
        "07003E89|Ordinator - Perks of Skyrim.esp": "Donner un coup d'espadon pour interrompre une attaque avant qu'elle ne touche vous permet d'enchaîner avec une attaque puissante dans les 2 secondes pour porter une frappe critique infligeant 50 % de dégâts critiques supplémentaires et désarmer la cible.",
        # Mace stamina depletion 0.05% per point
        "0700440A|Ordinator - Perks of Skyrim.esp": "Les attaques puissantes à la masse ont 10 % de chances d'épuiser toute votre vigueur à l'impact, infligeant 0,05 % de dégâts supplémentaires par point de vigueur consommé et portant une frappe critique.",
        # Dual wield frenzy 30% damage, 50% crit damage for 4s
        "07004EEF|Ordinator - Perks of Skyrim.esp": "Lorsque vous combattez avec deux armes, vous entrez dans une frénésie meurtrière toutes les 20 à 40 secondes. Pendant 4 secondes, vos attaques puissantes avec deux armes infligent 30 % de dégâts et 50 % de dégâts critiques supplémentaires.",
        # One-handed 20%
        "0700B149|Ordinator - Perks of Skyrim.esp": "Les armes à une main infligent 20 % de dégâts supplémentaires.",
        # One-handed 40%, 0.5% per level
        "0700B14A|Ordinator - Perks of Skyrim.esp": "Les armes à une main infligent 40 % de dégâts supplémentaires, et les coups critiques portés avec elles infligent 0,5 % de dégâts critiques supplémentaires par niveau d'Arme à une main.",
        # Two-handed 20%
        "0700B14B|Ordinator - Perks of Skyrim.esp": "Les armes à deux mains infligent 20 % de dégâts supplémentaires.",
        # Two-handed 40%, 0.5% per level
        "0700B14C|Ordinator - Perks of Skyrim.esp": "Les armes à deux mains infligent 40 % de dégâts supplémentaires, et les coups critiques portés avec elles infligent 0,5 % de dégâts critiques supplémentaires par niveau d'Arme à deux mains.",
        # Vokrii two-handed 40% damage
        "06000B93|Vokrii - Minimalistic Perks of Skyrim.esp": "Les attaques puissantes à deux mains ont 25 % de chances de paralyser la cible, portant une frappe critique qui inflige 40 % de dégâts supplémentaires.",
        # Vokrii one-handed 40% damage
        "06000BA0|Vokrii - Minimalistic Perks of Skyrim.esp": "Les attaques puissantes à une main ont 25 % de chances de renverser la cible, portant une frappe critique qui inflige 40 % de dégâts supplémentaires.",
        # Run speed
        "08000819|Ordinator - Combat Styles.esp": "Augmente la vitesse de course de 10 %.",
    }
    total_updated += fix_json_file(p_vok_nolvus, vok_fixes, "Vokriinator Black Nolvus Integration")

    print(f"\n==========================================")
    print(f"PHASE 1 COMPLETE: Successfully updated {total_updated} entries across Nolvus patches!")

if __name__ == "__main__":
    main()
