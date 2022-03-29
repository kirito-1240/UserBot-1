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
    DB.set_key("LOG_GROUP_PIC" , "https://telegra.ph/file/2f8b7ebf0f96101401871.png")
    DB.set_key("ASSISTANT_BOT_PIC" , "https://telegra.ph/file/0f244e71347abcad19e14.png")

async def add_log_group():
    async for chat in app.iter_dialogs():
        if chat.title == "⚠️ My Alien Logs ⚠️":
            DB.set_key("LOG_GROUP" , str(chat.id).replace("-100", ""))
            return chat.title
    try:
        result = await app(
            functions.channels.CreateChannelRequest(
                title="⚠️ My Alien Logs ⚠️",
                about="🚫 Please Don`t Delete This Group 🚫",
                megagroup=True,
            )
        )
        chat_id = result.chats[0].id
        DB.set_key("LOG_GROUP" , str(chat_id).replace("-100", ""))
    except:
        LOGS.error("• Something Went Wrong , Create A Group And Set Its Id On Config Var LOG_GROUP!")
    chat = await app.get_entity(chat_id)
    if isinstance(chat.photo, ChatPhotoEmpty):
        photo = await download_file(DB.get_key("LOG_GROUP_PIC"), "LOG_GROUP_PIC.jpg")
        photo = await app.upload_file(photo)
        await app(EditPhotoRequest(chat_id, InputChatUploadedPhoto(photo)))
        os.remove(photo)
