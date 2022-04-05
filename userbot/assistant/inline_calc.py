from userbot.events import alien_inline, alien_callback
from telethon import Button
import re

CALC = None

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
    CALC = None
    text = f"""
**• Alien Userbot Calc Menu!**

**• Your Calc:** ( `{CALC  or "Empty"}` )
"""
    result = event.builder.article(
        title="Alien Calc Menu!",
        text=text,
        buttons=buttons,
    )
    await event.answer([result])

@alien_callback(re.compile("calc(.*)"), owner=True)
async def calc_callback(event):
    work = str((event.pattern_match.group(1)).decode('utf-8'))
    if work == "AC":
        CALC = None
    elif work == "C":
        CALC = None
    elif work == "⌫":
        CALC = CALC[:-1]
    elif work == "+":
        CALC += "+"
    elif work == "-":
        CALC += "-"
    elif work == "÷":
        CALC += "/"
    elif work == "x":
        CALC += "*"
    elif work == "%":
        CALC += "/100"
    elif work == "=":
        if CALC.endswith(("*", ".", "/", "-", "+")):
            CALC = CALC[:-1]
        out = eval(CALC)
        num = float(out)
        text = f"""
**• Alien Userbot Calc Menu!**

**• Result:** ( `{num}` )
"""
        return await event.edit(text, buttons=buttons)
    text = f"""
**• Alien Userbot Calc Menu!**

**• Your Calc:** ( `{CALC or "Empty"}` )
"""
    await event.edit(text, buttons=buttons)
