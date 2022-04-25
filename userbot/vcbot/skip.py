from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player

@alien(pattern="skip")
async def skip_audio(event):
    await event.edit("`• Please Wait . . .`")
    player = Player(event.chat_id)
    await player.play_from_queue()
    await event.delete()

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Skip Current Playing On Group Voice Chat!",
        "commands": {
            "{cmdh}skip": "To Skip Current Playing On On Group Voice Chat!",
        },
    }
})
