from userbot import app
from telethon import events
from userbot.utils import load_plugins
import sys , os

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    event = await event.edit("` Restarting - [ ░░░ ]`")      
    await event.edit("`Restarting - [ █░░ ]`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    await event.edit("`Restarting - [ ██░ ]`")
    quit()
    await event.edit("`Restarting - [ ███ ]`")
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))
    await event.edit("**• Bot Restarted!**")
    await app.disconnect()

