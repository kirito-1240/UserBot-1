from userbot import app , bot
from userbot.events import alien

@alien(pattern="ytdl (.*)")
async def ytdl(event):
    await event.edit("`• Please Wait . . .`")
    link = str(event.pattern_match.group(1))
    me = await bot.get_me()
    results = await app.inline_query(me.username, f"ytdl_{link}")
    await results[0].click(event.chat_id)
    await event.delete()
