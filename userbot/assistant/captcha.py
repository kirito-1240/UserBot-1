from userbot import app, bot
from userbot.database import DB
from userbot.utils import shuffle
from telethon import events, Button 
from userbot.functions.captcha import Captcha
import re
import os
import shutil
import glob
import asyncio
import string
import random

@app.on(events.ChatAction)
async def captcha(event):
    user = await event.get_user()
    chat = await event.get_chat()
    if not (event.user_joined or event.user_added) or user.bot:
        return

@bot.on(events.InlineQuery(pattern=re.compile("^alien$")))
async def send_captcha(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    try:
        await bot.edit_permissions(chat.id, user.id, send_messages=False)
    except:
        return
    cap = Captcha()
    buttons = []
    for ans in cap['answer']:
        buttons.append(Button.inline(ans, data=f"captcha||truesemojies||{ans}||{user.id}||{len(cap['answer'])}"))
    for i in range(0,(16 - len(cap['answer']))):
        ans = random.choice(cap['others'])
        buttons.append(Button.inline(ans, data=f"captcha||falseemojies||{ans}||{user.id}||{len(cap['answer'])}"))
    buttons = shuffle(buttons)
    buttons = (buttons[::4], buttons[1::4], buttons[2::4], buttons[3::4])
    await event.reply(f"**• Hello {user.first_name}**\n\n**• Please Select The Correct Options:**", file=cap['captcha'], buttons=buttons)


@bot.on(events.CallbackQuery(data=re.compile("captcha\|\|(.*)\|\|(.*)\|\|(.*)\|\|(.*)")))
async def call_captcha(event):
    type = str((event.pattern_match.group(1)).decode('utf-8'))
    ans = str((event.pattern_match.group(2)).decode('utf-8'))
    user_id = int((event.pattern_match.group(3)).decode('utf-8'))
    ran = int((event.pattern_match.group(4)).decode('utf-8'))
    if event.sender_id != user_id:
        return await event.answer("• This Is Not For You 😠")
    msg = await app.get_messages(event.chat_id, ids=int(event.original_update.msg_id))
    buttons = msg.buttons
    if msg.text.endswith("Options:**"):
        msg.text += "\n\n**• Your Answers:** "
    datas = ""
    if type == "truesemojies":
        trues = 0
        for mes in msg.text:
            if mes == "✅":
                trues += 1
        i = 0
        for butts in buttons:
            x = 0
            for but in butts:
                if str(but.text) == ans:
                    buttons[i][x] = Button.inline("✅", data="emojiempty")
                x += 1
            i += 1
        await bot.edit_message(event.chat_id, int(event.original_update.msg_id), msg.text + "✅", buttons=buttons)
        if (trues + 1) == ran:
            await bot.edit_permissions(event.chat_id, user_id, send_messages=True)
            await event.answer("• Succesfuly Verified!", alert=True)
            await event.delete()
    else:
        warns = 0
        for mes in msg.text:
            if mes == "❌":
                warns += 1
        i = 0
        for butts in buttons:
            x = 0
            for but in butts:
                if str(but.text) == ans:
                    buttons[i][x] = Button.inline("❌", data="emojiempty")
                x += 1
            i += 1
        await bot.edit_message(event.chat_id, int(event.original_update.msg_id), msg.text + "❌", buttons=buttons)
        if (warns + 1) > 4:
            await event.answer("• The Option Is Not Correct, You Are Kicked!", alert=True)
            await asyncio.sleep(2)
            msg = await bot.kick_participant(event.chat_id, user_id)
            await msg.delete()
            await event.delete()
        else:
            await event.answer("• The Option Is Not Correct!", alert=True)
