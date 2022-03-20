from . import bot
from telethon import events

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start_Assistant(event):
    await event.reply("**Hi!**")
