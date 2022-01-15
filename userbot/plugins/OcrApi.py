from . import *
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.ocr ?(\S*)?$"))
async def OcrApi(event):
    await event.edit("`• Please Wait ...`")
    if event.pattern_match.group(1):
        lang = str(event.pattern_match.group(1))
    else:
        lang = "eng"
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.media.photo:
        media = reply.media.photo
        await app.download_media(media , "ocrinput.jpg")
        result = ocr_space_file("photo.png" , "eng")
        if result["IsErroredOnProcessing"] and "language" in result["ErrorMessage"][0]:
            await event.edit("**• Language Not Found!**")
        elif result["ParsedResults"][0]["ParsedText"]:
            await event.edit(f'''**• Result :** \n `{result["ParsedResults"][0]["ParsedText"]}` \n\n __🧾 From OcrApi!__''')
        elif not result["ParsedResults"][0]["ParsedText"]:
            await event.edit("**• Result Is Empty!**")
        elif result["IsErroredOnProcessing"]:
            await event.edit(f'''**• Error :** `{result["ErrorMessage"]}`''')
    else:
        await event.edit("**• Please Reply To Photo!**)
