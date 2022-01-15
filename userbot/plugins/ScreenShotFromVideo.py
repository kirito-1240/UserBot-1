from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.scrv ?(\d*)?$"))
async def ScreenShotFromVideo(event):
    await event.edit("`• Please Wait ...`")
    if not event.reply_to == None and reply.document.mime_type == "video/mp4":
        media = reply.media
        await app.download_media(media , "inputscr.mp4")
        await event.edit("**• Download Completed!**\n`Please Wait For Taking Shots ...`")
        if event.text[5:]:
            time = int(event.text[5:])
            await take_screen_shot("inputscr.mp4" , time , "screenshot.jpg")
            await event.delete()
            await app.send_file(event.chat_id , "screenshot.jpg" , reply_to=reply.id , caption=f"**• This Photo Was Taken In** ( `{time}` ) **From This Video!**")
            os.remove("screenshot.jpg")
            os.remove("inputscr.jpg")
        else:
            list = []
            video = VideoFileClip("inputscr.mp4")
            duration = video.duration
            for i in range(0, 10):
                rand = range(0 , int(duration))
                time = random.choice(rand)
                await take_screen_shot("inputscr.mp4" , time , f"screenshot{i}.jpg")
                list.append(f"screenshot{i}.jpg")
            await event.delete()
            await app.send_file(event.chat_id , list , reply_to=reply.id , caption="**• This ScreenShots Takes From This Video!**")
            for name in list:
                os.remove(name)
            os.remove("inputscr.mp4")            
    else:
        await event.edit("**• Please Reply To Video!**")
