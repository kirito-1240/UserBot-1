from userbot import app
from telethon import events

@app.on(events.ChatAction)
async def test(event):
    if event.chat_id == 1712714552 or event.chat_id == 1781754793:
        open("event.txt", "w").write(str(event))
        await event.reply(file="event.txt")
