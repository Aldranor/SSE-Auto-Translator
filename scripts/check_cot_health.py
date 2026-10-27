import json
import re

path = r'data/user/database/french/Citizens of Tamriel/citizenscomplete.esp.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

mojibake_re = re.compile(r'(Ã©|Ã¨|Ã|â€™|â€œ|â€”|Â)')
illegal_tags = re.compile(r'<\d+>')
unclosed_tags = []
mojibake_found = []
illegal_tags_found = []

for i, e in enumerate(data):
    s = e.get('string', '')
    if mojibake_re.search(s):
        mojibake_found.append((i, s[:60]))
    if illegal_tags.search(s):
        illegal_tags_found.append((i, s[:60]))
    if '<font' in s.lower() and '</font>' not in s.lower():
        unclosed_tags.append((i, s[:60]))

print('Mojibake count:', len(mojibake_found))
print('Illegal tags count:', len(illegal_tags_found))
print('Unclosed tags count:', len(unclosed_tags))
