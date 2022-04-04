from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player

@alien(pattern="skip")
async def skip_audio(event):
    await event.edit("`• Please Wait . . .`")
    player = Player(event.chat_id)
    await player.play_from_queue()
    await event.delete()
