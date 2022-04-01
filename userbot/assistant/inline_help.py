from userbot.events import alien_inline, alien_callback
from userbot.utils import chunks
from userbot.database import DB, PLUGINS, PLUGINS_HELP
from telethon import Button
import os, glob, re, random
import Config

PIC = random.choice(DB.get_key("INLINE_PIC"))

@alien_inline("alien", owner=True)
async def help(event):
    files = PLUGINS
    list = []
    emoji = DB.get_key("HELP_EMOJI") or "•"
    for file in sorted(files[0:10]):
        name = str(os.path.basename(file).replace(".py" , ""))
        list.append(Button.inline(f"{emoji} {name.title()} {emoji}", data=f"plugin_{name}_1"))
    buttons = []
    for key in chunks(list, 2):
        buttons.append(key)
    buttons.append([Button.inline("❌ Close ❌", data="close_1") , Button.inline("Next ▶️", data="page_2")])
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
async def help_pages(event):
    data = int(event.pattern_match.group(1).decode('utf-8'))
    files = PLUGINS
    start = int(f"{(data - 1)}0")
    if start == 00:
        start = 0
    end = start + 10
    if end > len(files):
        end = len(files)
    emoji = DB.get_key("HELP_EMOJI") or "•"
    list = []
    for file in sorted(files[start:end]):
        name = str(os.path.basename(file).replace(".py" , ""))
        list.append(Button.inline(f"{emoji} {name.title()} {emoji}", data=f"plugin_{name}_{data}"))
    buttons = []
    for key in chunks(list, 2):
        buttons.append(key)
    other = []    
    if data != 1:
        other.append(Button.inline("◀️ Back", data=f"page_{(data-1)}"))
    else:
        count = round(len(files) / 10)
        other.append(Button.inline("◀️ Back", data=f"page_{count}"))
    other.append(Button.inline("❌ Close ❌", data=f"close_{data}"))
    if len(files[start:end]) == 10 or data == 1:
        other.append(Button.inline("Next ▶️", data=f"page_{(data+1)}"))
    else:
        other.append(Button.inline("Next ▶️", data="page_1"))
    buttons.append(other)
    text = f"""
**• Alien Userbot Help Menu!**

**• Master:** {DB.get_key("OWNER")}
**• Assistant:** @{DB.get_key("ASSISTANT_USERNAME")}

**• Plugins Count:** ( `{len(files)}` )
**• Page:** ( {data} )
"""
    await event.edit(text, file=PIC, buttons=buttons)


@alien_callback(re.compile("close_(.*)"), owner=True)
async def close(event):
    page = int(event.pattern_match.group(1).decode('utf-8'))
    buttons = [Button.inline("♻️ Open Again ♻️", data=f"page_{page}")]
    await event.edit("**🚫 Help Menu Successfuly Closed!**", buttons=buttons)

@alien_callback(re.compile("plugin_(.*)_(.*)"), owner=True)
async def help_plugins(event):
    data = str(event.pattern_match.group(1).decode('utf-8'))
    page = int(event.pattern_match.group(2).decode('utf-8'))
    if data in PLUGINS_HELP:
        info = PLUGINS_HELP[data] 
        text = f"** 💡 Plugin Name:** ( `{data.title()}` )"
        text += f"""\n\n** 🧾 Plugin Info:** ( `{info["info"]}` )"""
        text += f"""\n\n\n** ♻️ Available Commands** ( `{len(info["commands"])}` ):"""
        for com in info["commands"]:
            text += "\n    `{}`".format(com.format(cmdh=Config.COMMAND_HANDLER))
        buttons = [[Button.inline("📍 Send Plugin 📍", data=f"sendplug_{data}_{page}")], [Button.inline("⬅️ Back ⬅️", data=f"page_{page}")]]
        await event.edit(text, file=PIC, buttons=buttons)
    else:
        await event.answer("• Not Available Help For This Plugin!", alert=True)

@alien_callback(re.compile("sendplug_(.*)_(.*)"), owner=True)
async def help_plugins(event):
    data = str(event.pattern_match.group(1).decode('utf-8'))
    page = str(event.pattern_match.group(2).decode('utf-8'))
    file = f"userbot/plugins/{data}.py"
    if data in PLUGINS_HELP:
        info = PLUGINS_HELP[data] 
        text = f"** 💡 Plugin Name:** ( `{data.title()}` )"
        text += f"""\n\n** 🧾 Information:** ( `{info["info"]}` )"""
        text += f"""\n\n\n** ♻️ Commands** ( `{len(info["commands"])}` ):"""
        for com in info["commands"]:
            text += "\n    `{}`".format(com.format(cmdh=Config.COMMAND_HANDLER))
    else:
        text = f"** 💡 Plugin Name:** ( `{data.title()}` )\n\n__• Not Available Help For This Plugin!__"
    buttons = [Button.inline("⬅️ Back ⬅️", data=f"plugin_{data}_{page}")]
    await event.edit(text, file=file, thumb="userbot/other/extra.jpg", buttons=buttons)
