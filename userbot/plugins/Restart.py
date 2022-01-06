from userbot import app
from telethon import events
import sys
from os import environ, execle

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    await event.edit("**• Bot Restarted!**")
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    exit()
    return
