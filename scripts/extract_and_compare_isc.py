import os
import py7zr
from pathlib import Path

# Extract Confrerie esp
archive_path = 'data/cache/isc_test.7z'
out_dir = Path('data/cache/isc_extracted')
out_dir.mkdir(exist_ok=True, parents=True)

with py7zr.SevenZipFile(archive_path, mode='r') as z:
    z.extract(targets=['00 - Main Files/Immersive Sounds - Compendium.esp'], path=out_dir)

confrerie_esp = out_dir / '00 - Main Files' / 'Immersive Sounds - Compendium.esp'
nolvus_esp = Path(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Immersive Sounds - Compendium\Immersive Sounds - Compendium.esp")

print(f"Confrerie ESP size: {confrerie_esp.stat().st_size} bytes")
print(f"Nolvus ESP size: {nolvus_esp.stat().st_size} bytes")
