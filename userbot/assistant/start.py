from userbot import bot
from telethon import events , Button
import time
from userbot.database.botusers import add_user

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start(event):
    info = await bot.get_entity(event.peer_id.user_id)
    try:
        add_user(info.id , time.time())
        await event.reply(f"**• Hello {info.first_name} 👋**\n\n**• Welcome To Best Self Manager Bot 😎**" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
    except:
        pass
        
