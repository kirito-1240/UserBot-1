from userbot import app
from userbot.events import alien
from userbot.functions.tools import download_file, unsplashsearch
from userbot.functions.logo import LogoMaker
from userbot.database import DB
import random, glob

@alien(pattern="(?i)^.logo (.*)$")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    text = str(event.pattern_match.group(1))
    query = random.choice(["blur", "blur background", "background", "neon lights", "lights", "wallpaper"])
    photo = await unsplashsearch(query)
    photo = await download_file(random.choice(photo), "last.jpg")
    font = random.choice(glob.glob("userbot/other/fonts/*"))
    stroke_width = int(len(text)) / 2
    LogoMaker.make_logo(photo, text, font, "output.png", fill="white", stroke_width=stroke_width, stroke_fill="black")
    await app.send_file(event.chat_id, "output.png", caption=f"""**• Logo By:** {DB.get_key("OWNER_NAME")}""")
    await event.delete()
    os.remove("output.png")
    os.remove(photo)
