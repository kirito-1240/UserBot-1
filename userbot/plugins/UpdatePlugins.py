from userbot import app
from userbot.utils import load_plugins
from telethon import events
import sys , os , glob
from time import sleep
from pathlib import Path

@app.on(events.NewMessage(pattern="(?i)^\.upplugins$"))
async def UpdatePlugins(event):
    event = await event.edit("**• Starting Import UserBot Plugins ...**")
    sleep(3)
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))
            await event.edit(f"""**• UserBot Has Imported :** ( `{plugin_name.replace(".py", "")}` )""")
            sleep(2)
    await event.edit("**• UserBot Has Imported Plugins!**")
