from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player, CLIENTS, VIDEO_ON

@alien(pattern="leavevc")
async def leavevc(event):
    await event.edit("`• Please Wait . . .`")
    player = Player(event.chat_id)
    chat = event.chat_id
    await player.group_call.stop()
    await player.group_call.leave()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await event.edit("**• Successfuly Leaved From Voice Chat In This Chat!**")
