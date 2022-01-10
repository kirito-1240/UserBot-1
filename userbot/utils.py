from pathlib import Path
import ffmpeg , sys , os , heroku3 , logging , math , importlib , glob , shlex , asyncio , functools
from Config import Config  
from time import sleep
from youtubesearchpython import VideosSearch

def ytvideo_info(queryb, limit):
    output = VideosSearch(query.lower() , limit=int(limit))
    result =  output.result()
    return result

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

def convert_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    result = (
        ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s") if seconds else "")
    )
    if result.endswith(":"):
        return result[:-1]
    return result

def creply(event):
    if not event.reply_to == None:
        return True
    return False

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
            if "voice=True" in media:
                type = "Voice"
            else:
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
