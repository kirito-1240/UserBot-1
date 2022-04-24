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
    chats = DB.get_key("CAPTCHA_CHATS") or []
    if event.chat_id in chats:
        me = await bot.get_me()
        results = await app.inline_query(me.username, f"aliencaptcha_{event.chat_id}_{user.id}")
        await results[0].click(event.chat_id, reply_to=event.action_message.id)
        
@bot.on(events.InlineQuery(pattern=re.compile("aliencaptcha_(.*)_(.*)")))
async def send_captcha(event):
    chat_id = int(event.pattern_match.group(1).replace("-100", ""))
    user_id = int(event.pattern_match.group(2))
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    try:
        await app.edit_permissions(chat_id, user_id, send_messages=False)
    except Exception as e:
        print(f"• Im Not Admin In {event.chat_id}, Captcha Not Working! - Error: ( {e} )")
        return
    cap = Captcha()
    buttons = []
    for ans in cap['answer']:
        buttons.append(Button.inline(ans, data=f"captcha||truesemojies||{ans}||{user_id}||{len(cap['answer'])}"))
    for i in range(0,(20 - len(cap['answer']))):
        ans = random.choice(cap['others'])
        buttons.append(Button.inline(ans, data=f"captcha||falseemojies||{ans}||{user_id}||{len(cap['answer'])}"))
    buttons = shuffle(buttons)
    user = await app.get_entity(user_id)
    buttons = (buttons[::4], buttons[1::4], buttons[2::4], buttons[3::4])
    text = f"**• Hello** {user.mention}\n\n**• Please Select The Correct Options:**"
    result = event.builder.photo(
        file=cap['captcha'],
        text=text,
        buttons=buttons,
    )
    await event.answer([result])

@bot.on(events.CallbackQuery(data=re.compile("captcha\|\|(.*)\|\|(.*)\|\|(.*)\|\|(.*)")))
async def call_captcha(event):
    type = str((event.pattern_match.group(1)).decode('utf-8'))
    ans = str((event.pattern_match.group(2)).decode('utf-8'))
    user_id = int((event.pattern_match.group(3)).decode('utf-8'))
    ran = int((event.pattern_match.group(4)).decode('utf-8'))
    if event.sender_id != user_id:
        return await event.answer("• This Is Not For You 😠", alert=True)
    user = await app.get_entity(user_id)
    msg = await app.get_messages(event.chat_id, ids=int(event.message_id))
    buttons = msg.buttons
    if msg.text.endswith("Options:**"):
        mtext = f"{msg.text}\n\n**• Your Answers:** "
    else:
        mtext = f"{msg.text}"
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
                if str(but.text) == ans and str(but.data.decode('utf-8').split("||")[1]) == "truesemojies":
                    buttons[i][x] = Button.inline("✅", data="emojiempty")
                x += 1
            i += 1
        await event.edit(mtext + "✅", buttons=buttons)
        if (trues + 1) == ran:
            await app.edit_permissions(event.chat_id, user_id, send_messages=True)
            await app.delete_messages(event.chat_id, event.message_id)
            await app.send_message(event.chat_id, f"**• User** {user.mention} **Succesfuly Verified!**", reply_to=event.message_id)
    else:
        warns = 0
        for mes in msg.text:
            if mes == "❌":
                warns += 1
        i = 0
        for butts in buttons:
            x = 0
            for but in butts:
                if str(but.text) == ans and str(but.data.decode('utf-8').split("||")[1]) == "falseemojies":
                    buttons[i][x] = Button.inline("❌", data="emojiempty")
                x += 1
            i += 1
        await event.edit(mtext + "❌", buttons=buttons)
        if (warns + 1) > 4:
            await app.kick_participant(event.chat_id, user_id)
            await app.delete_messages(event.chat_id, event.message_id)
            await app.send_message(event.chat_id, f"**• User** {user.mention} **Not Verified And Kicked!**", reply_to=event.message_id)
