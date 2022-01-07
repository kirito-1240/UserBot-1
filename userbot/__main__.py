import glob
from pathlib import Path
from userbot.utils import load_plugins , load_plugins_inline
from . import app , bot

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

path = "userbot/inlinebot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins_inline(plugin_name.replace(".py", ""))


print("Successfully Deployed!")

app.start()
app.run_until_disconnected()
bot.run_until_disconnected()
