import glob
from pathlib import Path
from . import app
from Config import Config
from time import sleep

with app:
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    app.send_message(Config.BOT_GROUP , "**•Start**")
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
