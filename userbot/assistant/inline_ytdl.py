from userbot import app
from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.utils import convert_time, convert_bytes
from userbot.functions.tools import download_file
from userbot.functions.ytdl import yt_info, yt_video_down, yt_audio_down
from yt_dlp import YoutubeDL
from telethon.tl.types import DocumentAttributeVideo, DocumentAttributeAudio
import re
import os
import time
import math

INFO = """
**• Title:** ( `{}` )
**• Description:** ( `{}` )
**• Duration:** ( `{}` )
**• Quality:** ( `{}` )
**• Resolution:** ( `{}` )
"""
LASTINFO = """
**• Title:** ( `{}` )
**• Description:** ( `{}` )
"""

@alien_inline(re.compile("ytdl_(.*)"), owner=True)
async def ytdl(event):
    

@alien_inline(re.compile("ytdl_(.*)"), owner=True)
async def ytdl(event):
    link = str(event.pattern_match.group(1))
    info = yt_info(link)
    desc = (info["description"])[:500] + " ..."
    thumb = info["title"] + ".jpg"
    await download_file(info["thumbnail"], thumb)
    buttons = [[Button.inline("🎞 Video 🎞", data=f"ytdown||video||{link}"), Button.inline("🎵 Audio 🎵", data=f"ytdown||audio||{link}")]]
    result = event.builder.photo(
        file=thumb,
        text="{}\n\n**• Please Chose Mode To Download!**".format(LASTINFO.format(info["title"], desc)),
        buttons=buttons,
    )
    await event.answer([result])
    
@alien_callback(re.compile("ytdown\|\|(.*)\|\|(.*)"), owner=True)
async def ytdown(event):
    type = str(event.pattern_match.group(1).decode('utf-8'))
    link = str(event.pattern_match.group(2).decode('utf-8'))
    await event.edit("`• Downloading . . .`")
    info = yt_info(link)
    desc = (info["description"])[:200] + " ..."
    thumb = info["title"] + ".jpg"
    if type == "video":
        filename = info["title"] + ".mp4"
        yt_video_down(link, filename)
        await app.send_file(event.chat_id, filename, thumb=thumb, caption=INFO.format(info["title"], desc, convert_time(info["duration"]), vid["format_note"], vid["resolution"]))
        os.remove(filename)
        os.remove(thumb)
        await app.delete_messages(event.chat_id, [event.id])
    elif type == "audio":
        filename = info["title"] + ".mp3"
        yt_video_down(link, filename)
        await app.send_file(event.chat_id, filename, thumb=thumb, caption=INFO.format(info["title"], desc, convert_time(info["duration"]), aud["format_note"], aud["resolution"]))
        os.remove(filename)
        os.remove(thumb)
