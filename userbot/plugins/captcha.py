from userbot import app
from userbot.events import alien
from userbot.database import DB

@alien(pattern="(add|del)captcha")
async def set_type(event):
    await event.edit("`• Please Wait . . .`")
    pow = event.pattern_match.group(1)
    chats = DB.get_key("CAPTCHA_CHATS") or []
    if pow.lower() == "add":
        if not event.chat_id in chats:
            chats.append(event.chat_id)
            DB.set_key("CAPTCHA_CHATS", chats)
        await event.edit("**• Captcha For This Chat Has Been Actived!**")
    else:
        if event.chat_id in chats:
            chats.remove(event.chat_id)
            DB.set_key("CAPTCHA_CHATS", chats)
        await event.edit("**• Captcha For This Chat Has Been DeActived!**")

@alien(pattern="captype (photo|text)")
async def set_type(event):
    await event.edit("`• Please Wait . . .`")
    type = event.pattern_match.group(1)
    if type.lower() == "photo":
        DB.set_key("CAPTCHA_TYPE", "photo")
        await event.edit("**• Captcha Mode Was Changed To Photo Mode!**")
    else:
        DB.set_key("CAPTCHA_TYPE", "text")
        await event.edit("**• Captcha Mode Was Changed To Text Mode!**")

@alien(pattern="capcount (\d*)")
async def set_type(event):
    await event.edit("`• Please Wait . . .`")
    count = int(event.pattern_match.group(1))
    if count > 25:
        return await event.edit("**• Please Enter A Number Later 25!**")
    DB.set_key("CAPTCHA_COUNT", count)
    await event.edit(f"**• Captcha Values Count Was Changed To {count} Values!**")

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Captcha Mode For New Members!",
        "commands": {
            "{cmdh}addcaptcha": "To Active Captcha Mode For Chat!",
            "{cmdh}delcaptcha": "To DeActive Captcha Mode For Chat!",
            "{cmdh}captype photo": "To Set Captcha Mode On Photo Mode!",
            "{cmdh}captype text": "To Set Captcha Mode On Text Mode!",
            "{cmdh}capcount [count]": "To Set Captcha Values Count!",
        },
    }
})
