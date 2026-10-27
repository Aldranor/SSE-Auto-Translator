import json
import datetime
import re
from pathlib import Path

db = Path("data/user/database/french")
index_path = db / "index.json"
index_data = json.load(open(index_path, encoding="utf-8"))

oct_2026 = datetime.datetime(2026, 10, 1, 0, 0, 0).timestamp()

verif_content = open("TRADUCTIONS_VERIFIEES.md", encoding="utf-8").read()

# Exact file names mentioned in TRADUCTIONS_VERIFIEES.md
exact_verified_files = set()
for fn in re.findall(r"`([^`]+)`", verif_content):
    clean = fn.strip().lower()
    if any(clean.endswith(ext) for ext in [".json", ".esp", ".esm", ".esl", ".txt"]):
        if not clean.endswith(".json") and not clean.endswith(".txt"):
            clean += ".json"
        exact_verified_files.add(clean)

# Also find in tables
for fn in re.findall(r"[\w\s\-\.\(\)\'\’\+_]+\.(?:esp|esm|esl|txt)(?:\.json)?", verif_content, re.IGNORECASE):
    clean_fn = fn.strip().lower()
    if not clean_fn.endswith(".json"):
        clean_fn += ".json"
    exact_verified_files.add(clean_fn)

print(f"Total exact verified files in doc: {len(exact_verified_files)}")

local_entries = []
for item in index_data:
    ts = item.get("timestamp", 0)
    src = item.get("source")
    is_local = (src is None or src == "Local") and not (item.get("mod_id") and src in ["NexusMods", "Confrérie des Traducteurs"])
    if is_local and ts < oct_2026:
        local_entries.append(item)

print(f"Local entries before Oct 2026: {len(local_entries)}")

unverified_list = []
partially_verified_list = []
fully_verified_list = []

for item in local_entries:
    name = item["name"]
    folder = db / name
    ts = item.get("timestamp", 0)
    dt = datetime.datetime.fromtimestamp(ts)
    
    json_files = list(folder.glob("*.json")) if folder.is_dir() else []
    
    file_stats = []
    total_strings = 0
    empty_strings = 0
    
    verified_files = []
    unverified_files = []
    
    for jf in json_files:
        fn = jf.name
        fn_lower = fn.lower()
        is_f_verif = fn_lower in exact_verified_files
        
        try:
            data = json.load(open(jf, encoding="utf-8"))
            n_str = len(data) if isinstance(data, list) else 0
            n_empty = sum(1 for s in data if not s.get("string") or not str(s.get("string")).strip()) if isinstance(data, list) else 0
        except Exception:
            n_str = 0
            n_empty = 0
            
        total_strings += n_str
        empty_strings += n_empty
        
        if is_f_verif:
            verified_files.append(fn)
        else:
            unverified_files.append(fn)
            
        file_stats.append({
            "filename": fn,
            "strings": n_str,
            "empty": n_empty,
            "verified": is_f_verif
        })
    
    entry_info = {
        "name": name,
        "date": dt.strftime("%Y-%m-%d"),
        "timestamp": ts,
        "total_files": len(json_files),
        "total_strings": total_strings,
        "empty_strings": empty_strings,
        "file_stats": file_stats,
        "verified_files": verified_files,
        "unverified_files": unverified_files
    }
    
    if len(verified_files) == len(json_files) and len(json_files) > 0:
        fully_verified_list.append(entry_info)
    elif len(verified_files) > 0:
        partially_verified_list.append(entry_info)
    else:
        unverified_list.append(entry_info)

print(f"Fully verified: {len(fully_verified_list)}")
print(f"Partially verified: {len(partially_verified_list)}")
print(f"Completely unverified: {len(unverified_list)}")

# Save full results to a JSON file for quick querying and reporting
with open("local_unverified_analysis.json", "w", encoding="utf-8") as out:
    json.dump({
        "fully_verified": fully_verified_list,
        "partially_verified": partially_verified_list,
        "unverified": unverified_list
    }, out, indent=2, ensure_ascii=False)

print("Saved to local_unverified_analysis.json")
