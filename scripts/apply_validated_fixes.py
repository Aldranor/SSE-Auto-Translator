import json
import re
from pathlib import Path

db_dir = Path('data/user/database/french')

# 1. Update Market mods
kojak_files = [
    Path('data/user/database/french/Marché extérieur de Blancherive/Kojaks Whiterun Market.esp.json'),
    Path("data/user/database/french/Whiterun Outskirts Market - Miggyluv's NPCs - French/WONpcs.esp.json"),
    Path('data/user/database/french/Marché extérieur de Blancherive/Kojaks Whiterun Market for JK Whiterun Outskirts.esp.json'),
]

for p in kojak_files:
    if p.exists():
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        modified = False
        for s in items:
            orig = s.get('original', '')
            if orig == 'Sinnen the Fence':
                s['string'] = 'Sinnen la receleuse'
                s['status'] = 'TranslationComplete'
                modified = True
            elif orig == 'Thieves Guild Fence Chest':
                s['string'] = 'Coffre de receleuse de la Guilde des voleurs'
                s['status'] = 'TranslationComplete'
                modified = True
            elif orig == 'Trueaz Ball':
                s['string'] = 'Balle de Trueaz'
                s['status'] = 'TranslationComplete'
                modified = True
            elif orig == 'Pen Key':
                s['string'] = "Clé de l'enclos"
                s['status'] = 'TranslationComplete'
                modified = True
            elif orig == "Owl's Perch Inn":
                s['string'] = "Auberge de la Chouette perchée"
                s['status'] = 'TranslationComplete'
                modified = True
        if modified:
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print('Updated Kojak file:', p)

# 2. Cleanup illegal numeric tags in all files (e.g., Abyss)
# like <10> -> 10, <5> -> 5
cleaned_numeric_tags_count = 0
cleaned_files = 0

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        modified = False
        for s in items:
            trans = s.get('string') or s.get('translation')
            if not trans:
                continue
            
            # Find tags like <10>, <5>, <25>
            illegal_tags = re.findall(r'<([0-9]+)>', trans)
            if illegal_tags:
                new_trans = re.sub(r'<([0-9]+)>', r'\1', trans)
                if 'string' in s:
                    s['string'] = new_trans
                if 'translation' in s:
                    s['translation'] = new_trans
                modified = True
                cleaned_numeric_tags_count += len(illegal_tags)
                
            # Lore fixes: Montagne rouge -> Mont Écarlate (for Vvardenfell Red Mountain)
            orig = s.get('original', '')
            if orig == 'Red Mountain' and trans == 'Montagne rouge':
                if 'string' in s:
                    s['string'] = 'Mont Écarlate'
                if 'translation' in s:
                    s['translation'] = 'Mont Écarlate'
                modified = True
                
            # Grammatical accord: Pas obscure -> Pas obscur
            if orig == 'Shadow Step' and trans == 'Pas obscure':
                if 'string' in s:
                    s['string'] = 'Pas obscur'
                if 'translation' in s:
                    s['translation'] = 'Pas obscur'
                modified = True
            if orig == 'Abyssal Shadow Step' and trans == 'Pas obscure abyssal':
                if 'string' in s:
                    s['string'] = 'Pas obscur abyssal'
                if 'translation' in s:
                    s['translation'] = 'Pas obscur abyssal'
                modified = True
                
        if modified:
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            cleaned_files += 1
    except Exception as e:
        pass

print(f"Cleaned {cleaned_numeric_tags_count} illegal numeric tags across {cleaned_files} files.")
