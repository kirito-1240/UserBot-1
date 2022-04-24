from userbot import app, bot
from telethon import events, Button
from userbot.database import DB
import re

@app.on(events.Raw)
async def new_join(event):
    if match:= re.search("UpdateChannel\((.*)channel_id=(\d*)", str(event)):
        chat = await app.get_entity(int(match[2]))
        user = await app.get_entity("me")
        if chat.username:
            username =  f"[{chat.title}](https://t.me/{chat.username}/{event.action_message.id})"
        else:
            username = f"[{chat.title}](https://t.me/c/{chat.id}/{event.action_message.id})"
        type = "bot" if event.client._bot else "app"
        buttons = [Button.inline("• Leave Chat •", data=f"leavenewjoin_{chat.id}_{type}")]
        text = f"""
**• Hey Master:** ( {DB.get_key("OWNER")} )

**• New Join To The Group/Channel!**

**• Group/Channel Info:**
   **• Title:** ( {chat.title} )
   **• ID:** ( {chat.id} )
   **• Username:** ( {username} )
"""
        await bot.send_message(DB.get_key("LOG_GROUP"), text, buttons=buttons)

@bot.on(events.CallbackQuery(data=re.compile("leavenewjoin_(.*)_(.*)")))
async def leave_chat(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    chat_id = int(event.data_match.group(1).decode("utf-8"))
    type = str(event.data_match.group(2).decode("utf-8"))
    if type == "app":
        info = await app.get_entity(chat_id)
        await app.delete_dialog(chat_id)
        if info.username:
            await event.edit("**• User Bot Successfuly Leaved From:** ( {} )".format(info.username))
        else:
            await event.edit("**• User Bot Successfuly Leaved From:** ( {} )".format(info.title))  
    else:
        info = await bot.get_entity(chat_id)
        await bot.delete_dialog(chat_id)
        if info.username:
            await event.edit("**• Assistant Bot Successfuly Leaved From:** ( {} )".format(info.username))
        else:
            await event.edit("**• Assistant Bot Successfuly Leaved From:** ( {} )".format(info.title))
