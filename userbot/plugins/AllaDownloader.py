from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.alla (.*)$"))
async def AllaDownloader(event):
    await event.edit("`• Please Wait . . .`")
    link = str(event.pattern_match.group(1))
    if not re.search("(?i)^https://alaatv.com/c/(\d*)$" , link):
        await event.edit("**• Your Link Is Invalid!**")
        return
    url , title , thumb , desc = get_alla_video(link , "480")
    r = requests.get(url , allow_redirects=True)
    open('allavideo.mp4', 'wb').write(r.content)
    r = requests.get(thumb , allow_redirects=True)
    open('allathumb.jpg', 'wb').write(r.content)
    await app.send_file(chat_id , "allavideo.mp4" , thumb="allathumb.jpg" , caption=f"**• Title:** ( `{title}` )\n**• Description:** ( `{desc}` )")
    os.remove("allavideo.mp4")
    os.remove("allathumb.jpg")
