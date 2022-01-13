from . import *
os.system("pip install pornhubapi")
import pornhub

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.spornv (.*)$"))
async def SearchPornVideo(event):
    await event.edit("`• Please Wait . . .`")
    keyword = str(event.pattern_match.group(1))
    client = pornhub.PornHub(keyword)
    await event.delete()
    for video in client.getVideos(5):
        caption = f"""
**• Name:** ( `{video['name']}` )
**• Url:** ( [Click Me!]({video['url']}) )
**• Duration:** ( `{video['duration']}` )
**• Rating:** ( `{video['rating']}` )
"""
        await app.send_file(event.chat_id , video["background"] , caption=caption)
