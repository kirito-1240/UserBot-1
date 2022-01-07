from userbot import app , START_TIME
from telethon import events
from datetime import datetime
import time
from userbot.utils import convert_time

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.ping$"))
async def start(event):
    start = datetime.now()
    edit = await event.edit("**Pong!!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = convert_time(time.time() - START_TIME)
    await edit.edit(f"**• Pong!!** - `{ms}`\n**• Uptime :** `{uptime}`")
