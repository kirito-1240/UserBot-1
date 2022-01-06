from userbot import app
from telethon import events
import os , sys

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    await event.edit("**• Bot Restarted!**")
    python = sys.executable
    os.execl(python, python, *sys.argv)
