from . import *

@bot.on(events.InlineQuery(pattern="help"))
async def inline_handler(event):
    plugins = int(len(glob.glob("userbot/plugins/*.py"))) - 1
    list = glob.glob("userbot/plugins/*.py")
    list.remove("userbot/plugins/__init__.py")
    buttons = list(create_buttons(list))
    await event.answer([event.builder.article(
        title="• UserBot Help •",
        text=f"**• Welcome To Help Main Menu!**\n\n**• Total Plugins: ( {plugins} )**\n\n**• Page: ( 1 )**",
        buttons=buttons,
    )])
