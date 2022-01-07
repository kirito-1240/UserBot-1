from inlinebot import bot
from inlinebot.utils import load_plugins
from telethon import events
import sys , os

@bot.on(events.NewMessage(pattern="(?i)^\.restart$"))
async def start(event):
    event = await event.reply("` Restarting - [ ░░░ ]`")      
    await event.edit("`Restarting - [ █░░ ]`")
    os.execl(sys.executable, sys.executable, *sys.argv)
    await event.edit("`Restarting - [ ██░ ]`")
    quit()
    await event.edit("`Restarting - [ ███ ]`")
    path = "inlinebot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))
    await event.edit("**• Bot Restarted!**")
    await bot.disconnect()
