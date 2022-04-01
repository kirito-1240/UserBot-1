from userbot import app, bot
from telethon import events, Button
from userbot.database import DB

async def new_join(event):
    user = await event.get_user()
    chat = await event.get_chat()
    if not (user and user.is_self):
        return
    if chat.username:
        chat = chat.username
    else:
        chat = f"[{chat.title}](https://t.me/c/{chat.id})"
    type = "bot" if event.client._bot else "user"
    buttons = [Button.inline("• Leave Chat •", data=f"leave_{type}_{event.chat_id}")]
    if event.user_added:
        tmp = event.added_by
        text = f"#ADD_LOG\n\n{tmp} just added {user} to {chat}."
    elif event.from_request:
        text = f"#APPROVAL_LOG\n\n{user} just got Chat Join Approval to {chat}."
    else:
        text = f"#JOIN_LOG\n\n{user} just joined {chat}."
    await bot.send_message(DB.get_key("LOG_GROUP"), text, buttons=buttons)

app.add_event_handler(new_join, events.ChatAction(func=lambda x: x.user_added or x.user_joined),)
bot.add_event_handler(new_join, events.ChatAction(func=lambda x: x.user_added))

@alien_callback(re.compile("leave_(.*)_(.*)"), owner=True)
async def leave_chat(event):
    type = str(event.data_match.group(1).decode("utf-8"))
    chat_id = int(event.data_match.group(2).decode("utf-8"))
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
