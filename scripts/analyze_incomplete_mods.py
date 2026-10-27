import json
import re
from pathlib import Path
from collections import defaultdict

db = Path("data/user/database/french")

def is_variable_or_technical(s):
    if not s:
        return True
    s = str(s).strip()
    if not s:
        return True
    # Variables like <...>, [...], %s, $Var, {0}
    if re.match(r"^<[^>]+>$", s) or re.match(r"^\[[^\]]+\]$", s) or re.match(r"^\$[a-zA-Z0-9_]+$", s):
        return True
    if re.match(r"^\{[0-9]+\}$", s) or re.match(r"^%[0-9]*[sdf]$", s):
        return True
    # Pure punctuation / symbols / numbers / brackets
    if re.match(r"^[0-9\s\-_.:,;!?/\\|<>=\[\]\(\)\*#%+\'\"]+$", s):
        return True
    # Internal identifiers like xx_yy or CamelCaseID without space or lowercase_with_underscore
    if re.match(r"^[a-zA-Z0-9]+_[a-zA-Z0-9_]+$", s):
        return True
    return False

def is_untranslatable_npc_name(item):
    if item.get("type") not in ("NPC_ FULL", "NPC_ SHRT"):
        return False
    orig = str(item.get("original") or "").strip()
    if not orig:
        return True
    # Check if original is identical to translated string already, or is a pure proper name
    trans = str(item.get("string") or "").strip()
    if trans == orig and trans != "":
        return True
    # Check if it has obvious English common words that usually get translated (e.g. Bandit, Guard, Citizen, Child, etc.)
    english_titles = [
        "guard", "bandit", "thug", "citizen", "child", "boy", "girl", "soldier", "warrior", "mage",
        "witch", "vampire", "skeleton", "ghost", "spirit", "cultist", "necromancer", "hunter",
        "farmer", "fisherman", "miner", "prisoner", "beggar", "priest", "patrol", "scout", "captain",
        "general", "commander", "elder", "apprentice", "adept", "master", "lord", "lady", "king",
        "queen", "assassin", "mercenary", "courier", "traveler", "pilgrim", "follower", "corpse",
        "dog", "wolf", "horse", "bear", "cat", "chicken", "cow", "goat", "spider", "mudcrab",
        "troll", "giant", "dragon", "hagraven", "draugr", "atronach", "dremora", "daedra", "phantom"
    ]
    orig_lower = orig.lower()
    for word in english_titles:
        if re.search(r"\b" + re.escape(word) + r"\b", orig_lower):
            return False # Likely needs translation (e.g. "Whiterun Guard", "Bandit Chief")
    
    # Also if contains " of ", " the ", " in ", " from "
    if re.search(r"\b(of|the|in|from|and|with)\b", orig_lower):
        return False
    
    # If it's 1-3 capitalized words like "Elenwen", "Kharjo", "M'aiq", "Astrid", "Ghorbash gro-Dushnikh", etc.
    # It's an NPC proper name
    return True

results = {
    "only_tech": [],
    "only_proper_names": [],
    "only_tech_and_names": [],
    "has_translatable": []
}

all_mods_data = defaultdict(list)

for mod_dir in sorted(db.iterdir()):
    if not mod_dir.is_dir():
        continue
    for f in mod_dir.glob("*.json"):
        try:
            with open(f, "r", encoding="utf-8") as fp:
                data = json.load(fp)
        except Exception:
            continue
        
        incomplete = [s for s in data if s.get("status") in ("TranslationIncomplete", "TranslationRequired")]
        if not incomplete:
            continue
        
        mod_key = mod_dir.name
        
        all_tech = True
        all_proper_names = True
        all_tech_or_names = True
        
        real_translatable = []
        
        for s in incomplete:
            orig = s.get("original", "").strip()
            t = s.get("type", "")
            
            tech = is_variable_or_technical(orig)
            proper_name = is_untranslatable_npc_name(s)
            
            if not tech:
                all_tech = False
            if not proper_name:
                all_proper_names = False
            if not (tech or proper_name):
                all_tech_or_names = False
                real_translatable.append(s)
        
        entry = {
            "mod": mod_dir.name,
            "file": f.name,
            "total_incomplete": len(incomplete),
            "samples": [s.get("original", "") for s in incomplete[:6]],
            "real_samples": [f"[{s.get('type')}] {s.get('original')}" for s in real_translatable[:6]]
        }
        
        if all_tech:
            results["only_tech"].append(entry)
        elif all_proper_names:
            results["only_proper_names"].append(entry)
        elif all_tech_or_names:
            results["only_tech_and_names"].append(entry)
        else:
            results["has_translatable"].append(entry)

print(f"Only technical / variables: {len(results['only_tech'])}")
print(f"Only NPC proper names: {len(results['only_proper_names'])}")
print(f"Only technical + NPC proper names: {len(results['only_tech_and_names'])}")
print(f"Has translatable content: {len(results['has_translatable'])}")

with open("incomplete_mods_analysis.json", "w", encoding="utf-8") as out:
    json.dump(results, out, indent=2, ensure_ascii=False)
