from userbot.utils import load_plugins
from userbot.functions.misc import add_to_db
from pathlib import Path
from telethon import Button
from . import app , bot , LOG_GROUP , LOGS
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
    LOGS.info("• Starting Setup Plugins . . .")
    load_plugins("plugins")
    load_plugins("assistant")
    LOGS.info("• Setup Plugins Completed!")
    if DB.get_key("RESTART"):
        edit = DB.get_key("RESTART")
        await app.edit_message(int(edit.split("||")[1]), int(edit.split("||")[0]), "**• Ok, Restart Bot Successfuly!**")
        DB.del_key("RESTART")
    await bot.send_message(LOG_GROUP , f"""**• UserBot And AssistantBot Has Been Start Now!**\n\n**• You Can Use The Robot:** {DB.get_key("OWNER_NAME")}""")
    LOGS.info("• UserBot And AssistantBot Has Been Start Now!")

bot.loop.run_until_complete(setup())
app.run_until_disconnected()
