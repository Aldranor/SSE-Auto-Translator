import os
import xml.etree.ElementTree as ET
import json
import re

def load_json_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return {item['original']: item['string'] for item in data}


def extract_data_from_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    
    for esp in root.findall('ESP'):
        traduit = esp.find('TRADUIT').text if esp.find('TRADUIT') is not None else ''
        entry = {"string": traduit}
        data.append(entry)
            
    json_file = os.path.splitext(xml_file)[0] + '.json'
    i = 1
    
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write('[')
        for entry in data:
            json.dump(entry, f, ensure_ascii=False, separators=(',', ':'))
            
            if(i <= len(data) - 1):
                f.write(', \n')
            else:
                f.write('\n')
                
            i = i + 1  
            
        f.write(']')

    print('translation file created')
    

def replace_data_in_xml(xml_file, adapted_file):
    
    with open(adapted_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    i = 0
    
    for esp in root.findall('ESP'):
        traduit_element = esp.find('TRADUIT')
        traduit_element.text = data[i]['string']
        i = i + 1 

    tree.write(xml_file.replace('.xml', '_updated.xml'), encoding='utf-8', xml_declaration=True)
    
    print('translation updated')

def main():
    translated_file = r"C:\Users\mouaw\Downloads\eet___esp_esm_translator_4.22\Bases Persos\Skyrim SE\sithis mod - lovecraftian inspired quest.xml"    
    json_updated = r"C:\Users\mouaw\OneDrive\Bureau\update_file.json"
    
    extract_data_from_xml(translated_file)
    replace_data_in_xml(translated_file, json_updated)
        
if __name__ == "__main__":
    main()