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

@bot.on(events.ChatAction)
async def send_captcha(event):
    user = await event.get_user()
    chat = await event.get_chat()
    if not (event.user_joined or event.user_added) or user.bot:
        return
    try:
        await bot.edit_permissions(chat.id, user.id, send_messages=False)
    except:
        return
    cap = Captcha()
    buttons = []
    for ans in cap['answer']:
        buttons.append(Button.inline(ans, data=f"captcha||true||{ans}||{user.id}"))
    for i in range(0,8):
        ans = random.choice(cap['others'])
        buttons.append(Button.inline(ans, data=f"captcha||false||{ans}||{user.id}"))
    buttons = shuffle(buttons)
    buttons = (buttons[::4], buttons[1::4], buttons[2::4], buttons[3::4])
    await event.reply(f"**• Hello {user.first_name}**\n\n**• Please Select The Correct Options:**", file=cap['captcha'], buttons=buttons)

@bot.on(events.CallbackQuery(data=re.compile("captcha\|\|(.*)\|\|(.*)\|\|(.*)")))
async def call_captcha(event):
    type = str((event.pattern_match.group(1)).decode('utf-8'))
    ans = str((event.pattern_match.group(2)).decode('utf-8'))
    user_id = int((event.pattern_match.group(3)).decode('utf-8'))
    if event.sender_id != user_id:
        return await event.answer("• This Is Not For You 😠")
    print(event.original_update.msg_id)
    print(event.text)
    if type == "true":
        await bot.edit_permissions(event.chat_id, user_id, send_messages=True)
        await event.delete()
    else:
        await event.answer("• The Option Is Not Correct, You Are Kicked!", alert=True)
        await asyncio.sleep(2)
        await bot.kick_participant(event.chat_id, user_id)
    shutil.rmtree("cache")
