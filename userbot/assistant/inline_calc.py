from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.database import DB
import re

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
    "×",
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
    result = event.builder.article(
        title="Alien Calc Menu!",
        text="**• Alien Userbot Calc Menu!**",
        buttons=buttons,
    )
    await event.answer([result])

@alien_callback(re.compile("calc(.*)"), owner=True)
async def calc_callback(event):
    work = str((event.pattern_match.group(1)).decode('utf-8'))
    if work in ["AC", "C"]:
        DB.set_key("ALIEN_CALC", "")
        return await event.answer("• Cleared!")
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
        try:
            out = eval(get)
            num = round(int(out))
            return await event.answer(f"• Result: ( {num} )")
        except:
            DB.set_key("ALIEN_CALC", "")
            return await event.answer("• Error, Please Try Again!")
    await event.answer("• Calc:  " + str(DB.get_key("ALIEN_CALC")))
