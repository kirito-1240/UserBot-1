import glob
from pathlib import Path
from userbot.utils import load_plugins , load_plugins_inline
from . import app , bot
from .Config import Config
from time import sleep

path = "userbot/plugins/*.py"
files = glob.glob(path)
send = app.send_message(Config.BOT_GROUP , "**• Starting Import UserBot Plugins ...**")
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        app.edit_message(send.chat_id , send.id , f"""`• Successfuly Imported : {plugin_name.replace(".py", "")} From UserBot Plugins!`""")
        sleep(2)
app.edit_message(send.chat_id , send.id , "**• Successfuly Imported UserBot Plugins!**")

path = "userbot/inlinebot/*.py"
files = glob.glob(path)
send = app.send_message(Config.BOT_GROUP , "**• Starting Import InlineBot Plugins ...**")
sleep(3)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins_inline(plugin_name.replace(".py", ""))
        app.edit_message(send.chat_id , send.id , f"""`• Successfuly Imported : {plugin_name.replace(".py", "")} From InlineBot Plugins!`""")
        sleep(2)
app.edit_message(send.chat_id , send.id , "**• Successfuly Imported InlineBot Plugins!**")


print("Successfully Deployed!")

bot.run_until_disconnected()
app.start()
app.run_until_disconnected()
