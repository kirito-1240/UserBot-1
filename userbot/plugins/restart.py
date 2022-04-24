from userbot import app
from userbot.utils import restart_app , runcmd
from userbot.events import alien
from userbot.database import DB
import Config
import os
import sys

@alien(pattern="restart")
async def restart(event):
    one = "█"
    two = "░"
    for i in range(0 , 6):
        c = 5 - int(i)
        await event.edit(f"""`• Restarting {one*i}{two*c}`""")      
    await event.edit("**• Bot Restarted!**\n\n`• Please Wait For A Minutes . . .`")
    DB.set_key("RESTART" , f"{event.id}||{event.chat_id}")
    if Config.HEROKU_API and Config.HEROKU_APP_NAME:
        restart_app()
    await runcmd("git pull")
    os.execl(sys.executable, "python3", "-m", "userbot")

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Restart Your Userbot!",
        "commands": {
            "{cmdh}restart": "To Restart Your Userbot!",
        },
    }
})
