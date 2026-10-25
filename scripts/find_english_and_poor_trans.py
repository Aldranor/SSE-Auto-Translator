import json
import re
from pathlib import Path
from collections import defaultdict

db_dir = Path('data/user/database/french')

english_grammar_words = [
    r'\bof the\b', r'\bthe\b', r'\bwith\b', r'\band\b', r'\bfrom\b',
    r'\bto\b', r'\bfor\b', r'\bin the\b', r'\bat\b', r'\byour\b'
]
eng_grammar_regex = re.compile('|'.join(english_grammar_words), re.IGNORECASE)

ignored_mods = [
    'legacy of the dragonborn', "l'héritage de l'enfant de dragon", 'lotd',
    'falskaar', 'wyrmstooth', 'inigo', 'lucien',
    'vigilant', 'unslaad', 'glenmoril', 'bruma', 'bsheartland', 'bsassets',
    'interesting npcs', '3dnpc', 'unofficial skyrim special edition patch'
]

untranslated_candidates = []

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    mod_name = p.parent.name
    mod_name_lower = mod_name.lower()
    
    if any(ig in mod_name_lower for ig in ignored_mods):
        continue
        
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        for s in items:
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            form_id = s.get('form_id', '')
            rec_type = s.get('type', '')
            
            if not trans or not orig:
                continue
            
            # Case 1: Exactly untranslated (English == French) and contains English words
            if orig == trans and len(orig.split()) > 1 and not orig.startswith('<') and not orig.startswith('['):
                if eng_grammar_regex.search(orig):
                    untranslated_candidates.append({
                        'mod': mod_name,
                        'file': p.name,
                        'form_id': form_id,
                        'type': rec_type,
                        'original': orig,
                        'translation': trans,
                        'reason': 'Texte identique à la source anglaise contenant des mots grammaticaux anglais'
                    })
            # Case 2: Translation contains English grammar words
            elif orig != trans and len(trans.split()) > 2 and not trans.startswith('<') and not trans.startswith('['):
                # Count English words in translation
                matches = eng_grammar_regex.findall(trans)
                if len(matches) >= 2:
                    untranslated_candidates.append({
                        'mod': mod_name,
                        'file': p.name,
                        'form_id': form_id,
                        'type': rec_type,
                        'original': orig,
                        'translation': trans,
                        'reason': f"Contient des mots anglais dans la traduction: {matches}"
                    })
    except Exception:
        pass

print(f"Total English / poor translation candidates: {len(untranslated_candidates)}")
with open('english_and_poor_translations.json', 'w', encoding='utf-8') as f:
    json.dump(untranslated_candidates, f, indent=2, ensure_ascii=False)

print("\nSample 25 findings:")
for item in untranslated_candidates[:25]:
    print(f"[{item['mod']}] {item['file']} ({item['type']})")
    print(f"  EN: {item['original']}")
    print(f"  FR: {item['translation']}")
    print(f"  Reason: {item['reason']}\n")
