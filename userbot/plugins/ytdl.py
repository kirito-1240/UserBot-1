from userbot import app , bot
from userbot.events import alien
import re

@alien(pattern="ytdl (.*)")
async def ytdl(event):
    await event.edit("`• Please Wait . . .`")
    if not re.search("/(?:https?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{11,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{11,})/gm", str(event.text)):
        return await event.edit("**• Your Link Is Invalid!**")
    link = str(event.pattern_match.group(1))
    me = await bot.get_me()
    results = await app.inline_query(me.username, f"ytdl_{link}")
    await results[0].click(event.chat_id)
    await event.delete()
