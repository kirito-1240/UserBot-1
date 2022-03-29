from userbot import app, bot
from userbot.core.logger import LOGS
from telethon import functions
from telethon.tl.functions.channels import EditPhotoRequest
from telethon.tl.types import InputChatUploadedPhoto, ChatPhotoEmpty
from userbot.database import DB
from userbot.functions.tools import download_file
import os, sys

async def add_to_db():
    app_info = await app.get_me()
    bot_info = await bot.get_me()
    DB.set_key("OWNER_ID" , app_info.id)
    DB.set_key("OWNER_NAME" , app_info.first_name)
    if app_info.username:
        DB.set_key("OWNER_USERNAME" , app_info.username)
    DB.set_key("ASSISTANT_ID" , bot_info.id)
    DB.set_key("ASSISTANT_NAME" , bot_info.first_name)
    DB.set_key("ASSISTANT_USERNAME" , bot_info.username)
    DB.set_key("LOG_GROUP_PIC" , "https://telegra.ph/file/494ecda6ce2914d4816f9.jpg")
    DB.set_key("ASSISTANT_BOT_PIC" , "https://telegra.ph/file/63e58861cdf1d0718302d.jpg")
    DB.set_key("START_PIC" , "https://telegra.ph/file/9f679f8e9ac417f2b8bd9.jpg")

async def add_log_group():
    async for chat in app.iter_dialogs():
        if chat.title == "⚠️ My Alien Logs ⚠️":
            chat_id = chat.id
    else:
        try:
            result = await app(
                    functions.channels.CreateChannelRequest(
                        title="⚠️ My Alien Logs ⚠️",
                        about="🚫 Please Don`t Delete This Group 🚫",
                        megagroup=True,
                    )
                )
        except:
            return LOGS.error("• Something Went Wrong , Create A Group And Set Its Id On Config Var LOG_GROUP!")      
        chat_id = result.chats[0].id
    info = await app.get_entity(chat_id)
    if info.username:
        username = info.username
    else:
        username = "Alien_" + str(DB.get_key("OWNER_ID")) + "_Logs"
        await app(functions.channels.UpdateUsernameRequest(chat_id , username))
    DB.set_key("START_PIC" , str(username))
    if isinstance(info.photo, ChatPhotoEmpty):
        photo = await download_file(DB.get_key("LOG_GROUP_PIC"), "LOG_GROUP_PIC.jpg")
        photo = await app.upload_file(photo)
        await app(EditPhotoRequest(chat_id, InputChatUploadedPhoto(photo)))
        os.remove(photo)
    return username
