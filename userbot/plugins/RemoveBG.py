from . import *

@app.on_message(filters.me & filters.regex("(?i)^\.rmbg$"))
async def RemoveBG(client , event):
    await event.edit_text("`• Please Wait ...`")
    if event.reply_to_message and event.reply_to_message.photo:
        media = event.reply_to_message.photo
        await app.download_media(media , "reminput.png")
        response = requests.post("https://api.remove.bg/v1.0/removebg" , files={'image_file': open("reminput.png" , "rb")} , data={'size': 'auto'} , headers={'X-Api-Key': Config.RMBG_API_KEY})
        file = open("outrem.png" , "wb")
        file.write(response.content)
        img = Image.open("outrem.png")
        img.save("outrem.webp", "webp")
        img.seek(0)
        await event.delete()
        await app.send_photo(event.chat.id , "outrem.png" , reply_to_message=event.reply_to_message.id , caption="**• Removed Background From Your Photo!**")
        await app.send_sticker(event.chat.id , open("outrem.webp", "rb") , reply_to_message=event.reply_to_message.id)
        os.remove("outrem.png")
        os.remove("reminput.png")
        os.remove("outrem.webp")
    else:
        await event.edit_text("**• Please Reply To Photo!**")
