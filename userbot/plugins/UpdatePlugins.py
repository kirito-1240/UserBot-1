from inlinebot import bot
from userbot.utils import load_plugins
from inlinebot.utils import load_plugins as loadplugins
from telethon import events
import sys , os
from time import sleep

@bot.on(events.NewMessage(pattern="(?i)^\.upplugins$"))
async def start(event):
    event = await event.edit("**• Starting Import UserBot Plugins ...**")      
    path = "userbot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))
            await event.edit(f"""**• UserBot Has Imported :** ( `{plugin_name.replace(".py", "")}` )""")
            sleep(2)
    await event.edit("**• UserBot Has Imported Plugins!**")

    edit = await event.reply("**• Starting Import InlineBot Plugins ...**")      
    path = "inlinebot/plugins/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            loadplugins(plugin_name.replace(".py", ""))
            await edit.edit(f"""**• InlineBot Has Imported :** ( `{plugin_name.replace(".py", "")}` )""")
            sleep(2)
     await edit.edit("**• InlineBot Has Imported Plugins!**")

