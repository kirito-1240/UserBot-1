from userbot import bot
from telethon import events , Button
from userbot.database.botusers import add_user , get_users

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start(event):
    add_user(event.peer_id.user_id)
    info = await bot.get_entity(event.peer_id.user_id)
    count = len(get_users())
    await event.reply(f"""
**• Hello {info.first_name} 👋**
**• Welcome To Best Self Manager Bot 😎**

**• Your ID:** ( `{info.id}` )
**• Bot Users:** ( `{count}` )
"""
, buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
