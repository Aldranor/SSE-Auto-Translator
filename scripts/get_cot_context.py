import json

path = r'data/user/database/french/Citizens of Tamriel/citizenscomplete.esp.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find the 26 TranslationRequired + entry 3375
indices = []
for i, e in enumerate(data):
    if e.get('status') != 'TranslationComplete' or i == 3375:
        indices.append(i)

print(f"Total target lines: {len(indices)}")

with open('cot_lines_context.txt', 'w', encoding='utf-8') as out:
    for idx in indices:
        e = data[idx]
        out.write(f"================================================================================\n")
        out.write(f"Index: {idx} | FormID: {e.get('form_id')} | Type: {e.get('type')}\n")
        out.write(f"ORIGINAL: {e.get('original')}\n")
        out.write(f"CURRENT : {e.get('string')}\n")
        out.write(f"STATUS  : {e.get('status')}\n\n")
        out.write("CONTEXT (5 preceding lines):\n")
        start = max(0, idx - 5)
        for prev in range(start, idx):
            pe = data[prev]
            out.write(f"  [{prev}] ({pe.get('type')}) ORIG: {pe.get('original')[:60]} -> TRAN: {pe.get('string')[:60]}\n")
        out.write("CONTEXT (5 following lines):\n")
        end = min(len(data), idx + 6)
        for nxt in range(idx + 1, end):
            ne = data[nxt]
            out.write(f"  [{nxt}] ({ne.get('type')}) ORIG: {ne.get('original')[:60]} -> TRAN: {ne.get('string')[:60]}\n")
        out.write("\n")

print("Done writing cot_lines_context.txt")
