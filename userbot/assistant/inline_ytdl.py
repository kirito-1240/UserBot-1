from userbot import app
from userbot.events import alien_inline, alien_callback
from telethon import Button
from telethon.utils import get_attributes
from userbot.utils import convert_time, convert_bytes
from userbot.functions.tools import download_file
from userbot.functions.ytdl import yt_info, yt_video_down, yt_audio_down
import re, os

INFO = """
**• Title:** ( `{}` )
**• Description:** ( `{}` )
**• Duration:** ( `{}` )
**• Size:** ( `{}` )
**• Quality:** ( `{}` )
**• Resolution:** ( `{}` )
"""
LASTINFO = """
**• Title:** ( `{}` )
**• Description:** ( `{}` )
"""

@alien_inline(re.compile("ytdl_(.*)"), owner=True)
async def ytdl(event):
    link = str(event.pattern_match.group(1))
    info = yt_info(link)
    desc = (info["description"])[:500] + " ..."
    buttons = []
    list = []
    for aud in info["audio_formats"]:
        list.append(Button.inline(f'🎶 {aud["format"].split(" - ")[1]}', data=f'ytdown||audio||{link}||{aud["format_id"]}'))
        if len(list) == 2:
            buttons.append([list[0], list[1]])
            list = []
    if len(list) == 1:
        buttons.append([list[0]])
    list = []
    for vid in info["video_formats"]:
        list.append(Button.inline(f'🎞 {vid["format"].split(" - ")[1]}', data=f'ytdown||video||{link}||{vid["format_id"]}'))
        if len(list) == 2:
            buttons.append([list[0], list[1]])
            list = []
    if len(list) == 1:
        buttons.append([list[0]])
    result = event.builder.article(
        title="Alien Youtube Menu!",
        text="{}\n\n**• Please Chose Mode To Download!**".format(LASTINFO.format(info["title"], desc)),
        buttons=buttons,
    )
    await event.answer([result])
    
@alien_callback(re.compile("ytdown\|\|(.*)\|\|(.*)\|\|(.*)"), owner=True)
async def ytdown(event):
    type = str(event.pattern_match.group(1).decode('utf-8'))
    link = str(event.pattern_match.group(2).decode('utf-8'))
    id = str(event.pattern_match.group(3).decode('utf-8'))
    await event.edit("`• Downloading . . .`")
    info = yt_info(link)
    desc = (info["description"])[:500] + " ..."
    thumb = info["title"] + ".jpg"
    await download_file(info["thumbnail"], thumb)
    if type == "video":
        for vid in info["video_formats"]:
            if str(vid["format_id"]) == id:
                filename = info["title"] + "." + vid["ext"]
                yt_video_down(link, vid["format_id"], filename)
                atts = get_attributes(filename)
                await app.send_file(event.chat_id, filename, thumb=thumb, caption=INFO.format(info["title"], desc, convert_time(info["duration"]), (convert_bytes(vid["size"]) or "--"), vid["format_note"], vid["resolution"]))
                os.remove(filename)
                os.remove(thumb)
                await event.delete()
    elif type == "audio":
        for aud in info["audio_formats"]:
            if str(aud["format_id"]) == id:
                filename = info["title"] + "." + aud["ext"]
                yt_video_down(link, aud["format_id"], filename)
                atts = get_attributes(filename)
                await app.send_file(event.chat_id, filename, thumb=thumb, caption=INFO.format(info["title"], desc, convert_time(info["duration"]), (convert_bytes(aud["size"]) or "--"), aud["format_note"], aud["resolution"]))
                os.remove(filename)
                os.remove(thumb)
                await event.delete()
