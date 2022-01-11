from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.cinfo$"))
async def start(event):   
    await event.edit("`• Please Wait . . .")
    end = datetime.now()
    chat = await event.get_chat()
    result = await get_chat_info(chat , event)
    await event.edit(str(result))
