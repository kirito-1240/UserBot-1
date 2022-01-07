from userbot import app
from telethon import events
import sys , os

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    one = "█"
    two = "░"
    for i in range(0 , 8):
        c = 7 - int(i)
        await event.edit(f"""`• Restarting - [ {one*i}{two*c} ]`""")      
    await event.edit("**• Bot Restarted!**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
    await app.disconnect()

