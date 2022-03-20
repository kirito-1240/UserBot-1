from userbot.utils import load_plugins , AddBot
from pathlib import Path
from telethon import Button
from . import app , bot , LOG
import logging , sys , os
import importlib
import glob

async def setup():
    me = await app.get_me()
    load_plugins("plugins")
    load_plugins("assistant")
    await AddBot()
    if me.username:
        username = "@" + me.username
    else:
        username = f"[{me.first_name}](tg://user?id={me.id})"
    await bot.send_file(LOG , "./userbot/other/bot.jpg" , caption=f"**• UserBot And AssistantBot Has Been Start Now!**\n\n**• You Can User The RoBot:** {username}" , buttons=[[Button.url("• Support •", url="https://t.me/MrAbolii")]])

bot.loop.run_until_complete(setup())

app.run_until_disconnected()
