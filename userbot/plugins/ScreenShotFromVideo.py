from userbot import app
from telethon import events
from moviepy.editor import VideoFileClip
import os , random , time
from userbot.utils import take_screen_shot , convert_bytes
from moviepy.editor import VideoFileClip
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.scrv ?(\d*)?$"))
async def ScreenShotFromVideo(event):
    edit = await event.edit("`Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.document.mime_type == "video/mp4":
        media = reply.media
        speed = "0"
        async def callback(current, total):
            start = current
            await edit.edit(f"""`Downloading ...`\n\n**• Current:** ( `{convert_bytes(current)}` )\n**• Total:** ( `{convert_bytes(total)}` )\n**• Speed:** ( `{convert_bytes(speed)}` )""")
            speed = current
        await app.download_media(media , "screenshotvideo.mp4" , progress_callback=callback)
        await edit.edit("**• Download Completed!**\n`Please Wait For Taking ...`")
        if event.text[5:]:
            time = int(event.text[5:])
            await take_screen_shot("screenshotvideo.mp4" , time , "screenshot.jpg")
            await edit.delete()
            await app.send_file(event.chat_id , "screenshot.jpg" , reply_to=reply.id  , caption=f"**• This Photo Was Taken In** (`{time}`) **From This Video!**")
            os.remove("screenshot.jpg")
            os.remove("screenshotvideo.mp4")
        else:
            list = []
            video = VideoFileClip("screenshotvideo.mp4")
            duration = video.duration
            for i in range(0, 10):
                rand = range(0 , int(duration))
                time = random.choice(rand)
                await take_screen_shot("screenshotvideo.mp4" , time , f"screenshot{i}.jpg")
                list.append(f"screenshot{i}.jpg")
            await edit.delete()
            await app.send_file(event.chat_id , list , reply_to=reply.id  , caption="**• This Photos Was Taken From This Video!**")
            for name in list:
                os.remove(f"{name}")
            os.remove("screenshotvideo.mp4")            
    else:
        await edit.edit("**• Please Reply To Video!**")
