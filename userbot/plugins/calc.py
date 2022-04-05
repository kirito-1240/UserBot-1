from userbot import app , bot
from userbot.events import alien
import Config

@alien(pattern="calc")
async def help(event):
    await event.edit("`• Please Wait . . .`")
    me = await bot.get_me()
    results = await app.inline_query(me.username, "alien_calc")
    await results[0].click(event.chat_id)
    await event.delete()

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Get Calc Panel!",
        "commands": {
            "{cmdh}help": "To Get Inline Calc!",
        },
    }
})
