import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('listing_traductions_locales_non_verifiees.md', 'r', encoding='utf-8') as f:
    text = f.read()

cat10_part = text.split("## 📁 Autres Patchs de Compatibilité & Corrections")[1]
cat10_json_names = set(re.findall(r'`([^`]+\.es[pml]\.json)`', cat10_part))

base = 'data/user/database/french'
found_files = {}

for root, dirs, files in os.walk(base):
    for f in files:
        f_lower = f.lower()
        for target in cat10_json_names:
            if f_lower == target.lower():
                found_files[target] = os.path.join(root, f)

checks = [
    (r'\bbarri[eè]re\b', 'fence/barrière au lieu de receleur'),
    (r'\bmontagne\s+rouge\b', 'Montagne rouge au lieu de Mont Écarlate'),
    (r'\bclair-osbcur\b', 'coquille clair-osbcur'),
    (r'\bfaillaise\b', 'vérifier si Falkreath'),
    (r'\bcavern\b', 'anglais cavern'),
    (r'\bcave\b', 'anglais cave (attention fausse alerte si français)'),
    (r'\bshrine\b', 'anglais shrine'),
    (r'\btemple of\b', 'anglais temple of'),
    (r'\btower\b', 'anglais tower'),
    (r'\bhall of\b', 'anglais hall of'),
    (r'\bfort\b', 'anglais fort'),
    (r'\bsword\b', 'anglais sword'),
    (r'\bshield\b', 'anglais shield'),
    (r'\bdagger\b', 'anglais dagger'),
    (r'\barmor\b', 'anglais armor'),
    (r'\bboots\b', 'anglais boots'),
    (r'\bgauntlets\b', 'anglais gauntlets'),
    (r'\bhelmet\b', 'anglais helmet'),
]

flagged = []

for target_name, fpath in found_files.items():
    if 'vigilant subtitle fix' in target_name:
        continue
    data = json.load(open(fpath, encoding='utf-8'))
    for item in data:
        curr = str(item.get('string') or '')
        orig = str(item.get('original') or '')
        typ = item.get('type')
        fid = item.get('form_id')
        idx = item.get('index')
        
        # Check Montagne rouge
        if 'montagne rouge' in curr.lower():
            flagged.append((target_name, fid, typ, idx, orig, curr, "Montagne rouge -> Mont Écarlate"))
        if 'clair-osbcur' in curr.lower():
            flagged.append((target_name, fid, typ, idx, orig, curr, "clair-osbcur -> Clair-Obscur"))
        if 'falkreath' in orig.lower() and 'faillaise' in curr.lower():
            flagged.append((target_name, fid, typ, idx, orig, curr, "Falkreath -> Épervine (et non Faillaise)"))
        if 'slash' in orig.lower() and 'flèche' in curr.lower():
            flagged.append((target_name, fid, typ, idx, orig, curr, "Slash -> Entaille (et non Flèche)"))
        if 'barrière' in curr.lower() and 'fence' in orig.lower():
            flagged.append((target_name, fid, typ, idx, orig, curr, "Fence -> Receleur (et non Barrière)"))

print(f"Total specific false friends flagged: {len(flagged)}")
for fl in flagged:
    print(f"[{fl[0]}] {fl[1]} | {fl[2]} | {fl[3]}")
    print(f"   Orig: {repr(fl[4])}")
    print(f"   Curr: {repr(fl[5])}")
    print(f"   Note: {fl[6]}")
