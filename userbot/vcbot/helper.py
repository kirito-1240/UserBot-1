from userbot import app
from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
from userbot.utils import runcmd, convert_time
import os
import re
from time import time

class Player:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        vcClient = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
        self.group_call = vcClient.get_group_call()

    async def make_vc_active():
        try:
            await app(functions.phone.CreateGroupCallRequest(chat_id, title="🎧 Alien Music 🎶"))
        except:
            return False
        return True

    async def startCall(self):
        try:
            await self.group_call.join(chat_id)
            return True
        except GroupCallNotFoundError:
            done = await make_vc_active()
            if not done:
                return False
            await self.group_call.join(chat_id)
            return True

async def youtube_download(query):
    search = VideosSearch(query, limit=1).result()
    data = search["result"][0]
    link = data["link"]
    title = data["title"]
    duration = data.get("duration") or "♾"
    thumb = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
    dl = await get_stream_link(link)
    return dl, thumb, title, link, duration

async def get_stream_link(ytlink):
    stream = await runcmd(f'yt-dlp -g -f "best[height<=?720][width<=?1280]" {ytlink}')
    return stream[0]

async def file_download(reply):
    thumb = "https://telegra.ph/file/22bb2349da20c7524e4db.mp4"
    title = reply.file.title or reply.file.name or str(time()) + ".mp4"
    file = reply.file.name or str(time()) + ".mp4"
    dl = await reply.download_media()
    duration = convert_time(reply.file.duration * 1000) if reply.file.duration else "🤷‍♂️"
    if reply.document.thumbs:
        thumb = await reply.download_media(thumb=-1)
    return dl, thumb, title, reply.message_link, duration
