from userbot.utils import load_plugins
from pathlib import Path
from telethon import Button
from . import app , bot , LOG_GROUP , LOGS
from userbot.database import DB
import os, sys
import importlib
import glob

async def setup():
    LOGS.info(f"• Connecting To {DB.name} Database . . .")
    if DB.ping():
        LOGS.info(f"• Connected To {DB.name} Database Successfully!")
    LOGS.info("• Starting Setup Plugins . . .")
    load_plugins("plugins")
    load_plugins("assistant")
    LOGS.info("• Setup Plugins Completed!")
    if DB.get_key("RESTART"):
        edit = DB.get_key("RESTART")
        await app.edit_message(int(edit.split("||")[1]), int(edit.split("||")[0]), "**• Ok, Restart Bot Successfuly!**")
        DB.del_key("RESTART")
    me = await app.get_me()
    if me.username:
        username = "@" + me.username
    else:
        username = f"[{me.first_name}](tg://user?id={me.id})"
    await bot.send_file(LOG_GROUP , "./userbot/other/bot.jpg" , caption=f"**• UserBot And AssistantBot Has Been Start Now!**\n\n**• You Can Use The Robot:** {username}" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])

bot.loop.run_until_complete(setup())
app.run_until_disconnected()
