from userbot import app, bot
from userbot.core.logger import LOGS
from telethon import functions
from telethon.tl.functions.channels import InviteToChannelRequest, EditPhotoRequest
from telethon.tl.types import InputChatUploadedPhoto, ChatPhotoEmpty
from userbot.database import DB
from userbot.functions.tools import download_file
import os, sys, asyncio

async def add_to_db():
    app_info = await app.get_me()
    bot_info = await bot.get_me()
    DB.set_key("OWNER" , f"[{app_info.first_name}](tg://user?id={app_info.id})")
    DB.set_key("OWNER_ID" , app_info.id)
    DB.set_key("OWNER_NAME" , app_info.first_name)
    if app_info.username:
        DB.set_key("OWNER_USERNAME" , app_info.username)
    DB.set_key("ASSISTANT_ID" , bot_info.id)
    DB.set_key("ASSISTANT_NAME" , bot_info.first_name)
    DB.set_key("ASSISTANT_USERNAME" , bot_info.username)
    DB.set_key("LOG_GROUP_PIC" , "https://telegra.ph/file/494ecda6ce2914d4816f9.jpg")
    DB.set_key("ASSISTANT_BOT_PIC" , "https://telegra.ph/file/63e58861cdf1d0718302d.jpg")
    DB.set_key("ALIVE_PIC" , "http://telegra.ph/file/e6e67226e79006c7fef4e.jpg")
    DB.set_key("START_PIC" , ["http://telegra.ph/file/902d092d69cde6a321c63.jpg", "http://telegra.ph/file/cfbf683e05bfd9fc4aa4e.jpg", "http://telegra.ph/file/f770f457e78b3af2fbd6a.jpg", "http://telegra.ph/file/2d3ea8948c4995b7e60aa.jpg", "https://telegra.ph/file/9f679f8e9ac417f2b8bd9.jpg", "http://telegra.ph/file/181078c24eda9f550a063.jpg"])
    DB.set_key("INLINE_PIC" , ["http://telegra.ph/file/902d092d69cde6a321c63.jpg", "http://telegra.ph/file/cfbf683e05bfd9fc4aa4e.jpg", "http://telegra.ph/file/f770f457e78b3af2fbd6a.jpg", "http://telegra.ph/file/2d3ea8948c4995b7e60aa.jpg", "https://telegra.ph/file/9f679f8e9ac417f2b8bd9.jpg", "http://telegra.ph/file/181078c24eda9f550a063.jpg"])

async def check_log_group():
    async for chat in app.iter_dialogs():
        if chat.title == "⚠️ My Alien Logs ⚠️":
            return chat.id
    return False

async def add_log_group():
    check = await check_log_group()
    if check is not False:
        chat_id = check
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
            return logs.error("• something went wrong , create a group and set its id on config var log_group!")    
        chat_id = result.chats[0].id
    info = await app.get_entity(chat_id)
    if info.username:
        username = info.username
    else:
        try:
            username = "Alien_" + str(DB.get_key("OWNER_ID")) + "_Logs"
            await app(functions.channels.UpdateUsernameRequest(chat_id , username))
        except:
            return LOGS.error("• Something Went Wrong , Create A Group And Set Its Id On Config Var LOG_GROUP!")
    DB.set_key("LOG_GROUP" , str(username))
    try:
        if isinstance(info.photo, ChatPhotoEmpty):
            photo = await download_file(DB.get_key("LOG_GROUP_PIC"), "LOG_GROUP_PIC.jpg")
            photo = await app.upload_file(photo)
            await app(EditPhotoRequest(chat_id, InputChatUploadedPhoto(photo)))
            os.remove(photo)
    except:
        return LOGS.error("• Something Went Wrong , Create A Group And Set Its Id On Config Var LOG_GROUP!")

async def add_asst_bot():
    me = await bot.get_me()
    try:
        await app(InviteToChannelRequest(DB.get_key("LOG_GROUP"), [me.username]))
    except Exception as er:
            LOGS.error("• Error while Adding Assistant to Log Group!")
