from userbot import app
from userbot.events import alien
from userbot.functions.tools import download_file, unsplashsearch
from userbot.functions.logo import LogoMaker
from userbot.database import DB
import random, glob, os

@alien(pattern="sphoto (.*)")
async def photosearch(event):
    await event.edit("`• Please Wait . . .`")
    query = str(event.pattern_match.group(1))
    photos = await unsplashsearch(query)
    if not photos:
        return await event.edit("**• Not Found Photo For Your Query!**")
    list = []
    c = 0
    for photo in photos:
        photo = await download_file(photo, f"photo{c}.jpg")
        list.append(photo)
        c += 1
        if c == 10:
            await app.send_file(event.chat_id, list, caption=f"""**• Query:** ( `{query}` )\n**• Count:** ( `{len(photos)}` )\n\n**• Photos By:** {DB.get_key("OWNER")}""")
            for photo in list:
                os.remove(photo)
            list = []
    if len(list) != 0:
        await app.send_file(event.chat_id, list, caption=f"""**• Query:** ( `{query}` )\n**• Count:** ( `{len(photos)}` )\n\n**• Photos By:** {DB.get_key("OWNER")}""")
        for photo in list:
            os.remove(photo) 
    await event.delete()
