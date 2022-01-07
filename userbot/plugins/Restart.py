from userbot import app
from telethon import events
from userbot.utils import load_plugins
import sys , os

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    event = await event.edit("` Restarting - [ ░░░ ]`")      
    await event.edit("`Restarting - [ █░░ ]`")
    await event.edit("`Restarting - [ ██░ ]`")
    await event.edit("`Restarting - [ ███ ]`")
    await event.edit("**• Bot Restarted!**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
    await app.disconnect()

