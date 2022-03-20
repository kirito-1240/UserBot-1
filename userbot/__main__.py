from userbot.utils import load_plugins , load_pluginss
from pathlib import Path
from . import app , bot
import logging , sys , os
import importlib
import glob

print("• Starting Setup Plugins ...")
path = "userbot/plugins/*.py"
files = glob.glob(path)
files.remove("userbot/plugins/__init__.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        try:
            load_plugins(plugin_name.replace(".py", ""))
            print(f"""• UserBot Has Imported ( {plugin_name.replace(".py", "")} ) Plugin""")
        except Exception as e:
            print(f"""• UserBot Can't Import ( {plugin_name.replace(".py", "")} ) Plugin - Error : < {e} >""")
print("• Starting Setup Assistant Plugins ...")
path = "userbot/assistant/*.py"
files = glob.glob(path)
files.remove("userbot/assistant/__init__.py")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        try:
            load_pluginss(plugin_name.replace(".py", ""))
            print(f"""• AssistantBot Has Imported ( {plugin_name.replace(".py", "")} ) Plugin""")
        except Exception as e:
            print(f"""• AssistantBot Can't Import ( {plugin_name.replace(".py", "")} ) Plugin - Error : < {e} >""")

print("• Setup All Plugins Completed!")
print("• UserBot And AssistantBot Has Been Start Now!")

async def setup():
    await app.send_message("@Mrabolii" , "test")

app.loop.run_until_complete(setup())

async def setupp():
    await bot.send_message("@Mrabolii" , "test")

bot.loop.run_until_complete(setupp())

app.run_until_disconnected()
