import os
import json
import re
from pathlib import Path
from collections import defaultdict

db_dir = Path('data/user/database/french')

# Filtered english words (NOT existing in French)
real_english_words = [
    r'\bkey\b', r'\bchest\b', r'\bsword\b', r'\bbow\b', r'\bboots\b', r'\bcuirass\b',
    r'\bshield\b', r'\bring\b', r'\bamulet\b', r'\bgauntlets\b', r'\bhelmet\b',
    r'\bdagger\b', r'\bstaff\b', r'\barrow\b', r'\bdoor\b', r'\bgate\b',
    r'\bhouse\b', r'\binn\b', r'\bfence\b', r'\bshack\b'
]
word_regex = re.compile('|'.join(real_english_words), re.IGNORECASE)

ignored_mods = [
    'legacy of the dragonborn', "l'héritage de l'enfant de dragon", 'lotd',
    'apocalypse', 'ordinator', 'falskaar', 'wyrmstooth', 'inigo', 'lucien',
    'vigilant', 'unslaad', 'glenmoril', 'bruma', 'bsheartland', 'bsassets',
    'interesting npcs', '3dnpc', 'adamant', 'mysticism', 'aetherius',
    'scion', 'manbeast', 'simonrim', 'vokrii', 'enai', 'ussep', 'unofficial skyrim special edition patch'
]

report = {
    'false_friends': [],
    'syntax_calques': [],
    'broken_variables': [],
    'untranslated_in_patches': [],
    'mod_inconsistencies': []
}

# 1. Mod-specific check for Marché de Blancherive (Kojaks Whiterun Market)
kojak_files = [
    Path(r"data/user/database/french/Marché extérieur de Blancherive/Kojaks Whiterun Market.esp.json"),
    Path(r"data/user/database/french/Whiterun Outskirts Market - Miggyluv's NPCs - French/WONpcs.esp.json")
]

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    mod_name = p.parent.name
    mod_name_lower = mod_name.lower()
    file_name = p.name
    file_name_lower = file_name.lower()
    
    if any(ig in mod_name_lower or ig in file_name_lower for ig in ignored_mods):
        continue
    
    try:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        items = d if isinstance(d, list) else d.get('strings', [])
        
        # Track translations by original to find internal inconsistencies
        orig_to_trans = defaultdict(set)
        
        for s in items:
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            form_id = s.get('form_id', '')
            
            if not trans or not orig:
                continue
            
            orig_to_trans[orig].add(trans)
            
            # Check false friends
            if 'fence' in orig.lower() and 'barri' in trans.lower():
                report['false_friends'].append({
                    'mod': mod_name,
                    'file': file_name,
                    'form_id': form_id,
                    'original': orig,
                    'current': trans,
                    'proposal': trans.replace('barrière', 'receleuse').replace('Barrière', 'Receleuse').replace('barriere', 'receleuse'),
                    'reason': 'Fence dans la Guilde des voleurs signifie Receleur/Receleuse, pas barrière.'
                })
            
            if 'pen key' in orig.lower() and 'crayon' in trans.lower():
                report['false_friends'].append({
                    'mod': mod_name,
                    'file': file_name,
                    'form_id': form_id,
                    'original': orig,
                    'current': trans,
                    'proposal': "Clé de l'enclos",
                    'reason': 'Pen désigne un enclos/cage à bétail, pas un crayon à papier.'
                })
                
            # Syntax calques (e.g. Trueaz Boule)
            if re.match(r'^[A-Z][a-z]+ Boule$', trans) or re.match(r'^[A-Z][a-z]+ Balle$', trans):
                word1 = trans.split()[0]
                report['syntax_calques'].append({
                    'mod': mod_name,
                    'file': file_name,
                    'form_id': form_id,
                    'original': orig,
                    'current': trans,
                    'proposal': f"Balle de {word1}",
                    'reason': "Inversion syntaxique issue d'un calque de l'anglais."
                })
            
            # Variables check
            orig_tags = re.findall(r'<[a-zA-Z0-9_%]+>', orig)
            trans_tags = re.findall(r'<[a-zA-Z0-9_%]+>', trans)
            
            # Check for illegal numeric tags like <10>, <5> in translation
            illegal_numeric_tags = [t for t in trans_tags if re.match(r'<[0-9]+>', t)]
            if illegal_numeric_tags:
                cleaned_trans = trans
                for t in illegal_numeric_tags:
                    cleaned_trans = cleaned_trans.replace(t, t[1:-1])
                report['broken_variables'].append({
                    'mod': mod_name,
                    'file': file_name,
                    'form_id': form_id,
                    'original': orig,
                    'current': trans,
                    'proposal': cleaned_trans,
                    'reason': f"Balises numériques illégales {illegal_numeric_tags} introduites dans la traduction (font bugger le moteur de jeu)."
                })
            elif orig_tags and set(orig_tags) != set(trans_tags):
                # Variable was dropped or corrupted
                report['broken_variables'].append({
                    'mod': mod_name,
                    'file': file_name,
                    'form_id': form_id,
                    'original': orig,
                    'current': trans,
                    'proposal': 'À réaligner sur les balises de la source',
                    'reason': f"Balises discordantes: Source {orig_tags} vs Traduction {trans_tags}."
                })
            
            # Untranslated English in patches/mods
            if orig == trans and len(orig.split()) > 1 and not orig.startswith('<') and not orig.startswith('['):
                if word_regex.search(orig):
                    report['untranslated_in_patches'].append({
                        'mod': mod_name,
                        'file': file_name,
                        'form_id': form_id,
                        'original': orig,
                        'current': trans
                    })
        
        # Check internal inconsistencies
        for orig, translations in orig_to_trans.items():
            if len(translations) > 1 and len(orig.split()) > 1:
                # filter trivial differences like trailing whitespace
                clean_t = {t.strip() for t in translations}
                if len(clean_t) > 1:
                    report['mod_inconsistencies'].append({
                        'mod': mod_name,
                        'file': file_name,
                        'original': orig,
                        'variants': list(clean_t)
                    })

    except Exception:
        pass

print("=== REFINED REPORT STATS ===")
print("False friends:", len(report['false_friends']))
print("Syntax calques:", len(report['syntax_calques']))
print("Broken variables:", len(report['broken_variables']))
print("Untranslated in patches:", len(report['untranslated_in_patches']))
print("Internal inconsistencies:", len(report['mod_inconsistencies']))

with open('refined_audit_report.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)
