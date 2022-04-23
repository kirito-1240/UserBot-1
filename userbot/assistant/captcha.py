from userbot import app, bot
import string, random
from userbot.database import DB
from userbot.events import alien_callback
from telethon import Button
from telethon import events
import re, os, glob, asyncio
os.system("pip install captcha")
from captcha.image import ImageCaptcha

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
    strings = (string.ascii_letters + str(string.digits))
    buttons = []
    truetext = ""
    for x in range(6):
        truetext += random.choice(strings)
    buttons.append(Button.inline(truetext, data=f"captcha||true||{user.id}"))
    for i in range(11):
        falsetext = ""
        for x in range(6):
            falsetext += random.choice(strings)
        buttons.append(Button.inline(falsetext, data=f"captcha||false||{user.id}"))
    buttons = random.sample(buttons, len(buttons))
    buttons = (buttons[::4], buttons[1::4], buttons[2::4], buttons[3::4])
    font = random.choice(glob.glob("userbot/other/fonts/*"))
    image = ImageCaptcha(fonts=[font])
    image.write(truetext, f"captcha{event.chat_id}{user.id}.png")
    await event.reply(f"**• Hello {user.first_name}**\n\n**• Please Select The Correct Option:**", file=f"captcha{event.chat_id}{user.id}.png", buttons=buttons)

@bot.on(events.CallbackQuery(data=re.compile("captcha\|\|(.*)\|\|(.*)")))
async def call_captcha(event):
    type = str((event.pattern_match.group(1)).decode('utf-8'))
    user_id = int((event.pattern_match.group(2)).decode('utf-8'))
    if event.sender_id != user_id:
        return await event.answer("• This Is Not For You 😠")
    if type == "true":
        await bot.edit_permissions(event.chat_id, user_id, send_messages=True)
        await event.delete()
    else:
        await event.answer("• The Option Is Not Correct, You Are Kicked!", alert=True)
        await asyncio.sleep(2)
        await bot.kick_participant(event.chat_id, user_id)
