from userbot import app , START_TIME
from telethon import events
import io
import os
import shutil
import time
from pathlib import Path
from userbot.utils import convert_bytes

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.ls(?:\s|$)([\s\S]*)$"))
async def start(event):
    edit = await event.edit("` Please Wait ...`")
    input = "".join(event.text.split(maxsplit=1)[1:])
    path = input or os.getcwd()
    if not os.path.exists(path):
        await edit.edit(f"**• There Is No Such Directory Or File With The Name** `{cat}` **Check Again!**")
        return
    path = Path(cat) if input else os.getcwd()
    if os.path.isdir(path):
        if input:
            output = "**• Folders and files in** `{}` :\n".format(path)
        else:
            output = "**• Folders And Files in Current Directory :**\n"
        lists = os.listdir(path)
        files = ""
        folders = ""
        for contents in sorted(lists):
            catpath = os.path.join(path, contents)
            if not os.path.isdir(catpath):
                size = os.stat(catpath).st_size
                if str(contents).endswith((".mp3", ".flac", ".wav", ".m4a")):
                    files += "🎵" + f"`{contents}`\n"
                if str(contents).endswith((".opus")):
                    files += "🎙" + f"`{contents}`\n"
                elif str(contents).endswith(
                    (".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")
                ):
                    files += "🎞" + f"`{contents}`\n"
                elif str(contents).endswith((".zip", ".tar", ".tar.gz", ".rar")):
                    files += "🗜" + f"`{contents}`\n"
                elif str(contents).endswith(
                    (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")
                ):
                    files += "🖼" + f"`{contents}`\n"
                else:
                    files += "📄" + f"`{contents}`\n"
            else:
                folders += f"📁`{contents}`\n"
        output = output + folders + files if files or folders else output + "__empty path__"
    else:
        size = os.stat(path).st_size
        output = "The details of given file :\n"
        if str(path).endswith((".mp3", ".flac", ".wav", ".m4a")):
            mode = "🎵"
        if str(path).endswith((".opus")):
            mode = "🎙"
        elif str(path).endswith((".mkv", ".mp4", ".webm", ".avi", ".mov", ".flv")):
            mode = "🎞"
        elif str(path).endswith((".zip", ".tar", ".tar.gz", ".rar")):
            mode = "🗜"
        elif str(path).endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".ico")):
            mode = "🖼"
        else:
            mode = "📄"
        time.ctime(os.path.getctime(path))
        time2 = time.ctime(os.path.getmtime(path))
        time3 = time.ctime(os.path.getatime(path))
        output += f"**• Location :** `{path}`\n"
        output += f"**• icon :** `{mode}`\n"
        output += f"**• Size :** `{convert_bytes(size)}`\n"
        output += f"**• Last Modified Time:** `{time2}`\n"
        output += f"**• Last Accessed Time:** `{time3}`"
    await edit.edit(output)
