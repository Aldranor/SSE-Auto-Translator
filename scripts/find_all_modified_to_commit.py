import os
import glob
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Check git status for tracked modified files
res = subprocess.run(['git', 'diff', '--name-only'], capture_output=True, text=True)
tracked_modified = res.stdout.strip().splitlines()

print("Tracked modified files:")
for f in tracked_modified:
    print("  ", f)

# Find all files in data/user/database/french modified in the last 24 hours
import time
now = time.time()
recent_files = []
for root, dirs, files in os.walk('data/user/database/french'):
    for f in files:
        if f.endswith('.json'):
            fp = os.path.join(root, f)
            mtime = os.path.getmtime(fp)
            if now - mtime < 4 * 3600: # last 4 hours
                recent_files.append(fp.replace('\\', '/'))

print(f"\nRecently modified files in data/user/database/french ({len(recent_files)}):")
for f in recent_files:
    print("  ", f)
