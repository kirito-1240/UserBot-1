from userbot import app
from telethon import events
from Config import Config
import requests

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.rmbg$"))
async def RemoveBG(event):
    await event.edit("`• Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.media.photo:
        media = reply.media
        await app.download_media(media , "reminput.png")
        response = requests.post("https://api.remove.bg/v1.0/removebg" , files={'image_file': open("reminput.png" , "rb")} , data={'size': 'auto'} , headers={'X-Api-Key': Config.API_KEY})
        file = open("outrem.png" , "wb")
        file.write(response.content)
        await event.delete()
        await app.send_file(chat , "outrem.png")
        os.remove("outrem.png")
        os.remove("reminput.png")
    else:
        await event.edit("**• Please Reply To Photo!**")
