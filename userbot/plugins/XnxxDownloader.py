from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.xnxx ?(240|480|720)? (.*)$"))
async def XnxxDownloader(event):
    await event.edit("`• Please Wait . . .`")
    if event.pattern_match[1]:
        quality = str(event.pattern_match[1])
    else:
        quality = "240"
    link = str(event.pattern_match[2])
    if not re.search("(?i)^https://www.xnxx.com/video-(.*)$" , link):
        await event.edit("**• Your Link Is Invalid!**")
        return
    url , title , thumb , desc = get_xnxx_video(link , quality)
    r = requests.get(url , allow_redirects=True)
    open('xnxxvideo.mp4', 'wb').write(r.content)
    r = requests.get(thumb , allow_redirects=True)
    open('xnxxthumb.jpg', 'wb').write(r.content)
    video = VideoFileClip("xnxxvideo.mp4")
    dur = convert_time(video.duration)
    timer = time.time()
    async def callback(current, total):
        await get_progress(current , total , event , timer , "u")
    await app.send_file(event.chat_id , "xnxxvideo.mp4" , thumb="xnxxthumb.jpg" , progress_callback=callback , caption=f"**• Title:** ( `{title}` )\n**• Description:** ( `{desc}` )\n**• Quality:** ( `{quality}p` )\n**• Duration:** ( `{dur}` )")
    await event.delete()
    os.remove("xnxxvideo.mp4")
    os.remove("xnxxthumb.jpg")
