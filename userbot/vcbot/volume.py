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
