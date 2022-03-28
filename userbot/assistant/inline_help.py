from userbot.events import alien_inline
from telethon import Button

MSG = """
**Alien - UserBot**
➖➖➖➖➖➖➖➖➖➖
**Support**: @MxAboli
➖➖➖➖➖➖➖➖➖➖
"""

IN_BTTS = [
    [
        Button.url("• Support• ", url="https://t.me/MxAboli"),
    ]
]


@alien_inline(pattern="inline_help")
async def inline_help(event):
    result = await event.builder.photo(
            file="userbot/other/bot.jpg",
            text=MSG,
            buttons=IN_BTTS,
        )
    await event.answer([result])
