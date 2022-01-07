import glob
from pathlib import Path
from inlinebot.utils import load_plugins
from . import bot
from Config import Config
from time import sleep

path = "inlinebot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))


print("• Successfully Deployed InlineBot!")

bot.run_until_disconnected()
