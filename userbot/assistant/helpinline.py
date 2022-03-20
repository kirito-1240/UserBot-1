from . import *

@bot.on(events.InlineQuery(pattern="assistant_help"))
async def inline_handler(event):
    plugins = int(len(glob.glob("userbot/plugins/*.py"))) - 1
    await event.answer(event.builder.photo(
        "./userbot/other/bot.jpg",
        title="• UserBot Help •",
        text=f"**• Welcome To Help Main Menu!**\n\n**• Total Plugins: ( {plugins} )**\n\n**• Page: ( 1 )**"
    ))
