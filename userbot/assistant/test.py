from userbot import app
from userbot.database import DB
from telethon import events

@app.on(events.ChatAction(func=lambda e : e.new_join_request))
async def test(event):
    open("event.txt", "w").write(str(event))
    await app.send_file(DB.get_key("LOG_GROUP"), file="event.txt")
