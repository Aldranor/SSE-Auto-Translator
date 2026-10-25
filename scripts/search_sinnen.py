import os

def search_text(base_dir, text):
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith(('.json', '.ats', '.txt')):
                p = os.path.join(root, f)
                try:
                    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                        c = fp.read()
                    if text.lower() in c.lower():
                        print(f"Found '{text}' in: {p}")
                except Exception:
                    pass

search_text('data', 'barrière')
search_text(r'E:\Code\Projects\SSE-Auto-Translator\src\data', 'barrière')
search_text(r'D:\Nolvus\Instances\Nolvus Awakening\MODS\mods', 'Sinnen')
