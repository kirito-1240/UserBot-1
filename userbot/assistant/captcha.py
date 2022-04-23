from userbot import app, bot
import string, random
from userbot.database import DB
from userbot.events import alien_callback
from telethon import Button
from telethon import events
import re, os
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
    buttons.append(Button.inline(truetext, data=f"true||{user.id}"))
    for i in range(11):
        falsetext = ""
        for x in range(6):
            falsetext += random.choice(strings)
        buttons.append(Button.inline(falsetext, data=f"false||{user.id}"))
    buttons = (buttons[::4], buttons[1::4], buttons[2::4], buttons[3::4])
    fonts = ["userbot/other/fonts/font14.ttf", "userbot/other/fonts/font16.ttf", "userbot/other/fonts/font15.ttf", "userbot/other/fonts/font19.ttf"]
    image = ImageCaptcha(fonts=fonts)
    image.write(truetext, f"captcha{event.chat_id}{user.id}.png")
    await bot.send_message(event.chat_id, f"Hello {user.first_name}", file=f"captcha{event.chat_id}{user.id}.png", buttons=buttons)

@alien_callback(re.compile("(.*)\|\|(.*)"), owner=True)
async def call_captcha(event):
    type = str((event.pattern_match.group(1)).decode('utf-8'))
    user_id = int((event.pattern_match.group(2)).decode('utf-8'))
    if type == "true":
        await event.answer("True", alert=True)
        await bot.edit_permissions(chat.id, user.id, send_messages=True)
    else:
        await event.answer("False", alert=True)
        await bot.kick_participant(event.chat_id, user_id)
