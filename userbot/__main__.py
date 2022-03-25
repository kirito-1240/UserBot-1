from userbot.utils import load_plugins, update_envs
from pathlib import Path
from telethon import Button
from . import app , bot , LOG_GROUP , LOGS
from userbot.database import DB
import logging , sys , os
import importlib
import glob

async def setup():
    me = await app.get_me()
    LOGS.info(f"• Connecting To {DB.name} Database . . .")
    if DB.ping():
        LOGS.info(f"• Connected To {DB.name} Database Successfully!")
    LOGS.info("• Starting Added Environments To Database . . .")
    update_envs()
    LOGS.info("• Environments Successfuly Added To Database!")
    LOGS.info("• Starting Setup Plugins . . .")
    load_plugins("plugins")
    load_plugins("assistant")
    LOGS.info("• Setup Plugins Completed!")
    if me.username:
        username = "@" + me.username
    else:
        username = f"[{me.first_name}](tg://user?id={me.id})"
    await bot.send_file(LOG_GROUP , "./userbot/other/bot.jpg" , caption=f"**• UserBot And AssistantBot Has Been Start Now!**\n\n**• You Can Use The Robot:** {username}" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])

bot.loop.run_until_complete(setup())
app.run_until_disconnected()
