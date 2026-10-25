import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('top_conflicts_report.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for line in lines[:120]:
    print(line)
