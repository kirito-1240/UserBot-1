from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player

@alien(pattern="joinvc")
async def joinvc(event):
    await event.edit("`• Please Wait . . .`")
    player = Player(event.chat_id)
    if not player.group_call.is_connected:
        await player.vc_joiner()
        await event.delete()
    else:
        await event.edit("**• Already On Voice Chat In This Chat!**")
