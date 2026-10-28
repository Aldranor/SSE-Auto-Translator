import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

phase3_files = [
    # 1. Remiel
    ('Remiel Base', 'data/user/database/french/Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)/hlioremi.esp.json'),
    ('Remiel LOTD', 'data/user/database/french/Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)/hliiremilotd.esp.json'),
    ('Remiel Beyond Reach', 'data/user/database/french/Remiel - Dwemer Specialist vostFR-63836-1-7-4-1726222506 (2)/hlizremiarnima.esp.json'),
    # 2. Vigilant
    ('Vigilant ESM', 'data/user/database/french/vigile_1.7.3_sse/vigilant.esm.json'),
    ('Vigilant Voiced', 'data/user/database/french/vigile_1.7.3_sse/vigilant voiced.esp.json'),
    ('Vigilant Creatures', 'data/user/database/french/vigile_1.7.3_sse/vigilant - my patches by xtudo - giant creatures fix.esp.json'),
    # 3. Fanatical Enemies
    ('Fanatical Enemies', 'data/user/database/french/Fanatical Enemies.esp - French/fanatical enemies.esp.json'),
    # 4. Akaviri Follower
    ('Akaviri Follower', 'data/user/database/french/AkaviriFollower.esp - French/akavirifollower.esp.json')
]

print(f"Scanning Phase 3 files ({len(phase3_files)} files)...")

total_records = 0
status_dist = {}
anomalies = []

en_words = [
    'the', 'and', 'with', 'from', 'what', 'where', 'when', 'why', 'who', 'how',
    'you', 'your', 'have', 'been', 'will', 'would', 'could', 'should',
    'sword', 'shield', 'helmet', 'boots', 'armor', 'dagger', 'bow',
    'damage', 'health', 'magicka', 'stamina', 'seconds', 'points'
]
en_pattern = re.compile(r'\b(' + '|'.join(en_words) + r')\b', re.IGNORECASE)

for label, fpath in phase3_files:
    fname = os.path.basename(fpath)
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        continue
    with open(fpath, 'r', encoding='utf-8') as jf:
        data = json.load(jf)
    
    total_records += len(data)
    print(f"[{label}] {fname} : {len(data)} entries")
    
    for item in data:
        st = item.get('status')
        status_dist[st] = status_dist.get(st, 0) + 1
        
        fid = item.get('form_id')
        typ = item.get('type')
        idx = item.get('index')
        orig = str(item.get('original') or '')
        curr = item.get('string')
        
        # 1. Null or empty string
        if curr is None or not str(curr).strip():
            if st != 'NoTranslationRequired':
                anomalies.append((label, fname, fid, typ, idx, orig, curr, "EMPTY_OR_NULL"))
            continue
            
        curr_str = str(curr)
        
        # 2. Status is TranslationRequired
        if st == 'TranslationRequired':
            anomalies.append((label, fname, fid, typ, idx, orig, curr, "STATUS_REQUIRED"))
            
        # 3. Mojibake
        if any(c in curr_str for c in ['Ã©', 'Ã¨', 'Ã ', 'Ã¢', 'Ã¹', 'Ã®', 'Ã«', 'Ã¯']):
            anomalies.append((label, fname, fid, typ, idx, orig, curr, "MOJIBAKE"))
            
        # 4. Untranslated English in dialog / text (where orig == curr and long)
        if orig == curr_str and len(orig) > 15 and st != 'NoTranslationRequired':
            matches = en_pattern.findall(orig)
            if len(matches) >= 3:
                anomalies.append((label, fname, fid, typ, idx, orig, curr, f"UNTRANSLATED_ENGLISH (matches: {matches[:4]})"))
                
        # 5. Lore false friends
        if 'montagne rouge' in curr_str.lower():
            anomalies.append((label, fname, fid, typ, idx, orig, curr, "LORE: Montagne rouge -> Mont Écarlate"))
        if 'falkreath' in orig.lower() and 'faillaise' in curr_str.lower():
            anomalies.append((label, fname, fid, typ, idx, orig, curr, "LORE: Falkreath -> Épervine (et non Faillaise)"))
        if 'clair-osbcur' in curr_str.lower():
            anomalies.append((label, fname, fid, typ, idx, orig, curr, "TYPO: clair-osbcur -> Clair-Obscur"))

print(f"\nTotal records scanned across Phase 3: {total_records}")
print(f"Status distribution: {status_dist}")
print(f"Total anomalies flagged: {len(anomalies)}")

by_issue = {}
for a in anomalies:
    by_issue.setdefault(a[7], []).append(a)

for issue, items in by_issue.items():
    print(f"\n--- {issue} ({len(items)} items) ---")
    for it in items[:10]:
        print(f"[{it[0]}] {it[2]} | {it[3]} | idx={it[4]}")
        print(f"   Orig: {repr(it[5][:80])}")
        print(f"   Curr: {repr(it[6][:80]) if it[6] else None}")

with open('phase3_anomalies.json', 'w', encoding='utf-8') as f:
    json.dump(anomalies, f, ensure_ascii=False, indent=2)
print("\nSaved phase3_anomalies.json.")
