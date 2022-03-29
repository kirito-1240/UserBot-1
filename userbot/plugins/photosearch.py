from userbot import app
from userbot.events import alien
from userbot.functions.tools import download_file, unsplashsearch
from userbot.functions.logo import LogoMaker
from userbot.database import DB
import random, glob, os

@alien(pattern="(?i)^\.psearch (.*)$")
async def photosearch(event):
    await event.edit("`• Please Wait . . .`")
    query = str(event.pattern_match.group(1))
    photos = await unsplashsearch(query)
    if not photos:
        return await event.edit("**• Not Found Photo For Your Query!**")
    list = []
    c = 1
    for x in photos:
        photo = await download_file(photos[x], f"photo{x}.jpg")
        list.append(photo)
        c += 1
        if c == 10:
            return
    await app.send_file(event.chat_id, list, caption=f"""**• Photos By:** {DB.get_key("OWNER_NAME")}""")
    await event.delete()
    for photo in list:
        os.remove(photo)
