from userbot import app
from userbot.events import alien_inline, alien_callback
from telethon import Button
from PIL import Image
from userbot.database import DB
from userbot.utils import convert_time, convert_bytes
from userbot.functions.tools import download_file
from concurrent.futures import ProcessPoolExecutor
from userbot.functions.ytdl import yt_info, yt_video, yt_audio
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
import re
import asyncio
import os
import math
import time

INFO = """
**• Title:** ( `{}` )
**• Link:** ( `{}` )
**• View Count:** ( `{}` )
**• Like Count:** ( `{}` )
**• Subscribes Count:** ( `{}` )
**• Uploader:** ( `{}` )
**• Description:** ( `{}` )
"""

@alien_inline(re.compile("ytdl_(.*)"), owner=True)
async def ytdl(event):
    link = str(event.pattern_match.group(1))
    info = yt_info(link)
    desc = (info["description"])[:300] + " ..."
    thumb = info["title"] + ".jpg"
    await download_file(info["thumbnail"], thumb)
    buttons = [[Button.inline("🎞 Video 🎞", data=f"ytdown||video||{link}"), Button.inline("🎵 Audio 🎵", data=f"ytdown||audio||{link}")]]
    result = event.builder.photo(
        file=thumb,
        text="{}\n\n**• Please Chose Mode To Download!**".format(INFO.format(info["title"], link, info["view_count"], info["like_count"], info["subs_count"], info["uploader"], desc)),
        buttons=buttons,
    )
    await event.answer([result])
    
@alien_callback(re.compile("ytdown\|\|(.*)\|\|(.*)"), owner=True)
async def ytdown(event):
    type = str(event.pattern_match.group(1).decode('utf-8'))
    link = str(event.pattern_match.group(2).decode('utf-8'))
    info = yt_info(link)
    desc = (info["description"])[:300] + " ..."
    thumb = info["title"] + ".jpg"
    img = Image.open(thumb)
    img.resize((320, 320))
    img.save(thumb, "JPEG")
    if type == "video":
        filename = info["title"] + ".mp4"
        await event.edit("`• Downloading . . .`\n\n__• This May Take A Long Time!__")
        await yt_video(link, filename)
        await event.edit("`• Uploading . . .`\n\n__• This May Take A Long Time!__")
        attributes=[
            DocumentAttributeVideo(
                duration=int(info["duration"]),
                w=int(info["width"]),
                h=int(info["height"]),
                supports_streaming=True,
            )
        ]
        await asyncio.gather(send_file(event, filename, info, link, attributes))
    elif type == "audio":
        filename = info["title"] + ".mp3"
        await event.edit("`• Downloading . . .`\n\n__• This May Take A Long Time!__")
        await yt_audio(link, filename)
        await event.edit("`• Uploading . . .`\n\n__• This May Take A Long Time!__")
        attributes=[
            DocumentAttributeAudio(
                duration=int(info["duration"]),
                title=str(info["title"]),
                performer=str(info["uploader"]),
            )
        ]
        await asyncio.gather(send_file(event, filename, info, link, attributes))

async def progress(current, total, event, start, type_of_ps, file_name):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            ''.join(["▰" for i in range(math.floor(percentage / 10))]),
            ''.join(["▱" for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                convert_bytes(current),
                convert_bytes(total),
                convert_time(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))

async def send_file(event, filename, info, link, attributes):
    desc = (info["description"])[:300] + " ..."
    thumb = info["title"] + ".jpg"
    ctime = time.time()
    progress_callback = lambda current, total: progress(current, total, event, ctime, "Uploading . . .", filename)
    await app.send_file(event.chat_id, filename, thumb=thumb, attributes=attributes, progress_callback=progress_callback, caption=INFO.format(info["title"], link, info["view_count"], info["like_count"], info["subs_count"], info["uploader"], desc))
    os.remove(filename)
    os.remove(thumb)
    chat = DB.get_key("YOUTUBE_GET_INLINE").split("||")[0].replace("-100", "")
    id = DB.get_key("YOUTUBE_GET_INLINE").split("||")[1]
    await app.delete_messages(int(chat), int(id))
