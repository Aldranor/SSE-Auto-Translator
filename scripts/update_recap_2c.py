with open('recap_modifications_phase2c.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = '| `00015265 (Skyrim.esm)`'
idx = text.find(target)
if idx != -1:
    new_row = '| `0003CBCB (Skyrim.esm)`<br>*CELL FULL* | Darklight Chambers | Chambres Clair-osbcur | **Tour Clair-Obscur - Chambres** | Correction de coquille dans le nom de lieu : Clair-Obscur (au lieu de Clair-osbcur) |\n'
    text = text[:idx] + new_row + text[idx:]
    text = text.replace("*Nombre d'ajustements majeurs :* **3**", "*Nombre d'ajustements majeurs :* **4**")
    with open('recap_modifications_phase2c.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated recap_modifications_phase2c.md with Darklight Chambers.')
