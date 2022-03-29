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
    list = []
    for x in range(0,9):
        photo = await download_file(photos[x], f"photo{x}.jpg")
        list.append(photo)
    await app.send_file(event.chat_id, list, caption=f"""**• Photos By:** {DB.get_key("OWNER_NAME")}""")
    await event.delete()
    for photo in list:
        os.remove(photo)
