from userbot import app , START_TIME
from pyrogram import filters
from datetime import datetime
from userbot.utils import convert_time

@app.on_message(filters.me & filters.regex("(?i)^\.ping$"))
async def Ping(client, event):
    start = datetime.now()
    edit = await event.edit_text("**Pong!!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = convert_time(time.time() - START_TIME)
    await edit.edit_text(f"**• Pong!!** `{ms}`\n**• Uptime :** `{uptime}`")
