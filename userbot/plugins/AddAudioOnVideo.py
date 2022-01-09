from userbot import app
from telethon import events
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip
import os
from userbot.utils import please_wait         

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.setaudio$"))
async def SetAudioForVideo(event):
    await please_wait(event)
    reply = await event.get_reply_message()
    if (not event.reply_to == None and reply.document.mime_type == "audio/mpeg") or (not event.reply_to == None and reply.document.mime_type == "audio/ogg"):
        media = reply.media
        await app.download_media(media , "smfv.mp3")
        await event.edit("**• Audio Was Set For Added To Videos!**")
    else:
        await event.edit("**• Please Reply To Music!**")
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.addaudio$"))
async def AddAudioOnVideo(event):
    await please_wait(event)
    reply = await event.get_reply_message()
    if os.path.exists("smfv.mp3"):
        if not event.reply_to == None and reply.document.mime_type == "video/mp4":
            media = reply.media
            await app.download_media(media , "amov.mp4")
            audio = AudioFileClip("smfv.mp3")
            video = VideoFileClip("amov.mp4")
            final = video.set_audio(audio)
            final.write_videofile("newamov.mp4") 
            await event.delete()
            await app.send_file(event.chat_id , "newamov.mp4" , reply_to=reply.id , voice_note=True , caption="**• Added Coustom Audio On This Video!**")
            os.remove("amov.mp4")
            os.remove("newamov.mp4")
        else:
            await event.edit("**• Please Reply To Video!**") 
    else:       
            await event.edit("**• Please Set Audio By Command :** `.safv`") 
