from userbot.events import alien_inline
from userbot.utils import chunks
from telethon import Button
import os, glob

def create_buttons(items):
    buttons = []
    list = []
    for item in items:
        list.append(Button.inline(f"• {item} •", data=f"help_{item}"))
        if len(list) == 2:
            buttons.append([list[0] , list[1]])
            list = []
    if len(list) > 0:
        buttons.append([list[0]])
    buttons.append([Button.inline("• Close •", data="close_menu")])          
    return buttons

@alien_inline(pattern="alien_inline_help")
async def inline_help(event):
    files = glob.glob("userbot/plugins/*.py")
    plugin_list = []
    for file in sorted(files):
        name = os.path.basename(file).replace(".py" , "")
        plugin_list.append(str(name.title()))
    result = await event.builder.article(
            title="Alien Userbot",
            text="**Alien - UserBot**\n➖➖➖➖➖➖➖➖➖➖\n**Owner**: @MxAboli\n**Assistant**: @ManagerSelfBot\n➖➖➖➖➖➖➖➖➖➖",
            buttons=create_buttons(plugin_list),
        )
    await event.answer([result])
