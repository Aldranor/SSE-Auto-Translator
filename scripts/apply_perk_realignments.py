import json
from pathlib import Path

db_dir = Path('data/user/database/french')

exact_realignments = {
    # Vokriinator Black
    ("0C000850|Vokriinator Black.esp", "Detection spells reveal targets from much farther away."): 
        "Les sorts de détection révèlent les cibles de beaucoup plus loin.",
    ("0C000834|Vokriinator Black.esp", "Elemental enchantments on armor are 30% more effective if you have an elemental spell of the same type equipped."):
        "Les enchantements élémentaux sur les armures sont 30 % plus efficaces si un sort élémental du même type est équipé.",
        
    # Artéfacts de Zim
    ("04000D6C|ZIA_Complete Pack.esp", "Sneak attacks are <50>% stronger."):
        "Les attaques furtives sont 50 % plus puissantes.",
    ("040460EB|ZIA_Complete Pack.esp", "Target takes <mag> points of shock damage, and half as much Magicka damage. Disintegrates elves with low health."):
        "La cible subit <mag> points de dégâts de foudre, et la moitié de ce montant en dégâts de magie. Désintègre les Elfes dont la santé est faible.",

    # Adamant
    ("02008E1A|Adamant.esp", "Protection spells like Oakflesh and Fire Shell affect nearby allies when dual cast."):
        "Les sorts de protection comme Corps de chêne et Carapace de feu affectent les alliés proches lors d'un double lancer.",
    ("0202517F|Adamant.esp", "Bashing also deals damage to Magicka and Stamina."):
        "Les frappes infligent également des dégâts de magie et de vigueur.",
    ("0208A4FB|Adamant.esp", "Your armor weighs nothing and doesn't slow you down when wearing three pieces of heavy armor."):
        "Votre armure ne pèse rien et ne vous ralentit pas lorsque vous portez trois pièces d'armure lourde.",
    ("0201A83E|Adamant.esp", "Shock spells have a chance to overload targets who fall below half Health."):
        "Les sorts de foudre ont une chance de surcharger les cibles dont la santé tombe sous les 50 %.",
    ("02080302|Adamant.esp", "block + sprint = shield charge"):
        "Sprinter tout en parant au bouclier exécute une charge au bouclier.",

    # La Voie du Sorcier (Path of Sorcery)
    ("00058F81|Skyrim.esm", "Elemental enchantments on armor and clothing are 30% more effective if you have an elemental spell of the same type equipped."):
        "Les enchantements élémentaux sur les armures et vêtements sont 30 % plus efficaces si un sort élémental du même type est équipé.",
    ("0A000BB1|PathOfSorcery.esp", "When at full health, healing spells boost maximum health by 40 for 60 seconds."):
        "Lorsque vous avez toute votre santé, les sorts de soin augmentent votre santé maximale de 40 points pendant 60 secondes.",
    ("0A000BC2|PathOfSorcery.esp", "Wards are 50% stronger and cost 30% less magicka to cast. If not wearing any chest armor, wards cost 50% less magicka to cast."):
        "Les barrières sont 50 % plus puissantes et coûtent 30 % de magie en moins. Sans armure sur le torse, elles coûtent 50 % de magie en moins.",
    ("0A000BC3|PathOfSorcery.esp", "Wards are 75% stronger and cost 50% less magicka to cast. If not wearing any chest armor, wards cost 70% less magicka to cast."):
        "Les barrières sont 75 % plus puissantes et coûtent 50 % de magie en moins. Sans armure sur le torse, elles coûtent 70 % de magie en moins.",
    ("0A000BC8|PathOfSorcery.esp", "Those affected by Aura of Light gain 50 armor for every person affected, up to 300 points."):
        "Les personnes affectées par Aura de lumière gagnent 50 points d'armure par personne affectée, jusqu'à 300 points.",
    ("0A000BC9|PathOfSorcery.esp", "Those affected by Aura of Light will be saved from a killing blow, healing 200 points. Only works once per battle per person."):
        "Les personnes affectées par Aura de lumière seront sauvées d'un coup mortel en récupérant 200 points de santé. Ne fonctionne qu'une fois par combat par personne.",
    ("0A000BFB|PathOfSorcery.esp", "Runes deal twice as much damage if the target is unaware that anything is amiss."):
        "Les runes infligent deux fois plus de dégâts si la cible n'est pas en alerte.",
    ("0A000BFE|PathOfSorcery.esp", "Align yourself with Winter, shunning Inferno and Storm. While a frost spell is equipped, your stamina regenerates faster; casting frost spells creates an ice shield to protect you. Grants the power \"Summon Blizzard\".  (Can only choose 1 elemental mastery)"):
        "Alignez-vous avec l'Hiver, délaissant l'Enfer et la Tempête. Lorsqu'un sort de glace est équipé, votre vigueur se régénère plus vite ; lancer des sorts de glace crée un bouclier de glace protecteur. Octroie le pouvoir « Invocation de blizzard ». (Une seule maîtrise élémentale possible)",
}

modified_files_count = 0
realigned_strings_count = 0

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        file_modified = False
        for s in items:
            form_id = s.get('form_id', '')
            orig = (s.get('original') or '').strip()
            
            key = (form_id, orig)
            if key in exact_realignments:
                new_trans = exact_realignments[key]
                if 'string' in s:
                    s['string'] = new_trans
                if 'translation' in s:
                    s['translation'] = new_trans
                s['status'] = 'TranslationComplete'
                file_modified = True
                realigned_strings_count += 1
                print(f"Realigned in {p.name}: {orig[:40]} -> {new_trans[:40]}")
            # Also fallback on exact original text match for unique long perk descriptions
            elif any(k[1] == orig for k in exact_realignments):
                target_key = next(k for k in exact_realignments if k[1] == orig)
                new_trans = exact_realignments[target_key]
                if 'string' in s:
                    s['string'] = new_trans
                if 'translation' in s:
                    s['translation'] = new_trans
                s['status'] = 'TranslationComplete'
                file_modified = True
                realigned_strings_count += 1
                print(f"Realigned (by text) in {p.name}: {orig[:40]} -> {new_trans[:40]}")
                
        if file_modified:
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            modified_files_count += 1
    except Exception:
        pass

print(f"\nDone! Realigned {realigned_strings_count} descriptions across {modified_files_count} files.")
