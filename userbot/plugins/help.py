from userbot import app , bot
from userbot.events import alien
from userbot import Config

@alien(pattern="help ?(.*)?")
async def help(event):
    await event.edit("`• Please Wait . . .`")
    if event.pattern_match.group(1):
        data = str(event.pattern_match.group(1))
        if data in PLUGINS_HELP:
            info = PLUGINS_HELP[data] 
            text = f"** 💡 Plugin Name:** ( `{data.title()}` )"
            text += f"""\n\n** 🧾 Plugin Info:** ( `{info["info"]}` )"""
            text += f"""\n\n\n** ♻️ Available Commands** ( `{len(info["commands"])}` ):"""
            for com in info["commands"]:
                text += "\n • `{}`\n      `{}`\n".format(com.format(cmdh=Config.COMMAND_HANDLER), info["commands"][com])
            await event.edit(text)
        else:
            await event.edit("**• Not Available This Plugin!**")
    else:
        me = await bot.get_me()
        results = await app.inline_query(me.username, "alien")
        await results[0].click(event.chat_id)
        await event.delete()

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Get Help From Userbot!",
        "commands": {
            "{cmdh}help": "To Get Help From Userbot!",
            "{cmdh}help [plugin_name]": "To Get Help From A Plugin!",
        },
    }
})
