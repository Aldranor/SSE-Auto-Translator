import os
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base = 'data/user/database/french'
dirs = os.listdir(base)

patterns = ['modpocalypse', 'true sons', 'fanatical', 'dibella', 'nithi', 'ai overhaul']

matched_dirs = []
for d in dirs:
    d_lower = d.lower()
    for p in patterns:
        if p in d_lower:
            matched_dirs.append(d)
            break

print(f"Matched {len(matched_dirs)} directories in {base}:")
total_files = 0
for d in sorted(matched_dirs):
    full_d = os.path.join(base, d)
    files = glob.glob(os.path.join(full_d, '*.json'))
    total_files += len(files)
    print(f"\n[{d}] -> {len(files)} JSON files:")
    for f in files:
        fname = os.path.basename(f)
        try:
            with open(f, 'r', encoding='utf-8') as jf:
                data = json.load(jf)
            count = len(data) if isinstance(data, list) else len(data.keys())
        except Exception as e:
            count = f"Error: {e}"
        print(f"   - {fname} ({count} entries)")

print(f"\nTotal files: {total_files}")
