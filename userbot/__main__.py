import glob
from pathlib import Path
from userbot.utils import load_plugins
from . import app
from Config import Config
from time import sleep

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        try:
            load_plugins(plugin_name.replace(".py", ""))
            print(f"""• UserBot Has Imported {plugin_name.replace(".py", "")} Plugin""")
        except Exception as e:
            print(f"""• UserBot Can't Import {plugin_name.replace(".py", "")} Plugin - Becuse Of Error {e}""")

app.start()
app.run_until_disconnected()
