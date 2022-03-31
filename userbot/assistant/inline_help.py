from userbot.events import alien_inline, alien_callback
from userbot.utils import chunks
from userbot.database import DB
from telethon import Button
import os, glob

@alien_inline(re.compile("test_(.*)"), owner=True)
async def alien_help(event):
    data = event.data_match.group(1).decode("utf-8")
    result = event.builder.article(title="Alien", text=str(data))
    await event.answer([result])

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
            list.append(Button.inline(f"• {name} •", data=f"help_plugin_{name}"))
        buttons = []
        for key in chunks(list, 2):
            buttons.append(key)
        buttons.append([Button.inline(f"• Next •", data=f"page_2")])
        text += "\n**• Page:** ( 1 )"
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
