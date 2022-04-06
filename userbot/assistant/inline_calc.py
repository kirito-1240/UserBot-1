from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.database import DB
import re

buttons = [
        [Button.inline("C", data="calc_C"), Button.inline("⌫", data="calc_⌫")],
        [Button.inline("𝟽", data="calc_𝟽"), Button.inline("𝟾", data="calc_𝟾"), Button.inline("𝟿", data="calc_𝟿"), Button.inline("+", data="calc_+")],
        [Button.inline("𝟺", data="calc_𝟺"), Button.inline("𝟻", data="calc_𝟻"), Button.inline("𝟼", data="calc_𝟼"), Button.inline("-", data="calc_-")],
        [Button.inline("𝟷", data="calc_𝟷"), Button.inline("𝟸", data="calc_𝟸"), Button.inline("𝟹", data="calc_𝟹"), Button.inline("×", data="calc_×")],
        [Button.inline("𝟶𝟶", data="calc_𝟶𝟶"), Button.inline("𝟶", data="calc_𝟶"), Button.inline(".", data="calc_."), Button.inline("÷", data="calc_÷")],
        [Button.inline("=", data="calc_=")],
    ]

@alien_inline("^alien_calc$", owner=True)
async def calc_pattern(event):
    DB.set_key("ALIEN_CALC", "")
    result = event.builder.article(
        title="Alien Calc Menu!",
        text="**• Alien Userbot Calc Menu!**",
        buttons=buttons,
    )
    await event.answer([result])

@alien_callback(re.compile("calc_(.*)"), owner=True)
async def calc_callback(event):
    work = str((event.pattern_match.group(1)).decode('utf-8'))
    if work == "C":
        DB.set_key("ALIEN_CALC", "")
        await event.answer("• Cleared!")
    elif work == "⌫":
        get = DB.get_key("ALIEN_CALC")
        DB.set_key("ALIEN_CALC", get[:-1])
    elif work in ["𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿"]:
        get = DB.get_key("ALIEN_CALC")
        DB.set_key("ALIEN_CALC", str(get) + work)
    elif work in ["𝟶", "𝟶𝟶", ".", "+", "-", "×", "÷"]:
        get = DB.get_key("ALIEN_CALC")
        if not get:
            return await event.answer("• Not Available!")
        DB.set_key("ALIEN_CALC", str(get) + work)
    elif work == "=":
        get = str(DB.get_key("ALIEN_CALC"))
        if not get:
            return await event.answer("• Empty!")
        get = get.replace("𝟶", "0")
        get = get.replace("𝟷", "1")
        get = get.replace("𝟸", "2")
        get = get.replace("𝟹", "3")
        get = get.replace("𝟺", "4")
        get = get.replace("𝟻", "5")
        get = get.replace("𝟼", "6")
        get = get.replace("𝟽", "7")
        get = get.replace("𝟾", "8")
        get = get.replace("𝟿", "9")
        get = get.replace("𝟶𝟶", "00")
        get = get.replace("×", "*")
        get = get.replace("÷", "/")
        try:
            out = eval(get)
            num = round(int(out))
            await event.edit(f"**• Result:** ( `{num}` )", buttons=buttons)
            return DB.set_key("ALIEN_CALC", "")
        except:
            DB.set_key("ALIEN_CALC", "")
            return await event.answer("• Error, Please Try Again!")
    await event.edit(f'**• Your Calc:** ( `{DB.get_key("ALIEN_CALC") or " "}` )', buttons=buttons)
