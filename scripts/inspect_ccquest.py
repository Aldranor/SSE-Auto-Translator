import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

p = 'data/user/database/french/CCQuest - Experience Patch.esp - French/ccquest - experience patch.esp.json'
data = json.load(open(p, encoding='utf-8'))

print(f"CCQuest entries: {len(data)}")
english_words = [r'\bthe\b', r'\band\b', r'\bwith\b', r'\bfrom\b', r'\byou\b', r'\bhave\b', r'\bkill\b', r'\bfind\b', r'\bspeak\b']
eng_re = re.compile('|'.join(english_words), re.IGNORECASE)

real_issues = []
for item in data:
    orig = item.get('original') or ''
    curr = item.get('string') or ''
    fid = item.get('form_id') or ''
    typ = item.get('type') or ''
    # Check untranslated English
    if curr.strip() == orig.strip() and eng_re.search(orig):
        real_issues.append((fid, typ, orig, curr, "100% English untranslated"))
    elif eng_re.search(curr) and len(curr.split()) > 3:
        # Check if mostly English
        words = curr.split()
        eng_count = sum(1 for w in words if eng_re.search(w))
        if eng_count >= 2:
            real_issues.append((fid, typ, orig, curr, "English words in translation"))
    
    # Check broken tags
    orig_tags = re.findall(r'<[^>]+>', orig)
    curr_tags = re.findall(r'<[^>]+>', curr)
    missing = [t for t in orig_tags if t not in curr]
    if missing:
        real_issues.append((fid, typ, orig, curr, f"Missing tags: {missing}"))

print(f"Real issues in CCQuest: {len(real_issues)}")
for r in real_issues[:20]:
    print(r)
