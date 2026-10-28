"""Apply targeted place name fixes to database."""
import json
import glob

# 1. NPCModTowns
fpaths = glob.glob(r"e:\Code\SSE Translator updated\data\user\database\french\**\NPCModTowns.esp.json", recursive=True)
for p in fpaths:
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    # idx 78
    d[78]["string"] = d[78]["string"].replace("la Honningbrew Meadery", "l'hydromellerie d'Hydrhonning")
    # idx 280
    d[280]["string"] = d[280]["string"].replace("The Bannered Mare", "la Jument pavoisée")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("Fixed NPCModTowns")

# 2. This Is Jorrvaskr
jpaths = glob.glob(r"e:\Code\SSE Translator updated\data\user\database\french\**\This Is Jorrvaskr.esp.json", recursive=True)
for p in jpaths:
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    d[440]["string"] = d[440]["string"].replace("la tour Underforge", "la tour de la Basse-Forge")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("Fixed This Is Jorrvaskr")

# 3. DBM_CC_DivineCrusaderHOWPatch
cpaths = glob.glob(r"e:\Code\SSE Translator updated\data\user\database\french\**\DBM_CC_DivineCrusaderHOWPatch.esp.json", recursive=True)
for p in cpaths:
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    s = d[45]["string"]
    s = s.replace("au fort Sungard", "au fort Gardesoleil")
    s = s.replace("au fort Gardesol", "au fort Gardesoleil")
    d[45]["string"] = s
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print("Fixed DivineCrusader")
