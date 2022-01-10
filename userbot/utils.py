import logging
import math
import importlib
from pathlib import Path
import asyncio , sys , os , heroku3
from Config import Config
import asyncio
import functools
import shlex
import glob
from . import app
import ffmpeg
from time import sleep

async def take_screen_shot(video_file , duration , thumb_image_path):
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    run = await runcmd(command)
    return run

async def runcmd(cmd):
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err

async def restart_app():
    Heroku = heroku3.from_key(Config.HEROKU_API)
    app = Heroku.apps()[Config.HEROKU_APP_NAME]
    app.restart()

def load_plugins(plugin_name):
    path = Path(f"userbot/plugins/{plugin_name}.py")
    name = "userbot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["userbot.plugins." + plugin_name] = load

def convert_bytes(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def convert_time(seconds: int) -> int:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

def media_type(media):
    msg = str((str(media)).split("(", maxsplit=1)[0])
    if msg == "MessageMediaDocument":
        mime = media.document.mime_type
        if mime == "application/x-tgsticker":
            type = "StickerAnimated"
        elif "image" in mime:
            if mime == "image/webp":
                type = "Sticker"
            elif mime == "image/gif":
                type = "GifDoc"
            else:
                type = "PicDoc"
        elif "video" in mime:
            if "DocumentAttributeAnimated" in str(media):
                type = "Gif"
            elif "DocumentAttributeVideo" in str(media):
                atr = str(media.document.attributes[0])
                if "supports_streaming=True" in atr:
                    type = "Video"
                type = "VideoDoc"
            else:
                type = "Video"
        elif "audio" in mime:
            type = "Audio"
        else:
            type = "Document"
    elif msg == "MessageMediaPhoto":
        type = "Pic"
    elif msg == "MessageMediaWebPage":
        type = "Web"
    else:
        type = "Msg"
    return type
