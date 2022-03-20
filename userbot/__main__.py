from userbot.utils import load_plugins , load_pluginss , AddBot
from pathlib import Path
from telethon import Button
from . import app , bot , LOG
import logging , sys , os
import importlib
import glob

async def setup():
    me = await app.get_me()
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
    print("• Setup Plugins Completed!")
    await AddBot()
    if me.username:
        username = "@" + me.username
    else:
        username = f"[{me.first_name}](tg://user?id={me.id})"
    await bot.send_file(LOG , "./userbot/other/bot.jpg" , caption=f"**• UserBot And AssistantBot Has Been Start Now!**\n\n**• You Can User The RoBot:** {me.username}" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])

bot.loop.run_until_complete(setup())

app.run_until_disconnected()
