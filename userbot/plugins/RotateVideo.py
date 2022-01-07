from userbot import app
from telethon import events
from moviepy.editor import VideoFileClip
import os
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.rotate (\d*)$"))
async def RotateVideo(event):
    rotate = int(event.text[7:])
    edit = await event.edit("`Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.document.mime_type == "video/mp4":
        media = reply.media
        await app.download_media(media , "rav.mp4")
        video = VideoFileClip("rav.mp4").rotate(rotate)
        video.write_videofile("newrav.mp4") 
        await edit.delete()
        await app.send_file(event.chat_id , "newrav.mp4" , reply_to=reply.id , voice_note=True , caption=f"**• This Video {rotate}° Rotated!**")
        os.remove("rav.mp4")
        os.remove("newrav.mp4")
    else:
        await edit.edit("**• Please Reply To Video!**")
