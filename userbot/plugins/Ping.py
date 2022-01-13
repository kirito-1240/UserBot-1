from . import *

@app.on_message(filters.me , filters.regex("(?i)^\.ping$"))
async def Ping(event):
    start = datetime.now()
    edit = await event.edit_text("**Pong!!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = convert_time(time.time() - START_TIME)
    await edit.edit_text(f"**• Pong!!** `{ms}`\n**• Uptime :** `{uptime}`")
