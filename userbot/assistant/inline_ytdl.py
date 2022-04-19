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
        await event.edit("`• Downloading . . .`")
        await yt_video(link, filename)
        await event.edit("`• Uploading . . .`")
        attributes=[
            DocumentAttributeVideo(
                duration=int(info["duration"]),
                w=int(info["width"]),
                h=int(info["height"]),
                supports_streaming=True,
            )
        ]
        await send_file(event.chat_id, filename, info, link, attributes)
    elif type == "audio":
        filename = info["title"] + ".mp3"
        await event.edit("`• Downloading . . .`")
        await yt_audio(link, filename)
        await event.edit("`• Uploading . . .`")
        attributes=[
            DocumentAttributeAudio(
                duration=int(info["duration"]),
                title=str(info["title"]),
                performer=str(info["uploader"]),
            )
        ]
        await send_file(event.chat_id, filename, info, link, attributes)


PPE = ProcessPoolExecutor()

async def send_file(chat_id, filename, info, link, attributes):
    loop = asyncio.get_event_loop()
    fucs = loop.run_in_executor(PPE, file_sender, chat_id, filename, info, link, attributes)
    return await asyncio.gather(fucs)

async def file_sender(chat_id, filename, info, link, attributes):
    desc = (info["description"])[:300] + " ..."
    thumb = info["title"] + ".jpg"
    await app.send_file(chat_id, filename, thumb=thumb, attributes=attributes, caption=INFO.format(info["title"], link, info["view_count"], info["like_count"], info["subs_count"], info["uploader"], desc))
    os.remove(filename)
    os.remove(thumb)
    chat = DB.get_key("YOUTUBE_GET_INLINE").split("||")[0].replace("-100", "")
    id = DB.get_key("YOUTUBE_GET_INLINE").split("||")[1]
    await app.delete_messages(int(chat), int(id))
