from userbot import app
from userbot.events import alien
from html_telegraph_poster import upload_image
import os

@alien(pattern="(?i)^\.uptel$")
async def uploadtelegraph(event):
    await event.edit("`• Please Wait . . .`")
    reply = await event.get_reply_message()
    if reply:
        photo = await app.download_media(reply.media)
        link = upload_image(photo)
        await event.edit(f"**• Your Telegraph Link:** ( {link} )")
        os.remove(photo)
