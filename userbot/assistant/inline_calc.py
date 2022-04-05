from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.database import DB
import re

DB.get_key("ALIEN_CALC")

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
button = [Button.inline(f"{var}", data=f"calc{var}") for var in vars]
buttons = list(zip(button[::4], button[1::4], button[2::4], button[3::4]))
buttons.append([Button.inline("=", data="calc=")])

@alien_inline("^alien_calc$", owner=True)
async def calc_pattern(event):
    DB.set_key("ALIEN_CALC", "")
    text = f'**• Alien Userbot Calc Menu!**\n\n**• Your Calc:** ( `{DB.get_key("ALIEN_CALC")  or "Empty"}` )'
    result = event.builder.article(
        title="Alien Calc Menu!",
        text=text,
        buttons=buttons,
    )
    await event.answer([result])

@alien_callback(re.compile("calc(.*)"), owner=True)
async def calc_callback(event):
    work = str((event.pattern_match.group(1)).decode('utf-8'))
    if work in ["AC", "C"]:
        DB.set_key("ALIEN_CALC", "")
        await event.answer("• Cleared!")
    elif work == "⌫":
        get = DB.get_key("ALIEN_CALC")
        DB.set_key("ALIEN_CALC", get[:-1])
    elif work in ["+", "-", "×", "÷", ".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "00"]:
        get = DB.get_key("ALIEN_CALC")
        DB.set_key("ALIEN_CALC", str(get) + work)
    elif work == "=":
        get = DB.get_key("ALIEN_CALC")
        get = get.replace("×", "*")
        get = get.replace("÷", "/")
        if not get:
            return await event.answer("• Empty!")
        out = eval(get)
        num = float(out)
        return await event.edit(f"**• Alien Userbot Calc Menu!**\n\n**• Result:** ( `{num}` )", buttons=buttons)
    await event.edit(f'**• Alien Userbot Calc Menu!**\n\n**• Your Calc:** ( `{DB.get_key("ALIEN_CALC") or "Empty"}` )', buttons=buttons)
