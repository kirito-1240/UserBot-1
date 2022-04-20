from userbot import app
from userbot.events import alien_inline, alien_callback
from telethon import Button
from PIL import Image
from userbot.database import DB
from userbot.functions.core import progress
from userbot.utils import convert_time, convert_bytes
from userbot.functions.tools import download_file
from userbot.functions.ytdl import yt_info, get_video_formats, get_video_link, get_audio_formats, get_audio_link
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
    list = get_video_formats(link)
    buttons = []
    buttons.append([
        Button.inline(
            f"🎞 {vid} - {list[vid]}",
            data=f"ytdown||video||{info['id']}||{vid}",
        )
        for vid in list
    ])
    list = get_audio_formats(link)
    buttons.append([
        Button.inline(
            f"🎵 {aud} - {list[aud]}",
            data=f"ytdown||audio||{info['id']}||{aud}",
        )
        for aud in list
    ])
    buttons = zip(buttons[::2], buttons[1::2])
    result = event.builder.photo(
        file=thumb,
        text="{}\n\n**• Please Chose Mode To Download!**".format(INFO.format(info["title"], link, info["view_count"], info["uploader"], desc)),
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

async def send_file(event, filename, info, link, attributes):
    desc = (info["description"])[:300] + " ..."
    thumb = info["title"] + ".jpg"
    ctime = time.time()
    progress_callback = lambda current, total: progress(current, total, event, ctime, "u", filename)
    await app.send_file(event.chat_id, filename, thumb=thumb, attributes=attributes, progress_callback=progress_callback, caption=INFO.format(info["title"], link, info["view_count"], info["like_count"], info["subs_count"], info["uploader"], desc))
    os.remove(filename)
    os.remove(thumb)
    chat = DB.get_key("YOUTUBE_GET_INLINE").split("||")[0].replace("-100", "")
    id = DB.get_key("YOUTUBE_GET_INLINE").split("||")[1]
    await app.delete_messages(int(chat), int(id))
