from userbot import app
from userbot.events import alien
from userbot.functions.tools import download_file, unsplashsearch
from userbot.functions.logo import LogoMaker
from userbot.database import DB
import random, glob, os

@alien(pattern="(?i)^\.logo (.*)$")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    text = str(event.pattern_match.group(1))
    colors = ["green", "blue", "red", "black", "white", "orange", "yellow", "purple", "pink", "gray"]
    query = random.choice(["blur", "color", "blur background", "background", "neon", "neon lights", "lights", "light", "city", "car", "wallpaper"])
    photo = await unsplashsearch(query)
    photo = await download_file(random.choice(photo), "last.jpg")
    font = random.choice(glob.glob("userbot/other/fonts/*"))
    await event.reply(str(font))
    stroke_width = int(len(text))
    if stroke_width < 4:
        return await event.edit("**• Please Enter A Text Larger Than 4 Word!**")
    LogoMaker.make_logo(photo, text, font, "output.png", fill=random.choice(colors), stroke_width=stroke_width / 2, stroke_fill=random.choice(colors))
    await app.send_file(event.chat_id, "output.png", caption=f"""**• Logo By:** {DB.get_key("OWNER_NAME")}""")
    await event.delete()
    os.remove("output.png")
    os.remove(photo)
