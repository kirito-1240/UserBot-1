from userbot import bot
from telethon import events , Button
from datetime import datetime
from userbot.database.botusers import add_starter_to_db

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start(event):
    try:
        info = await app.get_entity(event.peer_id.user_id)
        if info['username']:
            username = info['username']
        else:
            username = "---"
        add_starter_to_db(info['id'] , info['first_name'] , datetime.now() , username)
        await event.reply(f"**• Hello!**\n\n**• Welcome To Best Self Manager Bot 😎**" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
    except Exception as e:
        print(e)
        
