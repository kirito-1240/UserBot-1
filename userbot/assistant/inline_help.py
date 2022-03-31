from userbot.events import alien_inline, alien_callback
from userbot.utils import chunks
from userbot.database import DB
from telethon import Button
import os, glob, re, random
from userbot.database import PLUGINS_HELP

PIC = random.choice(DB.get_key("START_PIC"))

@alien_inline("alien", owner=True)
async def alien_help(event):
    files = glob.glob("userbot/plugins/*.py")
    list = []
    for file in sorted(files[0:10]):
        name = str(os.path.basename(file).replace(".py" , ""))
        list.append(Button.inline(f"• {name.title()} •", data=f"plugin_{name}_1"))
    buttons = []
    for key in chunks(list, 2):
        buttons.append(key)
    buttons.append([Button.inline("❌ Close ❌", data="close") , Button.inline("Next ▶️", data="page_2")])
    text = f"""
**• Alien Userbot Help Menu!**

**• Master:** {DB.get_key("OWNER")}
**• Assistant:** @{DB.get_key("ASSISTANT_USERNAME")}

**• Plugins Count:** ( `{len(files)}` )
**• Page:** ( 1 )
"""
    result = event.builder.photo(
        file=PIC,
        text=text,
        buttons=buttons,
    )
    await event.answer([result])

@alien_callback(re.compile("page_(.*)"), owner=True)
async def alien_help_pages(event):
    data = int(event.pattern_match.group(1))
    files = glob.glob("userbot/plugins/*.py")
    start = int(f"{(data - 1)}0")
    end = start + 10
    if end > len(files):
        end = len(files)
    list = []
    for file in sorted(files[start:end]):
        name = str(os.path.basename(file).replace(".py" , ""))
        list.append(Button.inline(f"• {name.title()} •", data=f"plugin_{name}_{data}"))
    buttons = []
    for key in chunks(list, 2):
        buttons.append(key)
    other = []    
    if data != 1:
        other.append(Button.inline(f"◀️ Back", data=f"page_{(data-1)}"))
    other.append(Button.inline(f"❌ Close ❌", data="close"))
    if not end > len(files):
        other.append(Button.inline(f"Next ▶️", data=f"page_{(data+1)}"))
    buttons.append([other])
    text = f"""
**• Alien Userbot Help Menu!**

**• Master:** {DB.get_key("OWNER")}
**• Assistant:** @{DB.get_key("ASSISTANT_USERNAME")}

**• Plugins Count:** ( `{len(files)}` )
**• Page:** ( {data} )
"""
    await event.edit(text, file=PIC, buttons=buttons)

@alien_callback(re.compile("plugin_(.*)_(.*)"), owner=True)
async def alien_help_plugins(event):
    data = str(event.pattern_match.group(1))
    page = int(event.pattern_match.group(2))
    await event.edit(f"{data} - {page}")
