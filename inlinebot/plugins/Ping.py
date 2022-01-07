from inlinebot import bot , START_TIME
from telethon import events
from datetime import datetime
import time
from inlinebot.functions import convert_time

@bot.on(events.NewMessage(pattern="(?i)^\.ping$"))
async def start(event):
    start = datetime.now()
    edit = await event.reply("**Pong!!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = convert_time(time.time() - START_TIME)
    await edit.edit(f"**• Pong!!** - `{ms}`\n**• Uptime :** `{uptime}`")
