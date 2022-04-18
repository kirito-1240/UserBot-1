from userbot.events import alien_inline, alien_callback
from telethon import Button
from userbot.functions.ytdl import yt_info
import re

@alien_callback(re.compile("ytdlclose"), owner=True)
async def ytdlclose(event):
    await event.edit("**• Youtube Downloader Panel Successfuly Closed!**")

@alien_inline(re.compile("ytdl_(.*)"), owner=True)
async def ytdl(event):
    link = str(event.pattern_match.group(1))
    info = yt_info(link)
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
    buttons.append([Button.inline("❌ Close ❌", data="ytdlclose")])
    result = event.builder.article(
        title="Alien Youtube Downloader Menu!",
        text="**• Youtube Downloader Panel:**\n\n**• Please Chose Mode To Download!**",
        buttons=buttons,
    )
    await event.answer([result])
    
@alien_inline(re.compile("ytdown\|\|(.*)\|\|(.*)\|\|(.*)"), owner=True)
async def ytdown(event):
    type = str(event.pattern_match.group(1))
    link = str(event.pattern_match.group(2))
    id = str(event.pattern_match.group(3))
    info = yt_info(link)
    if type == "video":
        for vid in info["video_formats"]:
            if str(vid["format_id"]) == id:
                return await event.edit(str(vid["url"]))
    else:
        for aud in info["audio_formats"]:
            if str(aud["format_id"]) == id:
                return await event.edit(str(aud["url"]))         
