"""Independent disk verification script for Phase 4."""
import json
import os
import re

DB_DIR = r"e:\Code\SSE Translator updated\data\user\database\french"

breton_re = re.compile(r"\b[Bb]réton(?:ne)?s?\b")

remaining_breton = 0
total_files_checked = 0
total_entries_checked = 0
json_errors = 0

for root, _, files in os.walk(DB_DIR):
    for f in sorted(files):
        if not f.endswith(".json") or f == "index.json":
            continue
        p = os.path.join(root, f)
        total_files_checked += 1
        try:
            with open(p, "r", encoding="utf-8") as fp:
                data = json.load(fp)
        except Exception as e:
            json_errors += 1
            print(f"JSON Error in {p}: {e}")
            continue

        for idx, row in enumerate(data):
            total_entries_checked += 1
            s = row.get("string", "")
            if s and breton_re.search(s):
                remaining_breton += 1
                print(f"Remaining Breton in {f} idx {idx}: {s[:60]}")

print("=" * 60)
print("INDEPENDENT VERIFICATION PHASE 4 REPORT")
print(f"Total files checked:       {total_files_checked}")
print(f"Total entries checked:     {total_entries_checked}")
print(f"JSON syntax errors:        {json_errors}")
print(f"Remaining 'Bréton' errors: {remaining_breton}")
print("=" * 60)

if remaining_breton == 0 and json_errors == 0:
    print(">>> VERIFICATION PASSED: 100% CLEAN AND COMPLIANT <<<")
else:
    print(">>> VERIFICATION FAILED <<<")
