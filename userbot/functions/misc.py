from userbot import app, bot, LOGS
from telethon import functions
from userbot.database import DB
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
            DB.set_key("LOG_GROUP" , chat.id)
            return x.title
    try:
        result = await app(
            functions.channels.CreateChannelRequest(
                title="⚠️ My Alien Logs ⚠️",
                about="🚫 Please Don`t Delete This Group 🚫",
                megagroup=True,
            )
        )
    except BaseException as er:
        LOGS.error("• Something Went Wrong , Create A Group And Set Its Id On Config Var LOG_GROUP!")
    chat_id = result.chats[0].id
    DB.set_key("LOG_GROUP" , chat_id)
