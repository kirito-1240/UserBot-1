from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.database import DB
import os, glob, re, random, time
import Config 

@alien_inline("alien_calc", owner=True)
async def help(event):
    DB.set_key("ALIEN_CALC", "")
    vars = [
    "AC",
    "C",
    "⌫",
    "%",
    "7",
    "8",
    "9",
    "+",
    "4",
    "5",
    "6",
    "-",
    "1",
    "2",
    "3",
    "x",
    "00",
    "0",
    ".",
    "÷",
]
    button = [Button.inline(f"{x}", data=f"calc_{x}") for x in vars]
    buttons = list(zip(button[::4], button[1::4], button[2::4], button[3::4]))
    buttons.append([Button.inline("=", data="calc=")])
    text = f"""
**• Alien Userbot Calc Menu!**

Your Calc:  ( `{DB.get_key("ALIEN_CALC")}` )
"""
    result = event.builder.article(
        title="Alien Calc Menu!",
        text=text,
        buttons=buttons,
    )
    await event.answer([result])
