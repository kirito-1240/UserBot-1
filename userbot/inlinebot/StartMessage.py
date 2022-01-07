from userbot import bot
from telethon import events , Button

@bot.on(events.NewMessage(incoming=True, pattern="(?i)^/start$"))
async def StartMessage(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("Button Url", url="https://t.me/MrAbolii")],
                        [Button.inline("Inline Button",data="example")]
                    ])

@bot.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You Clicked A Button!")
