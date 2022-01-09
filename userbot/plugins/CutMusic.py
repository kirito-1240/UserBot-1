from userbot import app
from telethon import events
import ffmpeg
from userbot.utils import runcmd , convert_bytes
        
@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.cmusic (\d*) (\d*)$"))
async def CutMusic(event):
    edit = await event.edit("`Please Wait ...`")
    reply = await event.get_reply_message()
    if not event.reply_to == None and reply.document.mime_type == "audio/mpeg":
        media = reply.media
        async def callback(current, total):
            await edit.edit(f"""`Downloading ...`\n\n**• Current Size:** ( `{convert_bytes(current)}` )\n**• Total Size:** ( `{convert_bytes(total)}` )""")
        await app.download_media(media , "cutmusic.mp3" , progress_callback=callback)
        await edit.edit("**• Download Completed!**\n`Please Wait For Cuting ...`")
        time1 = event.text.split(" ")[1]
        time2 = event.text.split(" ")[2]
        await runcmd(f"ffmpeg -i cutmusic.mp3 -ss {time1} -to {time2} -acodec copy cutmusicoutput.mp3")
        await edit.delete()
        await app.send_file(event.chat_id , "cutmusicoutput.mp3" , reply_to=reply.id  , caption="**• This ShortMusic Was Cuted From This Music!**")
        os.remove("cutmusicoutput.mp3")
        os.remove("cutmusic.mp3")
    else:
        await event.edit("**• Please Reply To Music!**")
