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
    res = [
            await event.builder.article(
                title="Alien Userbot",
                url="https://t.me/TheUltroid",
                description="• Alien Userbot Inline Help!",
                text=MSG,
                thumb="/userbot/other/bot.jpg",
                buttons=IN_BTTS,
            )
        ]
    await event.answer([res])
