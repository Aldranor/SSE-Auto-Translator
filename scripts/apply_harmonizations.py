import json
import re
from pathlib import Path

db_dir = Path('data/user/database/french')

# 1. Exact string harmonizations: { original_text: harmonized_translation }
harmonizations = {
    # Locations
    "Skyrim": "Bordeciel",
    "Bits and Pieces": "Bric-à-brac",
    "Hob's Fall Cave": "Grotte de Sourcechaude",
    "Sky Haven Temple": "Temple d'Havreciel",
    "Volkihar Keep": "Château Volkihar",
    "Sadri's Used Wares": "Les Occasions de Sadri",
    "The Frozen Hearth": "Le Foyer gelé",
    "The Ragged Flagon - Cistern": "La Cruche percée - Réservoir",
    "Dwemer Museum": "Musée dwemer",
    
    # Perks / Skills
    "Augmented Frost": "Gel pénétrant",
    "Augmented Shock": "Foudre déchaînée",
    "Twin Souls": "Âmes jumelles",
    
    # Spells / Powers / Magic
    "Frostbite": "Froid mordant",
    "Icy Spear": "Lance gelée",
    "Drain Health": "Ponction de santé",
    "Drain Life": "Ponction de vie",
    "Absorb Magicka": "Siphon de magie",
    "Missile of Molag Bal": "Projectile de Molag Bal",
}

harmonized_count = 0
harmonized_files = 0
unclosed_tags_fixed = 0

for p in db_dir.rglob('*.json'):
    if p.name == 'index.json':
        continue
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data if isinstance(data, list) else data.get('strings', [])
        
        file_modified = False
        for s in items:
            orig = (s.get('original') or '').strip()
            trans = (s.get('string') or s.get('translation') or '').strip()
            rec_type = s.get('type') or ''
            
            # Harmonization check
            if orig in harmonizations:
                target = harmonizations[orig]
                # Only apply to names (not long descriptions)
                if len(orig) < 60 and not ('DESC' in rec_type or 'DNAM' in rec_type):
                    if trans != target:
                        if 'string' in s:
                            s['string'] = target
                        if 'translation' in s:
                            s['translation'] = target
                        s['status'] = 'TranslationComplete'
                        file_modified = True
                        harmonized_count += 1
                        print(f"[{p.name}] Harmonized '{orig}': '{trans}' -> '{target}'")
                        
            # Unclosed font tag check in book/message text
            if trans and ('<font' in trans.lower()):
                open_font = len(re.findall(r'<font\b', trans, re.IGNORECASE))
                close_font = len(re.findall(r'</font>', trans, re.IGNORECASE))
                if open_font > close_font:
                    missing_close = open_font - close_font
                    fixed_trans = trans + ("</font>" * missing_close)
                    if 'string' in s:
                        s['string'] = fixed_trans
                    if 'translation' in s:
                        s['translation'] = fixed_trans
                    file_modified = True
                    unclosed_tags_fixed += 1
                    
        if file_modified:
            with open(p, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            harmonized_files += 1
    except Exception:
        pass

print(f"\nDone! Harmonized {harmonized_count} strings and fixed {unclosed_tags_fixed} unclosed tags across {harmonized_files} files.")
