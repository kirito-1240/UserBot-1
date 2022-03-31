from userbot import app
from userbot.events import alien
from userbot.functions.tools import Carbon
from userbot.database import DB

@alien(pattern="carbon ?(.*)?")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        code = str(event.pattern_match.group(1))
    elif reply and reply.text:
        code = str(reply.text)
    else:
        return await event.edit("**• Please Input A Text Or Reply To A Message!**")
    file = await Carbon(code)
    await app.send_file(event.chat_id, file, caption=f"""**• Carbonised By:** {DB.get_key("OWNER")}""")
    await event.delete()
