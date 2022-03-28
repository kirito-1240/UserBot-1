from userbot import app , bot
from userbot.events import alien

@alien(pattern="(?i)^\.help$")
async def help(event):
    me = await bot.get_me()
    results = await app.inline_query(me.username, "alien_inline_help")
    await results[0].click(event.chat_id)
    await event.delete()
