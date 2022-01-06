from userbot import app
from telethon import events
from moviepy.editor import VideoFileClip

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.emfv$"))
async def start(event):
    edit = await event.edit("`Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.document.mime_type == "video/mp4":
        media = reply.media
        await app.download_media(media , "emfv.mp4")
        clip = VideoFileClip("emfv.mp4")
        clip.audio.write_audiofile("output.mp3")
        await edit.delete()
        await app.send_file(event.chat_id , "output.mp3" , caption="**• Extracted Music From Video!**")
        os.remove("output.mp3")
    else:
        await edit.edit("**• Please Reply To Video!**")
