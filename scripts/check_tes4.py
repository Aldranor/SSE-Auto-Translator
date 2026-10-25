import struct

def read_tes4_header(esp_path):
    with open(esp_path, 'rb') as f:
        sig = f.read(4)
        size, flags, formid, version_ctrl, form_version, version_ctrl2 = struct.unpack('<IIIIHH', f.read(20))
        data = f.read(size)
        
        # Parse subrecords of TES4
        offset = 0
        subrecords = {}
        masters = []
        while offset < len(data):
            sub_sig = data[offset:offset+4].decode('ascii', errors='ignore')
            sub_size = struct.unpack('<H', data[offset+4:offset+6])[0]
            sub_data = data[offset+6:offset+6+sub_size]
            offset += 6 + sub_size
            if sub_sig == 'MAST':
                masters.append(sub_data.decode('utf-8', errors='ignore').rstrip('\x00'))
            elif sub_sig == 'HEDR':
                version = struct.unpack('<f', sub_data[:4])[0]
                num_records = struct.unpack('<I', sub_data[4:8])[0]
                subrecords['version'] = version
                subrecords['num_records'] = num_records
            elif sub_sig == 'CNAM':
                subrecords['author'] = sub_data.decode('utf-8', errors='ignore').rstrip('\x00')
            elif sub_sig == 'SNAM':
                subrecords['description'] = sub_data.decode('utf-8', errors='ignore').rstrip('\x00')
        subrecords['masters'] = masters
        subrecords['form_version'] = form_version
        return subrecords

print("Confrerie TES4:", read_tes4_header('data/cache/isc_extracted/00 - Main Files/Immersive Sounds - Compendium.esp'))
print("Nolvus TES4:", read_tes4_header(r"D:\Nolvus\Instances\Nolvus Awakening\MODS\mods\Immersive Sounds - Compendium\Immersive Sounds - Compendium.esp"))
