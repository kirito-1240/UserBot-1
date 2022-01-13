from . import *

@app.on_message(filters.me & filters.regex("(?i)^\.restart$"))
async def Restart(client , event):
    one = "█"
    two = "░"
    for i in range(0 , 10):
        c = 9 - int(i)
        await event.edit_text(f"""`• Restarting - [ {one*i}{two*c} ]`""")      
    await event.edit_text("**• Bot Restarted!**")
    restart_app()
    await bash("git pull && pip3 install -r requirements.txt")
    await bash("git push -u heroku master")
    os.execl(sys.executable, sys.executable, "-m", "userbot")

