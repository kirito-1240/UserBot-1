from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.cvideo (\d*) (\d*)$"))
async def CutVideo(event):
    await event.edit("`• Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.document.mime_type == "video/mp4":
        media = reply.media
        async def callback(current, total):
            await event.edit(f"""`Downloading ...`\n\n**• Current Size:** ( `{convert_bytes(current)}` )\n**• Total Size:** ( `{convert_bytes(total)}` )""")
        await app.download_media(media , "cutvideo.mp4" , progress_callback=callback)
        await event.edit("**• Download Completed!**\n`Please Wait For Cuting ...`")
        time1 = event.text.split(" ")[1]
        time2 = event.text.split(" ")[2]
        await runcmd(f"ffmpeg -i cutvideo.mp4 -ss {time1} -to {time2} -async 1 cutvideooutput.mp4")
        await event.delete()
        await app.send_file(event.chat_id , "cutvideooutput.mp4" , reply_to=reply.id  , caption="**• This ShortVideo Was Cuted From This Video!**")
        os.remove("cutvideooutput.mp4")
        os.remove("cutvideo.mp4")
    else:
        await event.edit("**• Please Reply To Music!**")
