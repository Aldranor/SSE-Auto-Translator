import json
from collections import defaultdict

with open('translation_audit_results.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("=== SUMMARY ===")
print("Broken variables:", len(data.get('broken_variables', [])))
print("False friends:", len(data.get('false_friends', [])))
print("Untranslated english:", len(data.get('untranslated_english', [])))
print("Internal inconsistencies:", len(data.get('internal_inconsistencies', [])))
print("Bad syntax names:", len(data.get('bad_syntax_names', [])))

print("\n=== DETAILED FALSE FRIENDS ===")
for item in data.get('false_friends', []):
    print(f"Mod/File: {item.get('context')}")
    print(f"  Orig: {repr(item.get('original'))[:100]}")
    print(f"  Trad: {repr(item.get('translation'))[:100]}")
    print(f"  Issue: {item.get('issue')}\n")

print("\n=== DETAILED BAD SYNTAX NAMES ===")
for item in data.get('bad_syntax_names', []):
    print(f"Mod/File: {item.get('context')}")
    print(f"  Orig: {repr(item.get('original'))}")
    print(f"  Trad: {repr(item.get('translation'))}")
    print(f"  Issue: {item.get('issue')}\n")

print("\n=== SAMPLE UNTRANSLATED ENGLISH (first 25) ===")
for item in data.get('untranslated_english', [])[:25]:
    print(f"Mod/File: {item.get('context')}")
    print(f"  Orig: {repr(item.get('original'))[:80]}")
    print(f"  Trad: {repr(item.get('translation'))[:80]}\n")

# Filter out book formatting tags like <font size=...> or <img ...> if they were counted as variables
real_var_issues = []
for item in data.get('broken_variables', []):
    orig = item.get('original', '')
    trad = item.get('translation', '')
    issue = item.get('issue', '')
    if any(tag in issue for tag in ['<mag>', '<dur>', '<min>', '<max>', '<lvl>', '<%']):
        real_var_issues.append(item)

print(f"\nTotal broken game variables (<mag>, <dur>, etc.): {len(real_var_issues)}")
for item in real_var_issues[:20]:
    print(f"Mod/File: {item.get('context')}")
    print(f"  Orig: {repr(item.get('original'))[:80]}")
    print(f"  Trad: {repr(item.get('translation'))[:80]}")
    print(f"  Issue: {item.get('issue')}\n")
