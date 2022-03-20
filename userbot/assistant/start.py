from . import *

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start(event):
    await event.reply(f"**• Hello . . .**\n\n**• Welcome To Best Self Manager Bot 😎**" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
