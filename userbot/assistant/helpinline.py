from . import *

@bot.on(events.InlineQuery(pattern="userbot_help"))
async def inline_handler(event):
    plugins = int(len(glob.glob("userbot/plugins/*.py"))) - 1
    list = glob.glob("userbot/plugins/*.py")
    list.remove("/userbot/plugins/__init__.py")
    list = chunks(list , 10)
    buttons = create_buttons(list)
    await event.answer([event.builder.article(
        title="• UserBot Help •",
        text=f"**• Welcome To Help Main Menu!**\n\n**• Total Plugins: ( {plugins} )**\n\n**• Page: ( 1 )**",
        buttons=buttons,
    )])

def create_buttons(items):
    buttons = []
    list1 = []
    list2 = []
    for item in items:
        list.append([[Button.inline(f"""Audio 🎵 {humanbytes(item['filesize'])}""",
                                     data=f"a||{item['from_id']}||{item['format_id']}||{item['yturl']}"))
        if len(list) == 2:
            buttons.append([list[0] , list[1]])
            list = []
    if len(list) > 0:
        buttons.append([list[0]])          
    return buttons
