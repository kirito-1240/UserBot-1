from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.nex1 ?(64|128|320)? (.*)$"))
async def Nex1MusicDownloader(event):
    await event.edit("`• Please Wait . . .`")
    if event.pattern_match[1]:
        quality = str(event.pattern_match[1])
    else:
        quality = "128"
    link = str(event.pattern_match[2])
    if not re.search("(?i)^https://m.nex1music.ir/(.*)$" , link):
        await event.edit("**• Your Link Is Invalid!**")
        return
    url , title , thumb , desc , uploadDate = get_nex1music(link , quality)
    timer = time.time()
    async def callback(current, total):
        await get_progress(current , total , event , timer , "u")
    await app.send_file(event.chat_id , url , progress_callback=callback , caption=f"**• Title:** ( `{title}` )\n**• Description:** ( `{desc}` )\n**• Quality:** ( `{quality}p` )\n**• Upload Date:** ( `{uploadDate}` )")
    await event.delete()
