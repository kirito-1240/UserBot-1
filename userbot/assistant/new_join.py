from userbot import app, bot
from telethon import events, Button
from userbot.database import DB
from userbot.events import alien_callback
import re

async def new_join(event):
    chat = await event.get_chat()
    user = await event.get_user()
    if not (user and user.is_self):
        return
    if chat.username:
        username =  f"[{chat.title}](https://t.me/{chat.username}/{event.action_message.id})"
    else:
        username = f"[{chat.title}](https://t.me/c/{chat.id}/{event.action_message.id})"
    type = "bot" if event.client._bot else "app"
    buttons = [Button.inline("• Leave Chat •", data=f"leave_{chat.id}_{type}")]
    text = f"""
**• Hey Master:** ( {DB.get_key("OWNER")} )

**• New Join To The Group/Channel!**

**• Group/Channel Info:**
   **• Title:** ( {chat.title} )
   **• ID:** ( {chat.id} )
   **• Username:** ( {username} )
"""
    await bot.send_message(DB.get_key("LOG_GROUP"), text, buttons=buttons)

app.add_event_handler(new_join, events.ChatAction(func=lambda x: x.user_added or x.user_joined),)
bot.add_event_handler(new_join, events.ChatAction(func=lambda x: x.user_added))

@alien_callback(re.compile("leave_(.*)_(.*)"), owner=True)
async def leave_chat(event):
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
