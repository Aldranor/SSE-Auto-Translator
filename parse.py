import xml.etree.ElementTree as ET
import json
import re

def main():
    translated_file = r"C:\Users\mouaw\OneDrive\Bureau\SSE-AT-nolvus\data\user\export\fanatical enemies.esp - Copie.json"
    
    db_files = [
        r"C:\Users\mouaw\OneDrive\Bureau\SKSE\Plugins\DynamicStringDistributor\fanatical enemies.esp\SSE-AT_exported.json",
    ]
    
    skyrim_files_path = r"C:\Users\mouaw\OneDrive\Documents\Translations\SSE-Auto-Translator-dev\src\data\app\database\french"
    json_files = [str(file) for file in Path(skyrim_files_path).rglob("*.json")]
    xml_files = [str(file) for file in Path(skyrim_files_path).rglob("*.xml")]

    db_files.extend(json_files)
    db_files.extend(xml_files)
        
    xml_patterns = [re.compile(r'of (.+)')]
    translations = []
    addSkyrimDb = False
    
    if addSkyrimDb:
        for db in db_files:
            if ".xml" in db:
                translations.append(extract_data_from_xml(db, xml_patterns))
            else:
                translations.append(extract_data_from_json(db, xml_patterns))

    if ".xml" in translated_file:
        replace_data_in_xml(translated_file, translations)
    else:
        replace_data_in_json(translated_file, translations)

def load_json_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return {item['original']: item['string'] for item in data}


ignored_translations = {
    "of Frost": None,
    "of Shock": None,
    "of Fire": None,
    "of Death": None,
    "of Ice": None,
    "of Freezing": None,
    "of Lightning": None,
}

translations = {
    'Sanctified':['béni', 'bénie'],
    'Hallowed':['sanctifié', 'sanctifiée'],
    'Reverent':['vertueux', 'vertueuse'],
    'Blessed':['pieux', 'pieuse'],
    'Holy':['grâce', 'grâce'],
    "Virtuous":['saint', 'sainte'],
    "Executioner's":['de bourreau', 'de bourreau'],
    "Bloodstained":['ensanglanté', 'ensanglantée'],
    "Black Bear Ancient Nord":["d'Ours noir nordique antique", "d'Ours noir nordique antique"],
    "Rogue Light Elven":['de voleur elfique léger', 'de voleur elfique légère',],
    "Vampire Royal Knight":['de chevalier vampire royal', 'de chevalier vampire royal'],
    "Netherlight":['de lumière du néant', 'de lumière du néant'],
    "Regal paladin":['de paladin royal', 'de paladin royal'],
}
    
mwords = ['espadon', 'hood', 'gant', 'casque', 'trident', 'bâton', 'quarterstaff']
pwords = ['gantelets', 'gloves', 'griffes', 'claws' , 'boots']
    
    
specific_translations = {
    "of the Conjurer": "de l'Invocateur",
    "of the Greybeards": 'des Grises-barbes',
    "of the Ancients": 'des Anciens',
    "of the Fates": 'des Parques',
    "of Emminent magicka": 'de magie majeure',
    "of Eminent Squire": "de noble écuyer",
    "of the Dragoon":"du dragon",
    "of the Summoner": "de l'Évocateur",
    "of Renwal": 'de renouveau',
    "of Energies": "d'énergies",
    "of Wile": "de ruse",
    "Griffes de fer Left":"Griffes de fer gauches",
    "of soil": "de sol",
    "of lightning blasts": 'de souffle foudroyant',
    'of lightning': 'de tempête',
    "Replica": 'Réplique',
    "of Shock": 'de foudre',
    "of Executioner's": "de bourreau",
    "of Faiure": "d'échec",
    "of Greybeards": "de Grisebarbes",
    "of Dungeon": "de donjon",
    'of frost': 'de glace',
    "of the Coven": "du cercle",
    'of fire': 'de feu',
    "of Deaths Door": 'des portes de la mort',
    "of Death": 'de la mort',
    "of Sanctity": 'de sainteté',
    "of Shorting":"de raccourcissement",
    "of Executions": "d'exécution",
    "of Reverence": "de révérance",
    "of Catapulting":"de catapultage",
    "of Holy Light": "de lumière sacrée",
    "of Epicness": "d'épopée",
    "of banishing": 'de bannissement',
    "Nordic Spear": "Lance Nordique",
    "Nordic spear": "Lance Nordique",
    "of Infernal Blasts": "d'explosion infernale",
    "Stalhrim Spear": "Lance de Stahlrim",
    "Stalhrim spear": "Lance de stahlrim",
    "Iron Spear": "Lance de fer",
    "Iron spear": "Lance de fer",
    "Steel Spear": "Lance en acier",
    "Elven Spear": "Lance Elfique",
    "Steel spear": "Lance en acier",
    "Elven spear": "Lance Elfique",
    "of Wights": "d'âmes en peine",
    "Dwarven shortspear": "Lance courte Dwemer",
    "Stalhrim Spear": "Lance de Stahlrim",
    "Silver Spear": "Lance en argent",
    "Dwarven Spear": "Lance Dwemer",
    "Stalhrim spear": "Lance de Stahlrim",
    "Silver spear": "Lance en argent",
    "Dwarven spear": "Lance Dwemer",
    "Silver Trident": "Trident en argent",
    "Elven Trident": "Trident Elfique",
    "Stalhrim Trident": "Trident de Stalhrim",
    "Stalhrim trident": "Trident de Stalhrim",
    "Iron Trident":"Trident en fer",
    "Daedric Trident":"Trident daedrique",
    "Ebony Trident": "Trident d'ébonite",
    "Glass Trident": "Trident de verre",
    "Nordic Trident":"Trident nordique",
    "Orcish Trident": "Trident orque",
    "Dwarven Trident": "Trident Dwemer",
    "Ancient Nord Spear": "Lance nordique antique",
    "Glass Spear": "Lance de verre",
    "Left": "gauches",
    "Glass spear": "Lance de verre",
    "Silver Quarterstaff": "Bâton de combat en argent",
    "Steel Quarterstaff": "Bâton de combat en acier",
    "Glass Quarterstaff": "Bâton de combat de verre",
    "Ancient nord honed shortspear":"Lance courte nordique antique affûtée",
    "Dwarven spear": "Lance dwemer",
    "Ebony shortspear": "Lance courte d'ébonite",
    "Elven spear":"Lance elfique",
    "Glass shortspear":"Lance courte de verre",
    "Daedric shortspear": "Lance courte daedrique",
    "Ancient Nord Honed Spear": "Lance nordique antique affûtée",
    "Ancient Nord Honed Spear": "Lance nordique antique affûtée",
    "Daedric Halberd":"Hallebarde daedrique",
    "Glass Halberd":"Hallebarde de verre",
    "Iron Halberd":"Hallebarde de fer",
    "Hood Light":"Capuchon léger",
    "Boots Light":"Bottes légères",
    "Cuirass light":"Cuirasse légère",
    "Gauntlets":"Gantelets",
    "Lowered Hood":"Capuchon ouvert",
    "Hood Helmet":"Capuchon",
    "Helmet":"Casque",
    'Shield':"Bouclier",
    "Boots":"Bottes",
    'Hood':'Capuchon',
    "Gloves":"Gantelets",
    "Armor":"Armure",
    "Greatsword":"Espadon",
    'Sword':'Épée',
    'Dagger':'Dague'
}

def extract_translation(traduit, original):
    patterns = [
        re.compile(r'de ((?:(?! de| d\'| du | pour)[\w\s-])+)$'),
        re.compile(r'd\'((?:(?! de| d\'| du | pour)[\w\s-])+)$'),
        re.compile(r'du ((?:(?! de| d\'| du | pour)[\w\s-])+)$')
    ]

    for pattern in patterns:
        match = pattern.search(traduit)
        original_word_count = len(original.split())
            
        if original in ignored_translations:
            return None
        
        if original_word_count < 2:
            return None

        if match:
        
            match_text = match.group(0).strip()
                
            if len(re.findall(r'\bde\b|\bd\'\b|\bdu\b', match.group(0))) > 1:
                return None
                                                  
            if "nordique antique" in match_text or "éclipse enchantée" in match_text:
                return None
          
            if " en " in match_text:
                return None
            
            return match_text
    return None

def extract_data_from_json(path, patterns, enchantements=True):
    data = []
    seen = set()
    with open(path, 'r', encoding='utf-8') as file:
        for item in json.load(file):
            original = item.get('original', '')
            traduit = item.get('string', '')
            type = item.get('type', '')
            original_word_count = len(original.split())
            status = item.get('status', 'TranslationComplete')
            
            if status == 'TranslationComplete':
                if "SPEL" in type:                
                    entry = {"original": original, "string": traduit}   
                    entry_tuple = tuple(entry.items())
                    original_word_count = len(original.split())
                    
                    if entry_tuple not in seen and traduit is not None and original_word_count > 2:
                        seen.add(entry_tuple)
                        data.append(entry)
                
                if enchantements:
                    for pattern in patterns:
                        match = pattern.search(original)
                        if match:
                            original_extract = 'of ' + match.group(1)
                            traduit_extract = extract_translation(traduit, original_extract)
                            if traduit_extract:
                                entry = {"original": original_extract, "string": traduit_extract}
                                entry_tuple = tuple(entry.items())
                                if entry_tuple not in seen:
                                    seen.add(entry_tuple)
                                    data.append(entry)
                          
        for key, translation in specific_translations.items():
            entry = {"original": key, "string": translation}
            data.append(entry)

    return {item['original']: item['string'] for item in data}


def extract_data_from_xml(xml_file, patterns, enchantements=True):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    seen = set()
    
    for esp in root.findall('ESP'):
        original = esp.find('ORIGINAL').text if esp.find('ORIGINAL') is not None else ''
        traduit = esp.find('TRADUIT').text if esp.find('TRADUIT') is not None else ''
        type =  esp.find('GRUP').text

        if "ARMO" in type or "ALCH" in type or "WEAP" in type or "MGEF" in type or "MISC" in type or "ACTI" in type or "LIGH" in type:                
                entry = {"original": original, "string": traduit}   
                entry_tuple = tuple(entry.items())
                original_word_count = len(original.split())
                
                if entry_tuple not in seen and traduit is not None and original_word_count > 1:
                    seen.add(entry_tuple)
                    data.append(entry)
                
        if enchantements:
            for pattern in patterns:
                match = pattern.search(original)
                if match:
                    original_extract = 'of ' + match.group(1)
                    traduit_extract = extract_translation(traduit, original_extract)
                    if traduit_extract:
                        entry = {"original": original_extract, "string": traduit_extract}
                        entry_tuple = tuple(entry.items())
                        if entry_tuple not in seen:
                            seen.add(entry_tuple)
                            data.append(entry)
                          
    for key, translation in specific_translations.items():
        entry = {"original": key, "string": translation}
        data.append(entry)

    return {item['original']: item['string'] for item in data}

def replace_data_in_xml(xml_file, translation_maps):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for esp in root.findall('ESP'):
        original = esp.find('ORIGINAL').text if esp.find('ORIGINAL') is not None else ''
        traduit_element = esp.find('TRADUIT')
        traduit = traduit_element.text if traduit_element is not None else ''
        for translation_map in translation_maps:
            for key, value in translation_map.items():
                if key.lower() in original.lower():
                    original = traduit

                    try:
                        traduit = traduit.replace(key, value)

                        if original == traduit:
                            traduit = traduit.lower().replace(key.lower(), value).capitalize()
                    except Exception as e:
                        print(f"Error replacing '{key}' with '{value}': {e}")

        if traduit_element is not None:
            traduit_element.text = traduit
    tree.write(xml_file.replace('.xml', '_updated.xml'), encoding='utf-8', xml_declaration=True)


def translate_hallowed(original, translation):
    for key, value in translations.items():
        if key in original:
            translation = translation.replace(key, '').strip()  # Strip leading/trailing spaces after removal            
            translated = False
            
            for mword in mwords:
                if mword in translation.lower():        
                    translation = translation + ' ' + value[0]
                    if 'of ' + value[0] in translation:
                        translation = translation.replace('of ', '')
                        
                    translated = True
                    break
                    
            if not translated:
                translation = translation + ' ' + value[1]
                if 'of ' + value[1] in translation:
                    translation = translation.replace('of ', '')

            for pword in pwords:
                if pword in translation.lower():
                    translation = translation + 's'
            
            return translation
    
    return translation

def replace_data_in_json(json_file, translation_maps):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for entry in data:
        original = entry['original']
        traduit = entry['string']
        
        traduit = translate_hallowed(original, traduit)
                 
        for translation_map in translation_maps:
            for key, value in translation_map.items():
                
                if key.lower() in original.lower():
                    if "Reinforced" in original and "renforcé" not in value and "of" not in key:
                        continue
            
                    try:
                        traduit = traduit.replace(key, value)

                        if original.lower() == traduit.lower():
                            traduit = re.sub(re.escape(key), value, traduit, flags=re.IGNORECASE)
                    except Exception as e:
                        print(f"Error replacing '{key}' with '{value}': {e}")

        entry['string'] = traduit

    output_file = json_file.replace('.json', '_updated.json')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('[')
        for i, entry in enumerate(data):
            json.dump(entry, f, ensure_ascii=False, separators=(',', ':'))
                    
            if i < len(data) - 1:
                f.write(',\n')
                    
        f.write(']')

    print(f"Updated JSON saved to {output_file}")

from pathlib import Path

main()