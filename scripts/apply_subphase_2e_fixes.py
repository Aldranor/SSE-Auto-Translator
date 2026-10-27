import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

recap_2e = []

def apply_precise_fixes(filepath, fixes_dict):
    """
    fixes_dict: {
        (form_id, type, index, original): (new_string, reason)
    }
    """
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)
        
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified_count = 0
    
    for (fid, typ, idx, orig), (new_str, reason) in fixes_dict.items():
        matches = [x for x in data if x.get('form_id') == fid and 
                                      x.get('type') == typ and 
                                      x.get('index') == idx and 
                                      x.get('original') == orig]
        
        if len(matches) == 0:
            print(f"[ERROR] 0 matches found in {os.path.basename(filepath)} for target:")
            print(f"   FID={fid}, TYPE={typ}, IDX={idx}, ORIG={repr(orig)}")
            sys.exit(1)
        elif len(matches) > 1:
            print(f"[FATAL BUG PREVENTED] {len(matches)} matches found in {os.path.basename(filepath)} for target:")
            print(f"   FID={fid}, TYPE={typ}, IDX={idx}, ORIG={repr(orig)}")
            sys.exit(1)
        
        item = matches[0]
        old_str = item.get('string')
        
        if old_str != new_str:
            recap_2e.append({
                'file': os.path.basename(filepath),
                'form_id': fid,
                'type': typ,
                'index': idx,
                'original': orig,
                'before': old_str,
                'after': new_str,
                'nature': reason
            })
            item['string'] = new_str
            item['status'] = 'TranslationComplete'
            modified_count += 1
        else:
            print(f"[INFO] Item already matches target string in {os.path.basename(filepath)}: {fid} -> {new_str}")

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully modified {modified_count} records in {os.path.basename(filepath)}.")
    return modified_count

# 1. attackodaedra.esp.json
f_att = 'data/user/database/french/AttackoDaedra.esp - French/attackodaedra.esp.json'
fixes_att = {
    ('0501A808|AttackoDaedra.esp', 'SPEL FULL', None, 'Namiiric Slash'): ('Entaille namiirique', "Correction de contresens critique : Slash = Entaille/Taillade (et non Flèche)"),
    ('0501A809|AttackoDaedra.esp', 'PROJ FULL', None, 'Namiiric Slash'): ('Entaille namiirique', "Correction de contresens critique : Slash = Entaille/Taillade (et non Flèche)")
}
apply_precise_fixes(f_att, fixes_att)

# 2. wintersun - gott patch.esp.json
f_w = 'data/user/database/french/Wintersun - Tribunal Integration/wintersun - gott patch.esp.json'
fixes_w = {
    ('05000A83|Wintersun - GotT Patch.esp', 'SPEL FULL', None, 'Epic Killer - Cloak Proc'): ('Tueur épique - Déclenchement de la cape', "Traduction de l'anglais résiduel et harmonisation avec Epic Killer - Cloak Start = Tueur épique - Début de la cape"),
    ('05000A82|Wintersun - GotT Patch.esp', 'MGEF FULL', None, 'Epic Killer - Cloak Proc'): ('Tueur épique - Déclenchement de la cape', "Traduction de l'anglais résiduel et harmonisation avec Epic Killer - Cloak Start = Tueur épique - Début de la cape")
}
apply_precise_fixes(f_w, fixes_w)

# 3. yot - clockwork.esp.json
f_yot = 'data/user/database/french/YOT - Clockwork.esp - French/yot - clockwork.esp.json'
fixes_yot = {
    ('01035426|Clockwork.esp', 'MESG DESC', None, 'I can only place one weapon on here.'): ('Une seule arme peut être placée ici.', "Correction de coquille orthographique et bégaiement 'arme une peut' -> 'arme peut'")
}
apply_precise_fixes(f_yot, fixes_yot)

print(f"\nTotal corrections successfully applied in Phase 2E: {len(recap_2e)}")

with open('recap_phase2e_diffs.json', 'w', encoding='utf-8') as f:
    json.dump(recap_2e, f, ensure_ascii=False, indent=2)

print("Saved recap_phase2e_diffs.json.")
