from userbot.utils import load_plugins
from userbot import app
from pathlib import Path
import glob

path = "userbot/setu*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        print("• UserBot Has Imported Setup Plugin")
        print("• Please Send ( .setup ) Command On Telegram To Setup Plugins")


app.start()
app.run_until_disconnected()
