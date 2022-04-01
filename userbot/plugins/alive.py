from userbot import app, START_TIME
from userbot.utils import convert_time
from userbot.events import alien
from userbot.database import DB
from platform import python_version
from telethon import version
import time

@alien(pattern="alive")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    uptime = convert_time(time.time() - START_TIME)
    await event.reply(f"""
**• Alien Userbot Has Been Online!**\n
**💡 Telethon Version :** ( `{version.__version__}` )
**💡 Python Version :** ( `{python_version()}` )
**💡 Uptime :** ( `{uptime}` )
**💡 Database :** ( `{DB.name}` )
**💡 Master:** ( {DB.get_key("OWNER")} )
""", file=DB.get_key("ALIVE_PIC"))
    await event.delete()

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Chack Alive Userbot!",
        "commands": {
            "{cmdh}alive": "To Check Alive Userbot!",
        },
    }
})
