import json
import datetime
import re
from pathlib import Path

db = Path("data/user/database/french")
index_path = db / "index.json"
index_data = json.load(open(index_path, encoding="utf-8"))

oct_2026 = datetime.datetime(2026, 10, 1, 0, 0, 0).timestamp()

verif_content = open("TRADUCTIONS_VERIFIEES.md", encoding="utf-8").read()
# Extract all backtick items, filenames, and mod titles from TRADUCTIONS_VERIFIEES.md
verified_names_lower = set()
for line in verif_content.splitlines():
    if line.strip().startswith("|") and not line.strip().startswith("| Mod") and not line.strip().startswith("| :---"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if parts:
            # Mod title
            title = re.sub(r"\*\*|[\[\]]", "", parts[0]).strip().lower()
            verified_names_lower.add(title)
            # Files mentioned
            if len(parts) > 1:
                for fn in re.findall(r"[\w\s\-\.\(\)\'\’\+_]+\.(?:esp|esm|esl|txt)(?:\.json)?", parts[1], re.IGNORECASE):
                    clean_fn = fn.strip().lower()
                    if not clean_fn.endswith(".json"):
                        clean_fn += ".json"
                    verified_names_lower.add(clean_fn)

# Also any general backtick file names in the document
for fn in re.findall(r"`([^`]+)`", verif_content):
    clean = fn.strip().lower()
    if any(clean.endswith(ext) for ext in [".json", ".esp", ".esm", ".esl", ".txt"]):
        if not clean.endswith(".json") and not clean.endswith(".txt"):
            clean += ".json"
        verified_names_lower.add(clean)

print(f"Extracted {len(verified_names_lower)} verified identifiers from TRADUCTIONS_VERIFIEES.md")

candidates = []
for item in index_data:
    ts = item.get("timestamp", 0)
    src = item.get("source")
    # A local translation has no external provider mod_id and source is None/Local
    is_local = (src is None or src == "Local") and not (item.get("mod_id") and src in ["NexusMods", "Confrérie des Traducteurs"])
    if is_local and ts < oct_2026:
        name = item["name"]
        item_folder = db / name
        dt = datetime.datetime.fromtimestamp(ts)
        
        # Check files inside
        json_files = list(item_folder.glob("*.json")) if item_folder.is_dir() else []
        file_names = [f.name for f in json_files]
        
        # Check verification status
        is_verified = False
        matching_verif = []
        for fn in file_names:
            fn_lower = fn.lower()
            if fn_lower in verified_names_lower:
                is_verified = True
                matching_verif.append(fn)
        
        name_lower = name.lower()
        for vn in verified_names_lower:
            if vn in name_lower or name_lower in vn:
                if len(vn) > 4: # avoid tiny matches
                    is_verified = True
                    matching_verif.append(vn)
        
        candidates.append({
            "name": name,
            "version": item.get("version", ""),
            "timestamp": ts,
            "date_str": dt.strftime("%Y-%m-%d"),
            "source": src or "Local",
            "files": file_names,
            "is_verified": is_verified,
            "matching_verif": list(set(matching_verif)),
            "folder_exists": item_folder.is_dir()
        })

print(f"Total local entries before Oct 2026: {len(candidates)}")
verified = [c for c in candidates if c["is_verified"]]
unverified = [c for c in candidates if not c["is_verified"]]
print(f"Verified: {len(verified)}")
print(f"Unverified: {len(unverified)}")

# Let's inspect the verified ones to see if matching logic is accurate
print("\n--- Verified Sample ---")
for c in verified:
    print(f"[{c['date_str']}] {c['name']} -> Matched: {c['matching_verif']}")
