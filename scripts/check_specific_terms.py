import json

path = "data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json"
data = json.load(open(path, encoding="utf-8"))

print(f"Total entries: {len(data)}")

# Let's inspect any entry with 'Dovahkiin', 'suicidaire', 'impie', 'obfuscation'
for idx, e in enumerate(data):
    s = e.get("string") or ""
    orig = e.get("original") or ""
    if "obfuscation" in s.lower():
        print(f"Entry {idx}: {orig} -> {s}")
    if "second knight" in orig.lower():
        print(f"Entry {idx}: {orig} -> {s}")
    if "first knight" in orig.lower():
        print(f"Entry {idx}: {orig} -> {s}")
