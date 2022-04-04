from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player

@alien(pattern="skip")
async def skip_audio(event):
    await event.edit("`• Please Wait . . .`")
    player = Player(event.chat_id)
    if player.group_call.is_connected:
        await player.play_from_queue()
        await event.delete()
    else:
        await event.edit("**• Not Recommended Audio For Voice Chat In This Chat!**")
