from userbot import app
from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.utils import convert_time, convert_bytes
from userbot.functions.tools import download_file
from userbot.functions.ytdl import yt_info, yt_video_down, yt_audio_down
import re, os, glob

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
    link = str(event.pattern_match.group(1))
    info = yt_info(link)
    desc = (info["description"])[:500] + " ..."
    thumb = info["title"] + ".jpg"
    await download_file(info["thumbnail"], thumb)
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
    list = []
    for oth in info["other_formats"]:
        list.append(Button.inline(f'🔗 {oth["format"].split(" - ")[1]}', data=f'ytdown||video||{link}||{oth["format_id"]}'))
        if len(list) == 2:
            buttons.append([list[0], list[1]])
            list = []
    if len(list) == 1:
        buttons.append([list[0]])
    result = event.builder.photo(
        file=thumb,
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
    desc = (info["description"])[:200] + " ..."
    thumb = info["title"] + ".jpg"
    if type == "video":
        for vid in info["video_formats"]:
            if str(vid["format_id"]) == id:
                filename = info["title"] + ".mp4"
                yt_video_down(link, vid["format_id"], filename)
                await app.send_file(event.chat_id, filename, thumb=thumb, caption=INFO.format(info["title"], desc, convert_time(info["duration"]), vid["format_note"], vid["resolution"]))
                os.remove(filename)
                os.remove(thumb)
                await app.delete_messages(event.chat_id, [event.id])
    elif type == "audio":
        for aud in info["audio_formats"]:
            if str(aud["format_id"]) == id:
                filename = info["title"] + ".mp3"
                yt_video_down(link, aud["format_id"], filename)
                for x in glob.glob(f'{info["title"]}*'):
                    if not x.endswith("jpg"):
                        id = x
                os.rename(id, filename)
                await app.send_file(event.chat_id, filename, thumb=thumb, caption=INFO.format(info["title"], desc, convert_time(info["duration"]), aud["format_note"], aud["resolution"]))
                os.remove(filename)
                os.remove(thumb)
                await app.delete_messages(event.chat_id, [event.id])
    elif type == "other":
        for oth in info["other_formats"]:
            if str(oth["format_id"]) == id:
                filename = info["title"] + "." + oth["ext"]
                await download_file(link, filename)
                await app.send_file(event.chat_id, filename, thumb=thumb, caption=INFO.format(info["title"], desc, convert_time(info["duration"]), oth["format_note"], oth["resolution"]))
                os.remove(filename)
                os.remove(thumb)
                await app.delete_messages(event.chat_id, [event.id])
