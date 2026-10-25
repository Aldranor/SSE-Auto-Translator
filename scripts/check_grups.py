import struct
from collections import Counter

def get_record_types(esp_path):
    types = Counter()
    with open(esp_path, 'rb') as f:
        # Read header
        f.seek(0)
        sig = f.read(4)
        size = struct.unpack('<I', f.read(4))[0]
        f.seek(24 + size) # after TES4
        
        while True:
            chunk = f.read(4)
            if not chunk or len(chunk) < 4:
                break
            if chunk == b'GRUP':
                grup_size = struct.unpack('<I', f.read(4))[0]
                label = f.read(4)
                f.read(12) # remaining grup header (group type, stamp, etc)
                # label is usually 4-char record type for top-level group
                types[label.decode('ascii', errors='ignore')] = grup_size
                f.seek(f.tell() + grup_size - 24)
            else:
                break
    return types

print("Confrerie GRUPs:")
for k, v in sorted(get_record_types('data/cache/isc_extracted/00 - Main Files/Immersive Sounds - Compendium.esp').items()):
    print(f"  {k}: size {v}")

print("\nNolvus GRUPs:")
for k, v in sorted(get_record_types(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Immersive Sounds - Compendium\Immersive Sounds - Compendium.esp").items()):
    print(f"  {k}: size {v}")
