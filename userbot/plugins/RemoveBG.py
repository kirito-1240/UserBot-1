from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.rmbg$"))
async def RemoveBG(event):
    await event.edit("`• Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.media.photo:
        media = reply.media.photo
        media = await app.download_media(media)
        response = requests.post("https://api.remove.bg/v1.0/removebg" , files={'image_file': open(media , "rb")} , data={'size': 'auto'} , headers={'X-Api-Key': Config.RMBG_API_KEY})
        file = open("outrem.png" , "wb")
        file.write(response.content)
        img = Image.open("outrem.png")
        img.save("outrem.webp", "webp")
        img.seek(0)
        await event.delete()
        await app.send_file(event.chat.id , "outrem.png" , reply_to=reply.id , file_name="Remove.png" , caption="**• Removed Background From Your Photo!**")
        await app.send_file(event.chat.id , open("outrem.webp", "rb") , reply_to=reply.id)
        os.remove("outrem.png")
        os.remove(media)
        os.remove("outrem.webp")
    else:
        await event.edit("**• Please Reply To Photo!**")
