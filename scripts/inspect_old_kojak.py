import json

path = r"E:\Code\Projects\SSE-Auto-Translator\src\data\user\database\french\Whiterun Outskirts Market for SSE - French\kojaks whiterun market.esp.ats"
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    d = json.load(f)

for s in d:
    print(f"{s.get('original')}  ===>  {s.get('translation')}")
