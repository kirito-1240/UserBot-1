from userbot import bot
from telethon import events, Button
from userbot.database import DB
import re

buttons = [
        [Button.inline("π", data="calc_R"), Button.inline("C", data="calc_C"), Button.inline("β«", data="calc_β«")],
        [Button.inline("π½", data="calc_π½"), Button.inline("πΎ", data="calc_πΎ"), Button.inline("πΏ", data="calc_πΏ"), Button.inline("+", data="calc_+")],
        [Button.inline("πΊ", data="calc_πΊ"), Button.inline("π»", data="calc_π»"), Button.inline("πΌ", data="calc_πΌ"), Button.inline("-", data="calc_-")],
        [Button.inline("π·", data="calc_π·"), Button.inline("πΈ", data="calc_πΈ"), Button.inline("πΉ", data="calc_πΉ"), Button.inline("Γ", data="calc_Γ")],
        [Button.inline("πΆπΆ", data="calc_πΆπΆ"), Button.inline("πΆ", data="calc_πΆ"), Button.inline(".", data="calc_."), Button.inline("Γ·", data="calc_Γ·")],
        [Button.inline("=", data="calc_=")],
    ]

@bot.on(events.InlineQuery(pattern="^alien_calc$"))
async def calc(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("β’ This Is Not For You!", alert=True) 
    DB.set_key("ALIEN_CALC", "")
    result = event.builder.article(
        title="Alien Calc Menu!",
        text="**β’ Alien Userbot Calc Menu!**",
        buttons=buttons,
    )
    await event.answer([result])

@bot.on(events.CallbackQuery(data=re.compile("calc_(.*)")))
async def calc_captcha(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("β’ This Is Not For You!", alert=True)
    work = str((event.pattern_match.group(1)).decode('utf-8'))
    if work == "C":
        DB.set_key("ALIEN_CALC", "")
        await event.answer("β’ Cleared!")
    elif work == "β«":
        get = DB.get_key("ALIEN_CALC")
        DB.set_key("ALIEN_CALC", get[:-1])
    elif work in ["π·", "πΈ", "πΉ", "πΊ", "π»", "πΌ", "π½", "πΎ", "πΏ"]:
        get = DB.get_key("ALIEN_CALC")
        DB.set_key("ALIEN_CALC", str(get) + work)
    elif work in ["πΆ", "πΆπΆ", ".", "+", "-", "Γ", "Γ·"]:
        get = DB.get_key("ALIEN_CALC")
        if not get:
            return await event.answer("β’ Not Available!")
        DB.set_key("ALIEN_CALC", str(get) + work)
    elif work == "R":
        get = DB.get_key("ALIEN_CALC_RECENT")
        if not get:
            await event.answer("β’ Recents Empty!")
            try:
                return event.edit(f'**β’ Your Calc:** ( `{DB.get_key("ALIEN_CALC") or " "}` )', buttons=buttons)
            except:
                return
        c = 1
        recents = "**β’ Alien Calc Recents:**\n\n"
        for rec in get:
            recents += f"**{c} -** `{rec} = {get[rec]}`\n"
            c += 1
        return await event.edit(recents, buttons=buttons)
    elif work == "=":
        gets = str(DB.get_key("ALIEN_CALC"))
        if not gets:
            return await event.answer("β’ Empty!")
        get = gets.replace("πΆ", "0")
        get = get.replace("π·", "1")
        get = get.replace("πΈ", "2")
        get = get.replace("πΉ", "3")
        get = get.replace("πΊ", "4")
        get = get.replace("π»", "5")
        get = get.replace("πΌ", "6")
        get = get.replace("π½", "7")
        get = get.replace("πΎ", "8")
        get = get.replace("πΏ", "9")
        get = get.replace("πΆπΆ", "00")
        get = get.replace("Γ", "*")
        get = get.replace("Γ·", "/")
        try:
            out = eval(get)
            num = round(int(out))
            await event.edit(f"**β’ Result:** ( `{num}` )", buttons=buttons)
            cal = DB.get_key("ALIEN_CALC_RECENT") or {}
            if int(len(cal)) >= 100:
                DB.del_key("ALIEN_CALC_RECENT")
                cal = {}
            cal.update({gets: num})
            DB.set_key("ALIEN_CALC_RECENT", cal)
            return DB.set_key("ALIEN_CALC", "")
        except:
            DB.set_key("ALIEN_CALC", "")
            return await event.answer("β’ Error, Please Try Again!")
    try:
        await event.edit(f'**β’ Your Calc:** ( `{DB.get_key("ALIEN_CALC") or " "}` )', buttons=buttons)
    except:
        pass
