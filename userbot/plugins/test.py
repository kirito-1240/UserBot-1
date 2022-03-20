from . import *
from userbot.database import set_key , get_key

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.test$"))
async def ls(event):
    await event.edit("`• Please Wait ...`")
    key = "ANTIFLOOD"
    value = event.chat_id
    set_key(str(key) , str(value))
    g = get_key(str(key))
    await event.edit(str(g))
