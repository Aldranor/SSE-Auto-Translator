import sys
from pathlib import Path
sys.path.insert(0, 'src')
sys.path.insert(0, 'core-lib/src')

from core.file_types.plugin.file import PluginFile

nolvus_esp_path = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Immersive Sounds - Compendium\Immersive Sounds - Compendium.esp")
pf_nolv = PluginFile(name=nolvus_esp_path.name, path=nolvus_esp_path, full_path=nolvus_esp_path)
strings = pf_nolv.get_strings()

print(f"Total strings: {len(strings)}")
non_vanilla = []
vanilla = []

for s in strings:
    # Check form_id master
    master = s.form_id.split('|')[-1] if '|' in s.form_id else ''
    if master.lower() in ('skyrim.esm', 'update.esm', 'dawnguard.esm', 'dragonborn.esm', 'hearthfires.esm'):
        vanilla.append(s)
    else:
        non_vanilla.append(s)

print(f"Vanilla master strings: {len(vanilla)}")
print(f"ISC new form strings: {len(non_vanilla)}")
for s in non_vanilla:
    print("  ISC record:", s.form_id, s.editor_id, s.type, repr(s.original))
