import json
import re
import shutil
from pathlib import Path

target_file = Path("data/user/database/french/LOTD - L'Héritage de l'Enfant de dragon/LegacyoftheDragonborn.esm.json")
backup_file = target_file.with_suffix(".json.bak")

print(f"Creating backup: {backup_file}")
shutil.copy2(target_file, backup_file)

def main():
    with open(target_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Total records in LOTD: {len(data)}")

    fixed_bogus_numeric_count = 0
    fixed_records_count = 0
    other_fixes = []

    for s in data:
        orig = s.get("original") or ""
        trans = s.get("string") or ""
        if not trans:
            continue
        
        modified = False
        
        # 1. Fix bogus numeric tags: <10> -> 10 (when <10> was NOT in orig)
        def clean_numeric_tag(match):
            nonlocal fixed_bogus_numeric_count, modified
            full_tag = match.group(0) # e.g. <10>
            num = match.group(1)      # e.g. 10
            # If orig had the exact tag <10>, keep it. Otherwise, remove brackets.
            if full_tag in orig:
                return full_tag
            fixed_bogus_numeric_count += 1
            modified = True
            return num

        new_trans = re.sub(r"<([0-9]+)>", clean_numeric_tag, trans)
        
        # 2. Fix broken <pagebreak] -> [pagebreak]
        if "<pagebreak]" in new_trans:
            new_trans = new_trans.replace("<pagebreak]", "[pagebreak]")
            other_fixes.append(f"Fixed <pagebreak] in {s.get('form_id')}")
            modified = True
            
        # 3. Fix translated font name $Bordecielbooks -> $skyrimbooks
        if "$Bordecielbooks" in new_trans:
            new_trans = new_trans.replace("$Bordecielbooks", "$skyrimbooks")
            other_fixes.append(f"Fixed $Bordecielbooks in {s.get('form_id')}")
            modified = True
            
        # 4. Fix DBM_NecrodaggerABIL: restore <mag>%
        if s.get("editor_id") == "DBM_NecrodaggerABIL" and "<mag>" in orig and "<mag>" not in new_trans:
            new_trans = re.sub(r"augmente de (?:30 points|<30> points)", "augmente de <mag> %", new_trans)
            other_fixes.append(f"Restored <mag> % in {s.get('form_id')} ({s.get('editor_id')})")
            modified = True
            
        if modified:
            s["string"] = new_trans
            fixed_records_count += 1

    print(f"Total bogus numeric tags stripped: {fixed_bogus_numeric_count}")
    print(f"Total records modified: {fixed_records_count}")
    for fix in other_fixes:
        print(f"  * {fix}")

    # Write back
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved changes to {target_file}")

    # Verify after write
    with open(target_file, "r", encoding="utf-8") as f:
        verify_data = json.load(f)

    print(f"Verification: {len(verify_data)} records successfully loaded back.")

if __name__ == "__main__":
    main()
