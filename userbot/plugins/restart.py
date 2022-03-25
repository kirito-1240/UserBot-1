from userbot import app
from userbot.utils import restart_app , runcmd
from telethon import events
from userbot.database import DB
import os
import sys

@alien(pattern="(?i)^\.restart$")
async def restart(event):
    one = "█"
    two = "░"
    for i in range(0 , 6):
        c = 5 - int(i)
        await event.edit(f"""`• Restarting {one*i}{two*c}`""")      
    await event.edit("**• Bot Restarted!**\n\n`• Please Wait For A Minutes . . .`")
    DB.set_key("RESTART" , f"{event.id}||{event.chat_id}")
    restart_app()
    await runcmd("git pull -f -q && pip3 install --no-cache-dir -U -q -r requirements.txt")
    os.execl(sys.executable, "python3", "-m", "userbot")
