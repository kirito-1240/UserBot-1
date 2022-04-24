from userbot import app
from userbot.events import alien
from userbot.database import DB

@alien(pattern="captcha (on|off)")
async def set_type(event):
    await event.edit("`• Please Wait . . .`")
    pow = event.pattern_match.group(1)
    chats = DB.get_key("CAPTCHA_CHATS") or []
    if pow.lower() == "on":
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
