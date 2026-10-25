import sys
sys.path.insert(0, 'src')
from pathlib import Path
from core.string.string_loader import StringLoader

path = Path(r"E:\Code\Projects\SSE-Auto-Translator\src\data\user\database\french\Whiterun Outskirts Market for SSE - French\kojaks whiterun market.esp.ats")
strings = StringLoader.load_strings_from_legacy_file(path)
for s in strings:
    print(f"{s.original}  ===>  {s.string}")
