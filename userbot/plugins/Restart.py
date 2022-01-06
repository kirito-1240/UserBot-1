from userbot import app
from telethon import events
import sys , os

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    await event.edit("` Restarting - [ ░░░ ]`")
    await event.edit("`Restarting - [ █░░ ]`")
    await event.edit("`Restarting - [ ██░ ]`")
    await event.edit("`Restarting - [ ███ ]`")
    await event.edit("**• Bot Restarted!**")
    await app.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
