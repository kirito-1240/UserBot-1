from . import *

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start_Assistant(event):
    await event.reply(f"**• Hi ( {event.from_user.first_name} )\n\n**• Welcome To Best Self Manager Bot 😎**" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
