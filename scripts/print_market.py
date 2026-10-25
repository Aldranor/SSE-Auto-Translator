import json

with open('data/user/database/french/Marché extérieur de Blancherive/Kojaks Whiterun Market.esp.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for s in d:
    print(f"{s.get('form_id')}: {s.get('original')} ==> {s.get('translation')}")
