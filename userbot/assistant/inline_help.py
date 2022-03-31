from userbot.events import alien_inline, alien_callback
from userbot.utils import chunks
from userbot.database import DB
from telethon import Button
import os, glob


@alien_inline("alien_inline_help", owner=True)
async def alien_help(event):
    files = glob.glob("userbot/plugins/*.py")
    text = f"""
**• Alien Userbot Help Menu!**

**• Master:** {DB.get_key("OWNER")}
**• Assistant:** @{DB.get_key("ASSISTANT_USERNAME")}

**• Plugins Count:** ( `{len(files)}` )
"""
    if len(files) > 10:
        list = []
        for file in sorted(files[0:10]):
            name = str(os.path.basename(file).replace(".py" , ""))
            list.append(Button.inline(f"• {name.title()} •", data=f"help_plugin_{name}"))
        buttons = []
        for key in chunks(list, 2):
            buttons.append(key)
        buttons.append([Button.inline(f"• Next •", data="alien_help_page_2")])
        text += "**• Page:** ( 1 )"
        result = event.builder.article(
            title="Alien Help Menu",
            text=text,
            buttons=buttons,
        )
        await event.answer([result])
    else:
        list = []
        for file in sorted(files):
            name = str(os.path.basename(file).replace(".py" , ""))
            list.append(Button.inline(f"• {name} •", data=f"help_plugin_{name}"))
        buttons = []
        for key in chunks(list, 2):
            buttons.append(key)
        result = event.builder.article(
            title="Alien Help Menu",
            text=text,
            buttons=buttons,
        )
        await event.answer([result])

@alien_callback("alien_help_page_(.*)", owner=True)
async def alien_help(event):
    data = int(event.pattern_match.group(1))
    files = glob.glob("userbot/plugins/*.py")
    start = int(f"{data}0")
    end = start + 10
    if end > len(files):
        end = len(files)
    list = []
    for file in sorted(files[start:end]):
        name = str(os.path.basename(file).replace(".py" , ""))
        list.append(Button.inline(f"• {name.title()} •", data=f"help_plugin_{name}"))
    buttons = []
    for key in chunks(list, 2):
        buttons.append(key)
    if not end > len(files):
        buttons.append([Button.inline(f"• Next •", data=f"alien_help_page_{(data+1)}")])
    buttons.append([Button.inline(f"• Back •", data=f"alien_help_page_{(data-1)}")])
    text = f"""
**• Alien Userbot Help Menu!**

**• Master:** {DB.get_key("OWNER")}
**• Assistant:** @{DB.get_key("ASSISTANT_USERNAME")}

**• Plugins Count:** ( `{len(files)}` )
**• Page:** ( {data} )
"""
    await event.edit(text, buttons=buttons)
