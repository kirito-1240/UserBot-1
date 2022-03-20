from userbot import bot
from telethon import events , Button
from userbot.database.botusers import add_user

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start(event):
    add_user(str(event.from_id.user_id))
    await event.reply(f"**• Hello . . .**\n\n**• Welcome To Best Self Manager Bot 😎**" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
