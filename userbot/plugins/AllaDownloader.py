from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.alla (.*) ?(240|480|720)?$"))
async def AllaDownloader(event):
    await event.edit("`• Please Wait . . .`")
    if event.pattern_match.group(2):
        format = str(event.pattern_match.group(2))
    else:
        format = "480"
    link = str(event.pattern_match.group(1))
    if not re.search("(?i)^https://alaatv.com/c/(\d*)$" , link):
        await event.edit("**• Your Link Is Invalid!**")
        return
    url , title , thumb , desc = get_alla_video(link , format)
    r = requests.get(url , allow_redirects=True)
    open('allavideo.mp4', 'wb').write(r.content)
    r = requests.get(thumb , allow_redirects=True)
    open('allathumb.jpg', 'wb').write(r.content)
    video = VideoFileClip("inputscr.mp4")
    dur = convert_time(video.duration)
    await app.send_file(event.chat_id , "allavideo.mp4" , thumb="allathumb.jpg" , caption=f"**• Title:** ( `{title}` )\n**• Description:** ( `{desc}` )\n**• Quality:** ( `{format}p` )\n**• Duration:** ( `{dur}` )")
    os.remove("allavideo.mp4")
    os.remove("allathumb.jpg")
