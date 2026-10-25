import os
import json
import re
from pathlib import Path

db_dir = Path('data/user/database/french')

suspicious_words = [
    r'\bkey\b', r'\bchest\b', r'\bsword\b', r'\bbow\b', r'\bboots\b', r'\bcuirass\b',
    r'\bshield\b', r'\bring\b', r'\bamulet\b', r'\bgauntlets\b', r'\bhelmet\b',
    r'\bdagger\b', r'\bstaff\b', r'\barrow\b', r'\bpotion\b', r'\bscroll\b',
    r'\bdoor\b', r'\bgate\b', r'\bhouse\b', r'\binn\b'
]
word_regex = re.compile('|'.join(suspicious_words), re.IGNORECASE)

# Ignored mods (official / big reputable translations from Confrérie / Nexus)
ignored_mods = [
    'legacy of the dragonborn', "l'héritage de l'enfant de dragon", 'lotd',
    'apocalypse', 'ordinator', 'falskaar', 'wyrmstooth', 'inigo', 'lucien',
    'vigilant', 'unslaad', 'glenmoril', 'bruma', 'bsheartland', 'bsassets',
    'interesting npcs', '3dnpc', 'adamant', 'apothecary', 'mysticism', 'aetherius',
    'scion', 'manbeast', 'simonrim', 'vokrii', 'enai', 'ussep', 'unofficial skyrim special edition patch'
]

findings = []

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    mod_name_lower = p.parent.name.lower()
    file_name_lower = p.name.lower()
    
    if any(ig in mod_name_lower or ig in file_name_lower for ig in ignored_mods):
        continue
    
    try:
        with open(p, 'r', encoding='utf-8') as f:
            d = json.load(f)
        items = d if isinstance(d, list) else d.get('strings', [])
        
        for s in items:
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            form_id = s.get('form_id', '')
            status = s.get('status', '')
            
            if not trans or not orig:
                continue
            
            # Check 1: Still identical to original while original is english (more than 1 word)
            if orig == trans and len(orig.split()) > 1 and not orig.startswith('<') and not orig.startswith('['):
                if word_regex.search(orig):
                    findings.append({
                        'type': 'Untranslated English in Patch/Mod',
                        'mod': p.parent.name,
                        'file': p.name,
                        'form_id': form_id,
                        'original': orig,
                        'translation': trans
                    })
            
            # Check 2: False friends or strange patterns
            if 'fence' in orig.lower() and 'barri' in trans.lower():
                findings.append({
                    'type': 'False friend: Fence -> Barrière instead of Receleur',
                    'mod': p.parent.name,
                    'file': p.name,
                    'form_id': form_id,
                    'original': orig,
                    'translation': trans
                })
            
            # Check 3: Suspicious english word remaining in translation
            elif orig != trans:
                m = word_regex.search(trans)
                if m:
                    matched_word = m.group(0).lower()
                    # avoid false positives where matched word is legitimately part of French
                    findings.append({
                        'type': f'Suspicious English word "{matched_word}" in translation',
                        'mod': p.parent.name,
                        'file': p.name,
                        'form_id': form_id,
                        'original': orig,
                        'translation': trans
                    })
            
            # Check 4: Variables mismatch (<mag>, <dur>, etc.)
            orig_vars = re.findall(r'<[a-zA-Z0-9_%]+>', orig)
            trans_vars = re.findall(r'<[a-zA-Z0-9_%]+>', trans)
            if orig_vars and set(orig_vars) != set(trans_vars):
                findings.append({
                    'type': 'Variable mismatch',
                    'mod': p.parent.name,
                    'file': p.name,
                    'form_id': form_id,
                    'original': orig,
                    'translation': trans,
                    'orig_vars': orig_vars,
                    'trans_vars': trans_vars
                })
    except Exception as e:
        pass

print(f"Total patch/imported mod findings: {len(findings)}")
with open('patch_audit_findings.json', 'w', encoding='utf-8') as f:
    json.dump(findings, f, indent=2, ensure_ascii=False)
