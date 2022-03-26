from userbot import app , bot
from telethon import Button
from userbot.events import alien_asst
from userbot.database.botusers import get_users
import os

@alien_aast(pattern="(?i)^\/users$")
async def Start(event):
    id = (await app.get_me()).id
    if event.peer_id.user_id == id:
        count = len(get_users())
        users = ""
        c = 1
        for user in get_users():
            users += f"{c}- `{user}`\n"
            c += 1
        try:
            await event.reply(f"**• Users Count:** ( `{count}` )\n\n{users}")
        except:
            f = open("users.txt" , "w")
            f.write(f"• Users Count: ( {count} )\n\n{users}")
            await event.reply("**• List Of Users!**" , file="users.txt")
            os.remove("users.txt")
