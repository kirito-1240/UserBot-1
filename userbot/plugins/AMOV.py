from userbot import app
from telethon import events
from moviepy.editor import VideoFileClip
import os

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.smfv$"))
async def start(event):
    edit = await event.edit("`Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.document.mime_type == "audio/mpeg":
        media = reply.media
        await app.download_media(media , "smfv.mp3")
        await edit.edit("**• Music Was Set For Added To Videos!**")
    else:
        await edit.edit("**• Please Reply To Music!**")
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.amov$"))
async def start(event):
    edit = await event.edit("`Please Wait ...`")
    reply = await event.get_reply_message()
    if os.path.exists("smfv.mp3"):
        if not event.reply_to == None and reply.document.mime_type == "audio/mpeg":
            media = reply.media
            await app.download_media(media , "amov.mp4")
            audio = mp.AudioFileClip("smfv.mp3")
            video = mp.VideoFileClip("amov.mp4")
            final = video.set_audio(audio)
            final.write_videofile("newamov.mp4") 
            await edit.delete()
            await app.send_file(event.chat_id , "newamov.mp4" , reply_to=reply.id , voice_note=True , caption="**• Deleted Music From Video!**")
            os.remove("amov.mp4")
            os.remove("newamov.mp4")
        else:
            await edit.edit("**• Please Reply To Video!**") 
    else:       
            await edit.edit("**• Please Set Music By Command :** `.smfv`") 
