from userbot import app
from telethon import events
from moviepy.editor import VideoFileClip
import os

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.dafv$"))
async def start(event):
    edit = await event.edit("`Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.document.mime_type == "video/mp4":
        media = reply.media
        await app.download_media(media , "dafv.mp4")
        videoclip = VideoFileClip("dafv.mp4")
        new_clip = videoclip.without_audio()
        new_clip.write_videofile("newdafv.mp4")
        await edit.delete()
        await app.send_file(event.chat_id , "newdafv.mp4" , reply_to=reply.id , voice_note=True , caption="**• Deleted Audio From Video!**")
        os.remove("newdafv.mp4")
        os.remove("dafv.mp4")
    else:
        await edit.edit("**• Please Reply To Video!**")
