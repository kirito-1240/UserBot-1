from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.xvideo ?(240|480|720)? (.*)$"))
async def XVideosDownloader(event):
    await event.edit("`• Please Wait . . .`")
    if event.pattern_match[1]:
        quality = str(event.pattern_match[1])
    else:
        quality = "240"
    link = str(event.pattern_match[2])
    if not re.search("(?i)^https://www.xvideos.com/video(.*)$" , link):
        await event.edit("**• Your Link Is Invalid!**")
        return
    url , title , thumb , desc , dur = get_xvideos_video(link , quality)
    r = requests.get(thumb , allow_redirects=True)
    open('xvideosthumb.jpg', 'wb').write(r.content)
    r = requests.get(url , allow_redirects=True)
    open('xvideosvideo.mp4', 'wb').write(r.content)
    dur = convert_time(dur)
    timer = time.time()
    async def callback(current, total):
        await get_progress(current , total , event , timer , "u")
    await app.send_file(event.chat_id , url , thumb="xvideosvideo.mp4" , progress_callback=callback , caption=f"**• Title:** ( `{title}` )\n**• Description:** ( `{desc}` )\n**• Quality:** ( `{quality}p` )\n**• Duration:** ( `{dur}` )")
    await event.delete()
    os.remove("xvideosvideo.mp4")
    os.remove("xvideosthumb.jpg")
