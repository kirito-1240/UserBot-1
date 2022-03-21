from userbot import bot
from telethon import events , Button
from userbot.database.botusers import add_user

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start(event):
    add_user(event.peer_id.user_id)
    info = await bot.get_entity(event.peer_id.user_id)
    await event.reply(f"""
**• Hello {info.first_name} 👋**
**• Welcome To The Best Self Manager Bot 😎**

__• Thanks For Using . . .__
"""
, buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
