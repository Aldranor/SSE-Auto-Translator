import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('top_conflicts_report.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Find Perks_Skills and Spells_Magic
idx_perks = text.find('TOP CONFLICTS: Perks_Skills')
idx_spells = text.find('TOP CONFLICTS: Spells_Magic')

print("=== PERKS ===")
print("\n".join(text[idx_perks:idx_spells].splitlines()[:60]))

print("\n=== SPELLS ===")
print("\n".join(text[idx_spells:].splitlines()[:80]))
