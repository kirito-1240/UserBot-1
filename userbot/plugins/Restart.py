from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    one = "█"
    two = "░"
    for i in range(0 , 8):
        c = 7 - int(i)
        await event.edit(f"""`• Restarting - [ {one*i}{two*c} ]`""")      
    await event.edit("**• Bot Restarted!**")
    restart_app()
    await bash("git pull && pip3 install -r requirements.txt")
    os.execl(sys.executable, sys.executable, "-m", "userbot")

