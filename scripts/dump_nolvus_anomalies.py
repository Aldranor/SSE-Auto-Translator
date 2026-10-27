import json
from pathlib import Path

data = json.load(open("phase0_global_scan_results.json", encoding="utf-8"))
results = data["results"]

nolvus_anomalies = []
for r in results:
    if "nolvus awakening" in r["mod"].lower():
        total = sum(len(v) for v in r["findings"].values())
        if total > 0:
            nolvus_anomalies.append(r)

out_path = Path("nolvus_anomalies.txt")
with open(out_path, "w", encoding="utf-8") as out:
    out.write(f"Total Nolvus mods with anomalies: {len(nolvus_anomalies)}\n")
    for r in nolvus_anomalies:
        out.write(f"\n==========================================\n")
        out.write(f"MOD: {r['mod']} / {r['file']}\n")
        for cat, items in r["findings"].items():
            if items:
                out.write(f"--- {cat} ({len(items)}) ---\n")
                for it in items:
                    out.write(json.dumps(it, ensure_ascii=False, indent=2) + "\n")
print("Written to nolvus_anomalies.txt")

