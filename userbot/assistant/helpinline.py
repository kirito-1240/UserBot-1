from . import *

@bot.on(events.InlineQuery(pattern="^help$"))
async def inline_handler(event):
    builder = event.builder
    results = builder.article(
        title="Hello!",
        text=f"Click Below To Know More!",
        buttons=Button.inline("Explore", data="explore"),
    )
        await event.answer([results])
