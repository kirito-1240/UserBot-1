from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.cinfo ?(.*)?$"))
async def start(event):
    await event.edit("`• Please Wait . . .`")
    try:
        if event.pattern_match.group(1):
            chat = await app.get_entity(event.pattern_match.group(1))
        else:
            chat = await event.get_chat()
    except ValueError:
        return await event.edit("**• Your Input Chat/Channel Id Invalid!**")
    result = await get_chat_info(chat)
    await event.edit(str(result))
