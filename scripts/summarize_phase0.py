import json

data = json.load(open("phase0_global_scan_results.json", encoding="utf-8"))
results = [r for r in data["results"] if r["is_unverified_local_mod"]]

results.sort(key=lambda r: sum(len(v) for v in r["findings"].values()), reverse=True)
print(f"Total unverified local files with anomalies: {len(results)}")
for r in results[:20]:
    total = sum(len(v) for v in r["findings"].values())
    details = ", ".join([f"{k}: {len(v)}" for k, v in r["findings"].items() if len(v) > 0])
    print(f"- {r['mod']} / {r['file']} : {total} anomalies ({details})")
