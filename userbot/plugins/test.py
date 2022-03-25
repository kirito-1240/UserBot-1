from userbot.events import alien

@alien(pattern="test")
async def _(event):
    await event.client.send_file(event.chat_id , "Config.py")
