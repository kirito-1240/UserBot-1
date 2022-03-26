from userbot import app , START_TIME
from userbot.events import alien
from userbot.database import CMDS_HELP
from datetime import datetime
from userbot.utils import convert_time
import time

@alien(pattern="(?i)^\.ping$")
async def ping(event):
    start = datetime.now()
    await event.edit("**Pong!!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = convert_time(time.time() - START_TIME)
    await event.edit(f"**• Pong!!** `{ms}`\n**• Uptime :** `{uptime}`")



plugin = ((__name__).split(".")[-1])
CMDS_HELP.update(
    {
        plugin:{
            "info": "To Get Ping And Uptime For Your Bot!",
            "cmds": {".ping": "To Get Ping And Uptime!"},
            "exm": [".ping"],
       }
    }
)
