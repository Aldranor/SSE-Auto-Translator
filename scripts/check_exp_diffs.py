import json
from pathlib import Path
from sse_plugin_interface.plugin import SSEPlugin

esp_path = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Nolvus Awakening Experience Integration\Nolvus Awakening Experience Integration.esp")
p = SSEPlugin.from_file(esp_path)
esp_strings = p.extract_strings()

d1 = json.load(open("data/user/database/french/Nolvus Awakening Experience Integration - French/Nolvus Awakening Experience Integration.esp.json", encoding="utf-8"))
d2 = json.load(open("data/user/database/french/Nolvus Awakening Experience Integration.esp - French/nolvus awakening experience integration.esp.json", encoding="utf-8"))

map_esp = {}
# PluginString: form_id, type, string, editor_id, index
for s in esp_strings:
    k = (s.form_id, s.type, s.index)
    map_esp[k] = s

map_d1 = {(e["form_id"], e["type"], e.get("index")): e for e in d1}
map_d2 = {(e["form_id"], e["type"], e.get("index")): e for e in d2}

in_esp_not_db = set(map_esp.keys()) - set(map_d1.keys())
in_db_not_esp = set(map_d1.keys()) - set(map_esp.keys())

print(f"In ESP not in DB: {len(in_esp_not_db)}")
print(f"In DB not in ESP: {len(in_db_not_esp)}")

for k in list(in_esp_not_db)[:15]:
    s = map_esp[k]
    print(f"  ESP: {k} -> {repr(s.string)}")
