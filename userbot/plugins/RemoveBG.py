from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.rmbg$"))
async def RemoveBG(event):
    await event.edit("`• Please Wait ...`")
    if not event.reply_to == None and event.reply_to_message.photo:
        media = event.reply_to_message.photo
        media = await app.download_media(media)
        response = requests.post("https://api.remove.bg/v1.0/removebg" , files={'image_file': open(media , "rb")} , data={'size': 'auto'} , headers={'X-Api-Key': Config.RMBG_API_KEY})
        file = open("outrem.png" , "wb")
        file.write(response.content)
        img = Image.open("outrem.png")
        img.save("outrem.webp", "webp")
        img.seek(0)
        await event.delete()
        await app.send_document(event.chat.id , "outrem.png" , reply_to_message_id=event.reply_to_message.message_id , file_name="Remove.png" , caption="**• Removed Background From Your Photo!**")
        await app.send_sticker(event.chat.id , open("outrem.webp", "rb") , reply_to_message_id=event.reply_to_message.message_id)
        os.remove("outrem.png")
        os.remove(media)
        os.remove("outrem.webp")
    else:
        await event.edit_text("**• Please Reply To Photo!**")
