from userbot import bot
import os
os.system("pip install pytz")
import pytz
from telethon import events , Button
import datetime
from userbot.utils import convert_time
from userbot.database.botusers import add_user , info_user , get_users

@bot.on(events.NewMessage(pattern="(?i)^\/start$"))
async def Start(event):
    tz = pytz.timezone('Asia/Tehran')
    now = datetime.datetime.now(tz)
    time = now.strftime("%Y/%m/%d - %H:%M:%S")
    add_user(event.peer_id.user_id , time)
    info = await bot.get_entity(event.peer_id.user_id)
    inf = info_user(info.id)
    count = len(get_users())
    await event.reply(f"""
**• Hello {info.first_name} 👋**

**• Welcome To Best Self Manager Bot 😎**

**• Your ID:** ( `{info.id}` )
**• Join Time:** ( `{inf.date}` )
**• Bot Users:** ( `{count}` )
"""
, buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])
