from userbot import app
from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.utils import convert_time, convert_bytes
from userbot.functions.tools import download_file
from userbot.functions.ytdl import yt_info, yt_video_down, yt_audio_down
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
import re
import os

INFO = """
**• Title:** ( `{}` )
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
        text="{}\n\n**• Please Chose Mode To Download!**".format(INFO.format(info["title"], desc)),
        buttons=buttons,
    )
    await event.answer([result])
    
@alien_callback(re.compile("ytdown\|\|(.*)\|\|(.*)"), owner=True)
async def ytdown(event):
    type = str(event.pattern_match.group(1).decode('utf-8'))
    link = str(event.pattern_match.group(2).decode('utf-8'))
    await event.edit("`• Downloading . . .`")
    info = yt_info(link)
    desc = (info["description"])[:300] + " ..."
    thumb = info["title"] + ".jpg"
    if type == "video":
        filename = info["title"] + ".mp4"
        yt_video_down(link, filename)
        await event.edit("`• Uploading . . .`")
        attributes=[
            DocumentAttributeVideo(
                duration=int(info["duration"]),
                w=str(info["width"]),
                h=str(info["height"]),
                supports_streaming=True
            )
        ]
        await app.send_file(event.chat_id, filename, thumb=thumb, attributes=attributes, caption=INFO.format(info["title"], desc))
        os.remove(filename)
        os.remove(thumb)
    elif type == "audio":
        filename = info["title"] + ".mp3"
        yt_video_down(link, filename)
        await event.edit("`• Uploading . . .`")
        attributes=[
            DocumentAttributeAudio(
                duration=int(info["duration"]),
                title=str(info["title"]),
                performer=str(info["uploader"])
            )
        ]
        await app.send_file(event.chat_id, filename, thumb=thumb, attributes=attributes, caption=INFO.format(info["title"], desc))
        os.remove(filename)
        os.remove(thumb)
