from userbot.events import alien
from userbot.utils import restart_app
from userbot.database import DB

@alien(pattern="restart")
async def restart(event):
    await event.edit("**• Bot Restarted!**\n\n`• Please Wait For A Minutes . . .`")
    DB.set_key("RESTART" , f"{event.id}||{event.chat_id}")
    restart_app()

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
