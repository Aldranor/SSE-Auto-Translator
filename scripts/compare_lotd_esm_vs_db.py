import sys
from pathlib import Path

# Add workspace to path
sys.path.insert(0, str(Path("src").resolve()))

import json
from core.file_types.plugin.file import PluginFile

esm_path = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Legacy of the Dragonborn\LegacyoftheDragonborn.esm")
json_path = Path(r"data\user\database\french\LOTD - L'Héritage de l'Enfant de dragon\LegacyoftheDragonborn.esm.json")

print("Loading ESM strings...")
pf = PluginFile(name=esm_path.name, full_path=esm_path)
esm_strings = pf.get_strings()
print(f"Extracted {len(esm_strings)} strings from ESM.")

print("Loading JSON database strings...")
with open(json_path, "r", encoding="utf-8") as f:
    json_data = json.load(f)
print(f"Loaded {len(json_data)} strings from JSON.")

# Compare FormIDs and originals
esm_dict = {}
for s in esm_strings:
    key = (s.form_id, s.type, s.index)
    esm_dict[key] = s

json_dict = {}
for s in json_data:
    key = (s.get("form_id"), s.get("type"), s.get("index"))
    json_dict[key] = s

in_esm_not_json = [k for k in esm_dict if k not in json_dict]
in_json_not_esm = [k for k in json_dict if k not in esm_dict]
orig_diff = []

for k in esm_dict:
    if k in json_dict:
        esm_orig = esm_dict[k].original or ""
        json_orig = json_dict[k].get("original") or ""
        if esm_orig != json_orig:
            orig_diff.append({
                "key": k,
                "esm_orig": esm_orig,
                "json_orig": json_orig,
                "json_trans": json_dict[k].get("string") or ""
            })

print(f"Keys in ESM but not in JSON: {len(in_esm_not_json)}")
print(f"Keys in JSON but not in ESM: {len(in_json_not_esm)}")
print(f"Original text differences for same key: {len(orig_diff)}")

if orig_diff:
    print("\nSample original text differences:")
    for d in orig_diff[:10]:
        print(f"Key: {d['key']}")
        print(f"  ESM original:  {d['esm_orig']}")
        print(f"  JSON original: {d['json_orig']}")
        print(f"  JSON string:   {d['json_trans']}")
        print()

with open("lotd_plugin_vs_db_diff.json", "w", encoding="utf-8") as out:
    json.dump({
        "in_esm_not_json_count": len(in_esm_not_json),
        "in_json_not_esm_count": len(in_json_not_esm),
        "orig_diff": orig_diff
    }, out, indent=2, ensure_ascii=False)
