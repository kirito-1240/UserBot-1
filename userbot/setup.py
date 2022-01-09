from userbot import app
from telethon import events
from userbot.utils import load_plugins
from time import sleep
from pathlib import Path
import glob , sys

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.setup$"))
async def start(event):
    edit = await event.edit("**• Starting Setup Plugins ...**")
    sleep(3)
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_plugins(plugin_name.replace(".py", ""))
                print(f"""• UserBot Has Imported {plugin_name.replace(".py", "")} Plugin""")
                await event.edit(f"""**• UserBot Has Imported :** ( `{plugin_name.replace(".py", "")}` )**Plugin!**""")
                sleep(1.5)
            except Exception as e:
                print(f"""• UserBot Can't Import {plugin_name.replace(".py", "")} Plugin - Becuse Of Error {e}""")
                await event.edit(f"""**• UserBot Can't Import :** ( `{plugin_name.replace(".py", "")}` ) **Plugin - Becuse Of Error :** ( `{e}` )""")
                sleep(1.5)
    await edit.edit("**• Setup Plugins Completed!**")
    await app.send_message(event.chat_id , "**• UserBot Has Been Start Now!**")
