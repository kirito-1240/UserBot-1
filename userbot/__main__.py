from userbot.utils import load_plugins
from userbot.functions.misc import add_to_db, add_log_group
from pathlib import Path
from telethon import Button
from userbot.core.logger import LOGS
from . import app, bot
from userbot.database import DB
from userbot.utils import runcmd
import os, sys
import importlib
import glob

async def setup():
    LOGS.info("• Starting Updating Requirements . . .")
    await runcmd("pip install -r requirements.txt")
    LOGS.info("• Update Requirements Completed!")
    LOGS.info(f"• Connecting To {DB.name} Database . . .")
    if DB.ping():
        LOGS.info(f"• Connected To {DB.name} Database Successfully!")
    else:
        LOGS.error(f"• Connecting To {DB.name} Database Unavailable!")
    LOGS.info("• Starting Added Vars To Database . . .")
    await add_to_db()
    LOGS.info("• Added Vars To Database Completed!")
    LOGS.info("• Creating Log Group . . .")
    username = await add_log_group()
    LOGS.info(f"• Log Group: @{username}")
    LOGS.info("• Create Log Group Completed!")
    LOGS.info("• Starting Setup Plugins . . .")
    load_plugins("plugins")
    load_plugins("assistant")
    LOGS.info("• Setup Plugins Completed!")
    if DB.get_key("RESTART"):
        edit = DB.get_key("RESTART")
        await app.edit_message(int(edit.split("||")[1]), int(edit.split("||")[0]), "**• Ok, Restart Bot Successfuly!**")
        DB.del_key("RESTART")    
    await bot.send_message(DB.get_key("LOG_GROUP"), "**• Alien UserBot Has Been Start Now!**\n\n**• User Mode:** `{}`\n**• Assistant:** @{}".format(DB.get_key("OWNER_NAME"), DB.get_key("ASSISTANT_USERNAME")))
    LOGS.info("• Alien UserBot Has Been Start Now!")

bot.loop.run_until_complete(setup())
app.run_until_disconnected()
