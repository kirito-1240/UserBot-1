from userbot import app, bot
from userbot.utils import chunks, convert_bytes
from userbot.functions.tools import download_file
from userbot.database import DB, PLUGINS, PLUGINS_HELP
from telethon import events,  Button
import os
import glob
import re
import random
import time
import Config

PIC = random.choice(DB.get_key("INLINE_PIC")) 

@bot.on(events.InlineQuery(pattern="^alien$"))
async def help(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    files = PLUGINS
    list = []
    emoji = DB.get_key("HELP_EMOJI") or "•"
    for file in sorted(files[0:10]):
        name = str(os.path.basename(file).replace(".py" , ""))
        list.append(Button.inline(f"{emoji} {name.title()} {emoji}", data=f"plugin_{name}_1"))
    buttons = []
    for key in chunks(list, 2):
        buttons.append(key)
    if (len(files) % 10) == 0:
        count = round(len(files) /10)
    else:
        count = round(len(files) /10) + 1
    buttons.append([Button.inline("◀️ Back", data=f"page_{count}"), Button.inline("Next ▶️", data="page_2")])
    buttons.append([Button.inline("❌ Close ❌", data="close_1")])
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

@bot.on(events.CallbackQuery(data=re.compile("page_(.*)")))
async def help_page(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
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
        if (len(files) % 10) == 0:
            count = round(len(files) /10)
        else:
            count = round(len(files) /10) + 1
        other.append(Button.inline("◀️ Back", data=f"page_{count}"))
    if int(data * 10) < len(files) or data == 1:
        other.append(Button.inline("Next ▶️", data=f"page_{(data+1)}"))
    else:
        other.append(Button.inline("Next ▶️", data="page_1"))
    buttons.append(other)
    buttons.append([Button.inline("❌ Close ❌", data=f"close_{data}")])
    text = f"""
**• Alien Userbot Help Menu!**

**• Master:** {DB.get_key("OWNER")}
**• Assistant:** @{DB.get_key("ASSISTANT_USERNAME")}

**• Plugins Count:** ( `{len(files)}` )
**• Page:** ( {data} )
"""
    await event.edit(text, file=PIC, buttons=buttons)

@bot.on(events.CallbackQuery(data=re.compile("close_(.*)")))
async def close(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    page = int(event.pattern_match.group(1).decode('utf-8'))
    buttons = [Button.inline("♻️ Open Again ♻️", data=f"page_{page}")]
    await event.edit("**🚫 Help Menu Successfuly Closed!**", buttons=buttons)

@bot.on(events.CallbackQuery(data=re.compile("empty")))
async def empty(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    await event.answer("• This Is A Display Button!", alert=True)

@bot.on(events.CallbackQuery(data=re.compile("plugin_(.*)_(.*)")))
async def help_plugins(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    data = str(event.pattern_match.group(1).decode('utf-8'))
    page = int(event.pattern_match.group(2).decode('utf-8'))
    if data in PLUGINS_HELP:
        info = PLUGINS_HELP[data] 
        text = f"** 💡 Plugin Name:** ( `{data.title()}` )"
        text += f"""\n\n** 🧾 Plugin Info:** ( `{info["info"]}` )"""
        text += f"""\n\n\n** ♻️ Available Commands** ( `{len(info["commands"])}` ):\n"""
        for com in info["commands"]:
            text += "\n • `{}`\n      `{}`\n".format(com.format(cmdh=Config.COMMAND_HANDLER), info["commands"][com])
        buttons = [[Button.inline("📍 Send Plugin 📍", data=f"sendplug_{data}_{page}")], [Button.inline("⬅️ Back ⬅️", data=f"page_{page}")]]
        await event.edit(text, file=PIC, buttons=buttons)
    else:
        await event.answer("• Not Available Help For This Plugin!", alert=True)

@bot.on(events.CallbackQuery(data=re.compile("sendplug_(.*)_(.*)")))
async def send_plug(event):
    if event.sender_id != int(DB.get_key("OWNER_ID")):
        return await event.answer("• This Is Not For You!", alert=True)
    data = str(event.pattern_match.group(1).decode('utf-8'))
    page = str(event.pattern_match.group(2).decode('utf-8'))
    file = f"userbot/plugins/{data}.py"
    if data in PLUGINS_HELP:
        info = PLUGINS_HELP[data]
        size = os.stat(file).st_size
        text = "**💡 The Details Of Sended Plugin File:**\n\n"
        time.ctime(os.path.getctime(file))
        time2 = time.ctime(os.path.getmtime(file))
        time3 = time.ctime(os.path.getatime(file))
        text += f"**• Plugin Name:** ( `{data.title()}` )\n"
        text += f"**• Size:** ( `{convert_bytes(size)}` )\n"
        text += f"**• Last Modified Time:** ( `{time2}` )\n"
        text += f"**• Last Accessed Time:** ( `{time3}` )"
    else:
        text = f"**💡 Plugin Name:** ( `{data.title()}` )\n\n__• Not Available Help For This Plugin!__"
    buttons = [Button.inline("⬅️ Back ⬅️", data=f"plugin_{data}_{page}")]
    await event.edit(text, file=file, thumb="userbot/other/extra.jpg", buttons=buttons)
