from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player

@alien(pattern="volume (.*)")
async def volume(event):
    await event.edit("`• Please Wait . . .`")
    vol = int(event.pattern_match.group(1))
    if vol > 200:
        vol = 200
    player = Player(event.chat_id)
    await player.group_call.set_my_volume(vol)
    await event.edit(f"**• Set My Volume On Voice Chat To:** ( `{vol}` )")

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Change Volume On Group Voice Chat!",
        "commands": {
            "{cmdh}volume [0,200]": "To Change Volume On Group Voice Chat!",
        },
    }
})
