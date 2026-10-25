import sys
from pathlib import Path
sys.path.insert(0, 'src')
sys.path.insert(0, 'core-lib/src')

from core.file_types.plugin.file import PluginFile

confrerie_esp_path = Path('data/cache/isc_extracted/00 - Main Files/Immersive Sounds - Compendium.esp')
nolvus_esp_path = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Immersive Sounds - Compendium\Immersive Sounds - Compendium.esp")

pf_conf = PluginFile(name=confrerie_esp_path.name, path=confrerie_esp_path, full_path=confrerie_esp_path)
pf_nolv = PluginFile(name=nolvus_esp_path.name, path=nolvus_esp_path, full_path=nolvus_esp_path)

conf_strings = pf_conf.get_strings()
nolv_strings = pf_nolv.get_strings()

print(f"Confrerie strings count: {len(conf_strings)}")
print(f"Nolvus strings count: {len(nolv_strings)}")

print("\n--- Confrerie first 20 strings ---")
for s in conf_strings[:20]:
    print(f"[{s.form_id}] ({s.editor_id}) [{s.type}]: {s.original!r}")

print("\n--- Nolvus first 20 strings ---")
for s in nolv_strings[:20]:
    print(f"[{s.form_id}] ({s.editor_id}) [{s.type}]: {s.original!r}")
