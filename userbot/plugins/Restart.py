from . import *

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.restart$"))
async def start(event):
    one = "█"
    two = "░"
    for i in range(0 , 10):
        c = 9 - int(i)
        await event.edit(f"""`• Restarting - [ {one*i}{two*c} ]`""")      
    await event.edit("**• Bot Restarted!**")
    await bash("git pull && pip3 install -r requirements.txt")
    await bash("git push -u heroku master")
    os.execl(sys.executable, sys.executable, "-m", "userbot")
    restart_app()

