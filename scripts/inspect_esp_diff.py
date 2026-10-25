import sys
from pathlib import Path
sys.path.insert(0, 'src')
sys.path.insert(0, 'core-lib/src')

from core.file_source.file_source_factory import FileSourceFactory
from sse_plugin_interface.plugin import SSEPlugin

confrerie_esp_path = Path('data/cache/isc_extracted/00 - Main Files/Immersive Sounds - Compendium.esp')
nolvus_esp_path = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Immersive Sounds - Compendium\Immersive Sounds - Compendium.esp")

p_conf = SSEPlugin.from_stream(FileSourceFactory.for_file_path(confrerie_esp_path).get_file_stream(), confrerie_esp_path.name)
p_nolv = SSEPlugin.from_stream(FileSourceFactory.for_file_path(nolvus_esp_path).get_file_stream(), nolvus_esp_path.name)

# Let's inspect raw strings extracted by SSEPlugin
conf_raw = p_conf.extract_strings()
nolv_raw = p_nolv.extract_strings()

print("Conf raw strings count:", len(conf_raw))
print("Nolv raw strings count:", len(nolv_raw))

# What types of records are in Nolvus vs Confrerie?
from collections import Counter
conf_types = Counter(s.type for s in conf_raw)
nolv_types = Counter(s.type for s in nolv_raw)

print("Conf string types:", conf_types)
print("Nolv string types:", nolv_types)
