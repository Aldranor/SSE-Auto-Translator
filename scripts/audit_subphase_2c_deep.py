import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

subphase_2c_mods = [
    'Lux - Patch Hub - French',
    'Lux Orbis - Patch Hub - French',
    "JK's Interiors Patch Collection - French",
    'JKs Guild HQ Interiors Patch Collection - French',
    'JKs Guild HQ Interiors Patch Collection',
    'Water for ENB [4K] - French',
    'Water for ENB [4K]',
    'Embers XD - French'
]

base_dir = 'data/user/database/french'

# Build a solid canonical reference dictionary for cells and world records
# Using USSEP, vanilla Skyrim.esm and verified mods
ref_map = {}
ussep_path = 'data/user/database/french/USSEP - Traduction Francaise'
if os.path.exists(ussep_path):
    for fn in os.listdir(ussep_path):
        if fn.endswith('.json'):
            d = json.load(open(os.path.join(ussep_path, fn), encoding='utf-8'))
            for item in d:
                fid = item.get('form_id')
                typ = item.get('type')
                s = item.get('string')
                if fid and typ and s and s.strip():
                    ref_map[(fid, typ)] = s

print(f"Loaded {len(ref_map)} reference entries from USSEP.")

# Also add reference entries from any other official mods in DB
for root, dirs, files in os.walk(base_dir):
    # Skip the patch hubs themselves
    if any(m.lower() in root.lower() for m in subphase_2c_mods):
        continue
    for f in files:
        if f.endswith('.json') and f != 'index.json':
            try:
                d = json.load(open(os.path.join(root, f), encoding='utf-8'))
                if isinstance(d, list):
                    for item in d:
                        fid = item.get('form_id')
                        typ = item.get('type')
                        orig = item.get('original')
                        s = item.get('string')
                        if fid and typ and s and s.strip() and s != orig:
                            if (fid, typ) not in ref_map:
                                ref_map[(fid, typ)] = s
            except:
                pass

print(f"Total reference dictionary size: {len(ref_map)} entries.")

# Scan all 2C mods
issues = []
total_records = 0

for mod in subphase_2c_mods:
    mod_dir = os.path.join(base_dir, mod)
    if not os.path.exists(mod_dir):
        print(f"Mod dir not found: {mod}")
        continue
    files = [f for f in os.listdir(mod_dir) if f.endswith('.json')]
    for fn in files:
        fp = os.path.join(mod_dir, fn)
        try:
            data = json.load(open(fp, encoding='utf-8'))
            total_records += len(data)
            for item in data:
                fid = item.get('form_id', '')
                typ = item.get('type', '')
                orig = item.get('original') or ''
                curr = item.get('string') or ''
                
                # Check 1: Empty string where original exists
                if orig.strip() and not curr.strip():
                    issues.append({
                        'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr,
                        'reason': "Empty translation string"
                    })
                
                # Check 2: English string left identical where official French differs
                ref_val = ref_map.get((fid, typ))
                if ref_val and curr != ref_val:
                    if ref_val.strip().lower() != curr.strip().lower():
                        # Don't flag if curr is valid French variant or both identical
                        issues.append({
                            'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr,
                            'ref': ref_val,
                            'reason': f"Reference mismatch with official: '{curr}' vs '{ref_val}'"
                        })
                elif curr == orig and len(orig.split()) > 1:
                    # Potential English string
                    issues.append({
                        'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr,
                        'reason': f"Untranslated English string: '{curr}'"
                    })
                
                # Check 3: Missing tags
                orig_tags = re.findall(r'<[^>]+>', orig)
                curr_tags = re.findall(r'<[^>]+>', curr)
                missing = [t for t in orig_tags if t not in curr]
                if missing:
                    issues.append({
                        'mod': mod, 'file': fn, 'fid': fid, 'type': typ, 'orig': orig, 'curr': curr,
                        'reason': f"Missing tags: {missing}"
                    })
        except Exception as e:
            print(f"Error reading {fp}: {e}")

print(f"\nTotal records scanned in Sub-phase 2C: {total_records}")
print(f"Total issues flagged: {len(issues)}")

# Group issues by mod
by_mod = {}
for iss in issues:
    by_mod.setdefault(iss['mod'], []).append(iss)

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
