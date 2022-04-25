from userbot import app , bot
from userbot.events import alien
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
        await event.delete()
    else:
        await event.edit("**• Your Link Is Invalid!**")

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Download From Youtube!",
        "commands": {
            "{cmdh}ytdl [link]": "To Download Given Youtube Link On All Formats!",
        },
    }
})
