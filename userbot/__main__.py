from userbot.utils import load_plugins
from userbot import app
from pathlib import Path
import logging , sys
import importlib
import glob

path = "userbot/setu*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        plugin_name = plugin_name.replace(".py", "")
        path = Path(f"userbot/{plugin_name}.py")
        name = "userbot.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        spec.loader.exec_module(load)
        sys.modules["userbot." + plugin_name] = load
        print("• UserBot Has Imported Setup Plugin")
        print("• Please Send ( .setup ) Command On Telegram To Setup Plugins")


app.start()
app.run_until_disconnected()
