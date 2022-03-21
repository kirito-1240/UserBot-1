from userbot import app
from userbot.utils import restart_app , runcmd
from telethon import events
import os
import sys

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def restart(event):
    one = "█"
    two = "░"
    for i in range(0 , 8):
        c = 7 - int(i)
        await event.edit(f"""`• Restarting - {one*i}{two*c}`""")      
    await event.edit("**• Bot Restarted!**")
    restart_app()
    await runcmd("git pull && git push -u heroku master")
    os.execl(sys.executable, sys.executable, "-m", "userbot")

