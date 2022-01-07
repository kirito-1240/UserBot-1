from inlinebot import bot
from telethon import events
import sys , os

@bot.on(events.NewMessage(pattern="(?i)^\.restart$"))
async def start(event):
    event = await event.reply("` Restarting - [ ░░░ ]`")
    await event.edit("`Restarting - [ █░░ ]`")
    await event.edit("`Restarting - [ ██░ ]`")
    await event.edit("`Restarting - [ ███ ]`")
    await event.edit("**• Bot Restarted!**")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
