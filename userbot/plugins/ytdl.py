from userbot import app , bot
from userbot.events import alien
from userbot.database import DB
import re

@alien(pattern="ytdl (.*)")
async def ytdl(event):
    await event.edit("`• Please Wait . . .`")
    link = str(event.pattern_match.group(1))
    if match := re.match('(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(shorts/|watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})(.*)', link):
        me = await bot.get_me()
        link = "https://youtu.be/" + match["id"]
        results = await app.inline_query(me.username, f"ytdl_{link}")
        click = await results[0].click(event.chat_id)
        DB.set_key("YOUTUBE_GET_INLINE", f"{event.chat_id}||{click.id}")
        await event.delete()
    else:
        await event.edit("**• Your Link Is Invalid!**")
