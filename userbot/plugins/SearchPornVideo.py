from . import *

@app.on_message(filters.me & filters.regex("(?i)^\.spornv (.*)$"))
async def SearchPornVideo(client , event):
    await event.edit_text("`• Please Wait . . .`")
    keyword = str(event.text[8:])
    client = pornhub.PornHub(keyword)
    await event.delete()
    for video in client.getVideos(5):
        caption = f"""
**• Name:** ( `{video['name']}` )
**• Url:** ( [Click Me!]({video['url']}) )
**• Duration:** ( `{video['duration']}` )
**• Rating:** ( `{video['rating']}` )
"""
        await app.send_photo(event.chat.id , video["background"] , caption=caption)
