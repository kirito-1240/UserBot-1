from userbot.events import alien_inline, alien_callback
import os, glob
from telethon import Button

def split_list(List, index):
    new_ = []
    while List:
        new_.extend([List[:index]])
        List = List[index:]
    return new_

@alien_inline("alien_inline_help", owner=True)
async def help_func(event):
    files = glob.glob("userbot/plugins/*.py")
    plugin_list = []
    for file in sorted(files):
        name = os.path.basename(file).replace(".py" , "")
        plugin_list.append(str(name))
    count = len(plugin_list)
    list = [
        Button.inline(f"{key}", data=f"help_plugin_{key}")
        for key in sorted(plugin_list[0:10])
    ]
    all = split_list(list, 2)
    fl = split_list(all, 5)
    fl.append([Button.inline("Next", data="page_1")])
    result = event.builder.article(
        title="Alien Help Menu",
        text=str(count),
        buttons=[fl],
    )
    await event.answer([result])
