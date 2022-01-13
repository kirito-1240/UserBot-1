from . import *

@app.on_message(filters.me & filters.regex("(?i)^\.scrv ?(\d*)?$"))
async def ScreenShotFromVideo(client , event):
    await event.edit_text("`• Please Wait ...`")
    if event.reply_to_message and event.reply_to_message.video:
        media = event.reply_to_message.video
        media = await app.download_media(media)
        await event.edit_text("**• Download Completed!**\n`Please Wait For Taking ...`")
        if event.text[5:]:
            time = int(event.text[5:])
            take_screen_shot(media , time , "screenshot.jpg")
            await event.delete()
            await app.send_photo(event.chat.id , "screenshot.jpg" , reply_to_message_id=event.reply_to_message.message_id  , caption=f"**• This Photo Was Taken In** ( `{time}` ) **From This Video!**")
            os.remove("screenshot.jpg")
            os.remove(media)
        else:
            list = []
            video = VideoFileClip(media)
            duration = video.duration
            for i in range(0, 10):
                rand = range(0 , int(duration))
                time = random.choice(rand)
                take_screen_shot(media , time , f"screenshot{i}.jpg")
                list.append(f"screenshot{i}.jpg")
            await event.delete()
            list2 = []
            for name in list:
                list2.append(InputMediaPhoto(name))
            await app.send_media_group(event.chat.id , list2 , reply_to_message_id=event.reply_to_message.message_id  , caption="**• This Photos Was Taken From This Video!**")
            for name in list:
                os.remove(f"{name}")
            os.remove(media)            
    else:
        await event.edit("**• Please Reply To Video!**")
