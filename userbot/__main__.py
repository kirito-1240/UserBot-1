from userbot.utils import load_plugins
from pathlib import Path
from . import app
import logging , sys
import importlib
import glob

print("• Starting Setup Plugins ...")
path = "userbot/plugin/*.py"
files = glob.glob(path)
files.remove("userbot/plugin/__init__.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        try:
            load_plugins(plugin_name.replace(".py", ""))
            print(f"""• UserBot Has Imported {plugin_name.replace(".py", "")} Plugin""")
        except Exception as e:
            print(f"""• UserBot Can't Import {plugin_name.replace(".py", "")} Plugin - Becuse Of Error {e}""")
print("• Setup Plugins Completed!")
print("• UserBot Has Been Start Now!")

app.run()
