from userbot import app
from userbot.events import alien_inline
from telethon import Button
from PIL import Image
from userbot.database import DB
from userbot.functions.core import progress
from userbot.utils import convert_time, convert_bytes
from userbot.functions.tools import download_file, downloadfile
from userbot.functions.ytdl import yt_info, get_video_formats, get_audio_formats, yt_video, yt_audio
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
import re
import asyncio
import os
import time

INFO = """
**• Title:** ( `{}` )
**• Link:** ( `{}` )
**• View Count:** ( `{}` )
**• Uploader:** ( `{}` )
**• Description:** ( `{}` )
"""

@alien_inline(re.compile("ytdl_(.*)"), owner=True)
async def ytdl(event):
    link = str(event.pattern_match.group(1))
    info = yt_info(link)
    desc = (info["description"])[:300] + " ..."
    thumb = info["id"] + ".jpg"
    await download_file(info["thumbnail"], thumb)
    list = get_video_formats(link)
    buttons = []
    for vid in list:
        buttons.append(
            Button.inline(
                f"🎞 {vid}",
                data=f"yt||v||{link}||{list[vid]}",
           ))
    list = get_audio_formats(link)
    for aud in list:
        buttons.append(
            Button.inline(
                f"🎵 {aud}",
                data=f"yt||a||{link}||{list[aud]}",
            ))
    buttons = (buttons[::3], buttons[1::3], buttons[2::3])
    result = event.builder.photo(
        file=thumb,
        text="{}\n\n**• Please Chose Mode To Download!**".format(INFO.format(info["title"], link, info["view_count"], info["uploader"], desc)),
        buttons=buttons,
    )
    await event.answer([result])
    
@bot.on(events.CallbackQuery(data=re.compile("yt\|\|(.*)\|\|(.*)\|\|(.*)")))
async def ytdown(event):
    type = str(event.pattern_match.group(1).decode('utf-8'))
    link = str(event.pattern_match.group(2).decode('utf-8'))
    format_id = str(event.pattern_match.group(3).decode('utf-8'))
    info = yt_info(link)
    desc = (info["description"])[:300] + " ..."
    thumb = info["id"] + ".jpg"
    img = Image.open(thumb)
    img.resize((320, 320))
    img.save(thumb, "JPEG")
    loop = asyncio.get_event_loop()
    if type == "v":
        filename = info["id"] + ".mp4"
        if os.path.exists(filename):
            os.remove(filename)
        await event.edit("`• Downloading . . .`\n\n__• This May Take A Long Time!__")
        await yt_video(link, format_id, filename)
        await event.edit("`• Uploading . . .`\n\n__• This May Take A Long Time!__")
        attributes=[
            DocumentAttributeVideo(
                duration=int(info["duration"]),
                w=int(info["width"]),
                h=int(info["height"]),
                supports_streaming=True,
            )
        ]
        loop.create_task(send_file(event, filename, info, link, attributes))
    elif type == "a":
        filename = info["id"] + ".mp3"
        if os.path.exists(filename):
            os.remove(filename)
        await event.edit("`• Downloading . . .`\n\n__• This May Take A Long Time!__")
        await yt_audio(link, format_id, filename)
        await event.edit("`• Uploading . . .`\n\n__• This May Take A Long Time!__")
        attributes=[
            DocumentAttributeAudio(
                duration=int(info["duration"]),
                title=str(info["title"]),
                performer=str(info["uploader"]),
            )
        ]
        loop.create_task(send_file(event, filename, info, link, attributes))

async def send_file(event, filename, info, link, attributes):
    desc = (info["description"])[:300] + " ..."
    thumb = info["id"] + ".jpg"
    ctime = time.time()
    progress_callback = lambda current, total: progress(current, total, event, ctime, "u", filename)
    await app.send_file(event.chat_id, filename, thumb=thumb, attributes=attributes, progress_callback=progress_callback, caption=INFO.format(info["title"], link, info["view_count"], info["uploader"], desc))
    os.remove(filename)
    os.remove(thumb)
    await event.delete()
