import json
from pathlib import Path
from sse_plugin_interface.plugin import SSEPlugin

esp_path = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Nolvus Awakening Experience Integration\Nolvus Awakening Experience Integration.esp")
p = SSEPlugin.from_file(esp_path)
esp_strings = p.extract_strings()

f1_path = Path("data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json")
f2_path = Path("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json")

d1 = json.load(open(f1_path, encoding="utf-8"))
d2 = json.load(open(f2_path, encoding="utf-8"))

print(f"ESP strings count: {len(esp_strings)}")
print(f"d1 count: {len(d1)}")
print(f"d2 count: {len(d2)}")

# Let's see what d1 and d2 contain
print("\n--- First 10 in ESP ---")
for i, s in enumerate(esp_strings[:10]):
    print(f"{i}: [{s.type}] ({s.form_id}) idx={s.index}: {s.string[:50]}...")

print("\n--- First 10 in d1 ---")
for i, s in enumerate(d1[:10]):
    print(f"{i}: [{s.get('type')}] ({s.get('form_id')}) idx={s.get('index')}: ORIG={s.get('original')[:35]}... TRAD={s.get('string')[:35]}...")

print("\n--- First 10 in d2 ---")
for i, s in enumerate(d2[:10]):
    print(f"{i}: [{s.get('type')}] ({s.get('form_id')}) idx={s.get('index')}: ORIG={s.get('original')[:35]}... TRAD={s.get('string')[:35]}...")
