from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.ocrlangs$"))
async def OcrApiLangs(event):
    await event.edit("`• Please Wait ...`")
    await app.send_file(event.chat_id , "userbot/other/ocrlangs.jpg" , caption="**• OcrApi Available Languages!**")
    await event.delete()
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.ocr ?(\S*)?$"))
async def OcrApi(event):
    await event.edit("`• Please Wait ...`")
    if event.pattern_match.group(1):
        lang = str(event.pattern_match.group(1))
    else:
        lang = "eng"
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.media.photo:
        media = reply.media
        await app.download_media(media , "ocrinput.jpg")
        result = ocr_space_file("ocrinput.jpg" , lang)
        try:
            text = result["ParsedResults"][0]["ParsedText"]
            await event.edit(f'''**• Result :** \n `{text}` \n\n 🧾**From OcrApi!**''')
        except Exception as e:
            await event.edit(f'''**• Error :** `{e}`''')
        os.remove("ocrinput.jpg")
    else:
        await event.edit("**• Please Reply To Photo!**")
