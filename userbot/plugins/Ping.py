from userbot import app
from telethon import events
from datetime import datetime

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^/ping$"))
async def start(event):
    start = datetime.now()
    edit = await event.edit("**Pong!!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await edit.edit(f"**• Pong!!** - `{ms}`")
