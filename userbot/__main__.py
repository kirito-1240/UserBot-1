from userbot.utils import load_plugins , load_pluginss
from pathlib import Path
from . import app , bot , LOG
import logging , sys , os
from asyncio import sleep
import importlib
import glob

async def setup():
    edit = await bot.send_message(LOG , "`• Starting Setup Plugins ...`")
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    files.remove("userbot/plugins/__init__.py")
    for name in files:
        sleep(1)
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_plugins(plugin_name.replace(".py", ""))
                await edit.reply(f"""• UserBot Has Imported ( {plugin_name.replace(".py", "")} ) Plugin""")
            except Exception as e:
                await edit.reply(f"""• UserBot Can't Import ( {plugin_name.replace(".py", "")} ) Plugin - Error : < {e} >""")
    editt = await bot.send_message(LOG , "`• Starting Setup Assistant Plugins ...`")
    path = "userbot/assistant/*.py"
    files = glob.glob(path)
    files.remove("userbot/assistant/__init__.py")
    for name in files:
        sleep(1)
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_pluginss(plugin_name.replace(".py", ""))
                await editt.reply(f"""• AssistantBot Has Imported ( {plugin_name.replace(".py", "")} ) Plugin""")
            except Exception as e:
                await editt.reply(f"""• AssistantBot Can't Import ( {plugin_name.replace(".py", "")} ) Plugin - Error : < {e} >""")
    sleep(2)
    await bot.send_message(LOG , "• Setup All Plugins Completed!")
    await bot.send_message(LOG , "• UserBot And AssistantBot Has Been Start Now!")

bot.loop.run_until_complete(setup())

app.run_until_disconnected()
