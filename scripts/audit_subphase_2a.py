import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

subphase_2a_mods = [
    'Nolvus Awakening AI Patch - French',
    'Nolvus Awakening Clothes Patch.esp - French',
    'Nolvus Awakening Clothes Balance Patch - French',
    'Nolvus Awakening Gourmet Integration - French',
    'Nolvus Awakening Stances Perk System.esp - French',
    'Nolvus Awakening Ashes of War Stance Framework.esp - French',
    'Nolvus Awakening Seasonal Plant Mashup - French',
    'Nolvus Awakening Custom Outfits.esp - French',
    'Nolvus Awakening Lighting Patch - French',
    'Nolvus - Northern Roads Grass Patches - French',
    'Nolvus Awakening Combat Scaling Overhaul - Prepare to Die - French'
]

base_dir = 'data/user/database/french'

# Build a comprehensive reference dictionary from verified translations & USSEP
ref_map = {}
for root, dirs, files in os.walk(base_dir):
    # Skip Nolvus Awakening itself for reference
    if 'nolvus awakening' in root.lower() or 'nolvus - northern' in root.lower():
        continue
    for f in files:
        if f.endswith('.json') and f != 'index.json':
            fp = os.path.join(root, f)
            try:
                d = json.load(open(fp, encoding='utf-8'))
                if isinstance(d, list):
                    for item in d:
                        fid = item.get('form_id')
                        typ = item.get('type')
                        orig = item.get('original')
                        s = item.get('string')
                        if fid and typ and s and s.strip() and s != orig:
                            # Prefer official or established
                            if (fid, typ) not in ref_map:
                                ref_map[(fid, typ)] = s
            except:
                pass

print(f"Built reference dictionary with {len(ref_map)} validated entries.")

# English indicators
english_words = [
    r'\bthe\b', r'\band\b', r'\bwith\b', r'\bfrom\b', r'\bboots?\b', r'\bcuirass\b',
    r'\bhelmet\b', r'\bgauntlets?\b', r'\bshield\b', r'\bsword\b', r'\baxe\b', r'\bbow\b',
    r'\bdagger\b', r'\bgloves?\b', r'\bhood\b', r'\bring\b', r'\bamulet\b', r'\brobes?\b',
    r'\bcirclet\b', r'\barmor\b', r'\bheavy\b', r'\blight\b', r'\biron\b', r'\bsteel\b',
    r'\bebony\b', r'\bgolden\b', r'\bsilver\b', r'\bdragon\b', r'\bpatch\b', r'\bquest\b'
]
eng_regex = re.compile('|'.join(english_words), re.IGNORECASE)

issues = []

for mod in subphase_2a_mods:
    mod_dir = os.path.join(base_dir, mod)
    if not os.path.exists(mod_dir):
        continue
    files = [f for f in os.listdir(mod_dir) if f.endswith('.json')]
    for fn in files:
        fp = os.path.join(mod_dir, fn)
        try:
            data = json.load(open(fp, encoding='utf-8'))
            for item in data:
                fid = item.get('form_id', '')
                typ = item.get('type', '')
                orig = item.get('original') or ''
                curr = item.get('string') or ''
                
                # Check 1: Missing tag present in original
                orig_tags = re.findall(r'<[^>]+>', orig)
                curr_tags = re.findall(r'<[^>]+>', curr)
                missing_tags = [t for t in orig_tags if t not in curr]
                if missing_tags:
                    issues.append({
                        'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr,
                        'reason': f"Missing tags from original: {missing_tags}"
                    })
                
                # Check 2: Reference mismatch (e.g. known French canonical string)
                ref_val = ref_map.get((fid, typ))
                if ref_val and curr != ref_val:
                    # Filter minor punctuation/whitespace
                    if ref_val.strip().lower() != curr.strip().lower():
                        issues.append({
                            'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr,
                            'ref': ref_val,
                            'reason': f"Reference mismatch with official/master: '{curr}' vs '{ref_val}'"
                        })
                
                # Check 3: Full English text validated as French
                if curr and curr.strip() and orig.strip():
                    if curr.strip() == orig.strip() and len(orig.split()) > 1:
                        # Ignore proper names if NPC_ FULL without english words
                        if typ in ['NPC_ FULL', 'NPC_ SHRT'] and not eng_regex.search(orig):
                            pass
                        elif eng_regex.search(orig):
                            issues.append({
                                'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr,
                                'reason': "Untranslated English string"
                            })
                
                # Check 4: Specific Bethesda lore errors or false friends
                lower_curr = curr.lower()
                if "montagne rouge" in lower_curr:
                    issues.append({'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr, 'reason': "Montagne Rouge -> Mont Écarlate"})
                if "mana" in lower_curr and "magie" not in lower_curr:
                    issues.append({'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr, 'reason': "Mana -> Magie"})
                if "endurance" in lower_curr and "vigueur" not in lower_curr:
                    issues.append({'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr, 'reason': "Endurance -> Vigueur"})
        except Exception as e:
            print(f"Error reading {fp}: {e}")

print(f"\nAudit complete. Total issues identified in Sub-phase 2A: {len(issues)}")
# Group issues by mod and print
by_mod = {}
for iss in issues:
    m = iss['mod']
    by_mod.setdefault(m, []).append(iss)

for m, isss in by_mod.items():
    print(f"\n=== {m} ({len(isss)} issues) ===")
    for iss in isss[:20]:
        print(f"  [{iss['file']}] {iss['fid']} ({iss['type']})")
        print(f"    orig: {iss['orig']}")
        print(f"    curr: {iss['curr']}")
        if 'ref' in iss:
            print(f"    ref:  {iss['ref']}")
        print(f"    issue: {iss['reason']}")
    if len(isss) > 20:
        print(f"    ... and {len(isss) - 20} more issues")
