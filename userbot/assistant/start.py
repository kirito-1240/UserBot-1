from userbot import bot
from telethon import Button
from userbot.events import alien_asst
from userbot.database.botusers import add_user
from userbot.database import DB

@alien_asst(pattern="(?i)^\/start$")
async def start(event):
    add_user(event.peer_id.user_id)
    info = await bot.get_entity(event.peer_id.user_id)
    await event.reply(f"""
**• Hello {info.first_name} 👋**
**• Welcome To The Best Self Manager Bot 😎**

__• Thanks For Using . . .__
""")
