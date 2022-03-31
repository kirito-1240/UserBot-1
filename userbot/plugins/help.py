from userbot import app , bot
from userbot.events import alien

@alien(pattern="help")
async def help(event):
    await event.edit("`• Please Wait . . .`")
    me = await bot.get_me()
    results = await app.inline_query(me.username, "alien")
    await results[0].click(event.chat_id)
    await event.delete()

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Get Help From Userbot!",
        "commands": ["{cmdh}help"],
    }
})
