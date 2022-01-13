from . import *

@app.on_message(filters.me & filters.regex("(?i)^\.ping$"))
async def Ping(client , event):
    start = datetime.now()
    await event.edit_text("**Pong!!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = convert_time(time.time() - START_TIME)
    await event.edit_text(f"**• Pong!!** `{ms}`\n**• Uptime :** `{uptime}`")
