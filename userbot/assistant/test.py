from userbot import app
from userbot.database import DB
from telethon import events

@app.on(events.Raw)
async def handler(update):
    if "UpdateChannel" in str(update):
        open("event.txt", "w").write(str(update.stringify()))
        await app.send_file(DB.get_key("LOG_GROUP"), file="event.txt")
