from userbot import app, bot
import string, random
from userbot.events import alien_callback
from telethon import Button
from telethon import events
import re, os

@app.on(events.ChatAction)
async def send_captcha(event):
    strings = (string.ascii_letters + str(string.digits))
    buttons = []
    user = await event.get_user()
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
    await bot.send_message(event.chat_id, f"Hello {truetext}", buttons=buttons)

@alien_callback(re.compile("(.*)\|\|(.*)"), owner=True)
async def call_captcha(event):
    type = str((event.pattern_match.group(1)).decode('utf-8'))
    user_id = int((event.pattern_match.group(2)).decode('utf-8'))
    if type == "true":
        await event.answer("True")
    else:
        await event.answer("False")
