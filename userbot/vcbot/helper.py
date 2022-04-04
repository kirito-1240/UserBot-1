from userbot import app
from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
from userbot.utils import runcmd, convert_time
import os
import re
from time import time

CLIENTS = {}

class Player:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        if CLIENTS.get(chat_id):
            self.group_call = CLIENTS[chat_id]
        else:
            vcClient = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
            self.group_call = vcClient.get_group_call()
            CLIENTS.update({chat_id: self.group_call})

    async def make_vc_active():
        try:
            await app(functions.phone.CreateGroupCallRequest(chat_id, title="🎧 Alien Music 🎶"))
        except:
            return False
        return True

    async def startCall(self):
        if self.chat_id not in CLIENTS:
            try:
                await self.group_call.join(chat_id)
            except GroupCallNotFoundError:
                done = await make_vc_active()
                if not done:
                    return False
                await self.group_call.join(chat_id)
            return True
        else:
            return True

    async def vc_joiner():
        done = await startCall()
        if done:
            return True
        return False

async def download(query):
    if query.startswith("https://") and not "youtube" in query.lower():
        thumb, duration = None, "Unknown"
        title = link = query
    else:
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

async def vid_download(query):
    search = VideosSearch(query, limit=1).result()
    data = search["result"][0]
    link = data["link"]
    video = await get_stream_link(link)
    title = data["title"]
    thumb = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
    duration = data.get("duration") or "♾"
    return video, thumb, title, link, duration

async def file_download(event, reply):
    thumb = "https://telegra.ph/file/22bb2349da20c7524e4db.mp4"
    title = reply.file.title or reply.file.name or str(time()) + ".mp4"
    file = reply.file.name or str(time()) + ".mp4"
    dl = await reply.download_media()
    duration = convert_time(reply.file.duration * 1000) if reply.file.duration else "🤷‍♂️"
    if reply.document.thumbs:
        thumb = await reply.download_media("vcbot/downloads/", thumb=-1)
    return dl, thumb, title, reply.message_link, duration
