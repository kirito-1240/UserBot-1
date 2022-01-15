from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.imbin$"))
async def ImageToBinary(event):
    await event.edit("`• Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.media.photo:
        media = reply.media
        await app.download_media(media , "bininput.jpg")
        img = cv2.imread("bininput.jpg" , 0) 
        img = cv2.medianBlur(img, 5) 
        image = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) 
        cv2.imwrite("outbin.jpg" , image)
        await app.send_file(event.chat_id , "outbin.jpg" , reply_to=reply.id , caption="**• This Photo Converted To Binary Photo!**")
        await event.delete()
        os.system("outbin.jpg")
    else:
        await event.edit("**• Please Reply To Photo!**")
