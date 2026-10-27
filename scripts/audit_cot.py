import json
import re

path = r'data/user/database/french/Citizens of Tamriel/citizenscomplete.esp.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries: {len(data)}")

# 1. Identical entries
identical = []
for i, e in enumerate(data):
    if e.get('original') == e.get('string'):
        identical.append((i, e.get('type'), e.get('editor_id'), e.get('original'), e.get('status')))

print(f"Total identical: {len(identical)}")
with open('cot_identical.txt', 'w', encoding='utf-8') as out:
    for idx, t, edid, orig, st in identical:
        out.write(f"[{idx}] Status: {st} | Type: {t} | EDID: {edid} | Text: {repr(orig)}\n")

# 2. English words in string
english_pattern = re.compile(r'\b(the|and|you|that|with|from|this|have|your|what|they|will|about|would|there|their)\b', re.IGNORECASE)
suspicious = []
for i, e in enumerate(data):
    if e.get('status') == 'TranslationComplete' and e.get('original') != e.get('string'):
        s = e.get('string', '')
        matches = english_pattern.findall(s)
        if len(matches) >= 2:
            suspicious.append((i, e.get('type'), e.get('original'), s, matches))

print(f"Suspicious English in string: {len(suspicious)}")
with open('cot_suspicious_english.txt', 'w', encoding='utf-8') as out:
    for idx, t, orig, trans, m in suspicious:
        out.write(f"[{idx}] Type: {t} | Matches: {m}\nORIG: {orig}\nTRAN: {trans}\n\n")

print("Done writing audit files.")
