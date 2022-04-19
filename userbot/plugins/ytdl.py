from userbot import app , bot
from userbot.events import alien
from userbot.database import DB
import re

@alien(pattern="ytdl (.*)")
async def ytdl(event):
    await event.edit("`• Please Wait . . .`")
    if not re.search("((?:https|http)?:\/\/)?(?:www\.)?youtu(?:\.be\/|be.com\/\S*(?:watch|embed)(?:(?:(?=\/[-a-zA-Z0-9_]{10,}(?!\S))\/)|(?:\S*v=|v\/)))([-a-zA-Z0-9_]{10,})", str(event.text)):
        return await event.edit("**• Your Link Is Invalid!**")
    link = str(event.pattern_match.group(1))
    me = await bot.get_me()
    results = await app.inline_query(me.username, f"ytdl_{link}")
    click = await results[0].click(event.chat_id)
    DB.set_key("YOUTUBE_GET_INLINE", f"{event.chat_id}||{click.id}")
    await event.delete()
