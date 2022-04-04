import asyncio
import os
import re
import traceback
from time import time
from traceback import format_exc
from userbot import app
from pytgcalls import GroupCallFactory
from pytgcalls.exceptions import GroupCallNotFoundError
from telethon.errors.rpcerrorlist import (
    ParticipantJoinMissingError,
    ChatSendMediaForbiddenError,
)
from userbot.core.logger import LOGS
from userbot.functions.tools import download_file
from userbot.database import DB
from userbot.utils import runcmd, convert_time
from telethon import events
from telethon.tl import functions, types
from telethon.utils import get_display_name
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
     
ACTIVE_CALLS = []
VC_QUEUE = {}
MSGID_CACHE = {}
VIDEO_ON = {}
CLIENTS = {}

class Player:
    def __init__(self, chat, event=None, video=False):
        self._chat = chat
        self._current_chat = event.chat_id if event else DB.get_key("LOG_GROUP")
        self._video = video
        if CLIENTS.get(chat):
            self.group_call = CLIENTS[chat]
        else:
            _client = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON)
            self.group_call = _client.get_group_call()
            CLIENTS.update({chat: self.group_call})

    async def make_vc_active(self):
        try:
            await app(functions.phone.CreateGroupCallRequest(self._chat, title="🎧 Alien Music 🎶"))
        except Exception as e:
            LOGS.error(e)
            return False, e
        return True, None

    async def startCall(self):
        if VIDEO_ON:
            for chats in VIDEO_ON:
                await VIDEO_ON[chats].stop()
            VIDEO_ON.clear()
            await asyncio.sleep(3)
        if self._video:
            for chats in list(CLIENTS):
                if chats != self._chat:
                    await CLIENTS[chats].stop()
                    del CLIENTS[chats]
            VIDEO_ON.update({self._chat: self.group_call})
        if self._chat not in ACTIVE_CALLS:
            try:
                self.group_call.on_network_status_changed(self.on_network_changed)
                self.group_call.on_playout_ended(self.playout_ended_handler)
                await self.group_call.join(self._chat)
            except GroupCallNotFoundError as er:
                LOGS.info(er)
                dn, err = await self.make_vc_active()
                if err:
                    return False, err
            except Exception as e:
                LOGS.error(e)
                return False, e
        return True, None

    async def on_network_changed(self, call, is_connected):
        chat = self._chat
        if is_connected:
            if chat not in ACTIVE_CALLS:
                ACTIVE_CALLS.append(chat)
        elif chat in ACTIVE_CALLS:
            ACTIVE_CALLS.remove(chat)

    async def playout_ended_handler(self, call, source, mtype):
        if os.path.exists(source):
            os.remove(source)
        await self.play_from_queue()

    async def play_from_queue(self):
        chat_id = self._chat
        if chat_id in VIDEO_ON:
            await self.group_call.stop_video()
            VIDEO_ON.pop(chat_id)
        try:
            song, title, link, thumb, from_user, pos, dur = await get_from_queue(chat_id)
            try:
                await self.group_call.start_audio(song)
            except ParticipantJoinMissingError:
                await self.vc_joiner()
                await self.group_call.start_audio(song)
            if MSGID_CACHE.get(chat_id):
                await MSGID_CACHE[chat_id].delete()
                del MSGID_CACHE[chat_id]
            text = "<strong>🎧 Now playing #{}: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👤 <strong>Requested by:</strong> {}".format(pos, link, title, dur, from_user)
        try:
            mes = await app.send_message(self._current_chat, text, file=thumb, link_preview=False)
            MSGID_CACHE.update({chat_id: mes})
            VC_QUEUE[chat_id].pop(pos)
            if not VC_QUEUE[chat_id]:
                VC_QUEUE.pop(chat_id)
        except (IndexError, KeyError):
            await self.group_call.stop()
            del CLIENTS[self._chat]
            await app.send_message(self._current_chat, "**• Queue List Is Empty!**\n\n**• Successfully Left From Voice Chat In This Chat!**")
        
    async def vc_joiner(self):
        chat_id = self._chat
        done, err = await self.startCall()
        if done:
            await app.send_message(self._current_chat, "**• Successfuly Joined On Voice Chat In This Chat!**")
            return True
        await app.send_message(self._current_chat, "**• Error While Joining On Voice Chat In This Chat!**")
        return False

def add_to_queue(chat_id, song, song_name, link, thumb, from_user, duration):
    try:
        n = sorted(list(VC_QUEUE[chat_id].keys()))
        play_at = n[-1] + 1
    except BaseException:
        play_at = 1
    stuff = {
        play_at: {
            "song": song,
            "title": song_name,
            "link": link,
            "thumb": thumb,
            "from_user": from_user,
            "duration": duration,
        }
    }
    if VC_QUEUE.get(chat_id):
        VC_QUEUE[int(chat_id)].update(stuff)
    else:
        VC_QUEUE.update({chat_id: stuff})
    return VC_QUEUE[chat_id]

def list_queue(chat):
    if VC_QUEUE.get(chat):
        txt, n = "", 0
        for x in list(VC_QUEUE[chat].keys())[:18]:
            n += 1
            data = VC_QUEUE[chat][x]
            txt += f'<strong>{n}. <a href={data["link"]}>{data["title"]}</a> :</strong> <i>By: {data["from_user"]}</i>\n'
        txt += "\n\n....."
        return txt

async def get_from_queue(chat_id):
    play_this = list(VC_QUEUE[int(chat_id)].keys())[0]
    info = VC_QUEUE[int(chat_id)][play_this]
    song = info.get("song")
    title = info["title"]
    link = info["link"]
    thumb = info["thumb"]
    from_user = info["from_user"]
    duration = info["duration"]
    return song, title, link, thumb, from_user, play_this, duration

async def youtube_download(query):
    search = VideosSearch(query, limit=1).result()
    data = search["result"][0]
    link = data["link"]
    title = data["title"]
    performer = data["channel"]["name"]
    duration = data.get("duration")
    thumb = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
    song = await get_stream_link(link)
    song = await download_file(song, title + ".mp3")
    return song, thumb, title, performer, duration, reply.message_link

async def get_stream_link(ytlink):
    stream = await runcmd(f'yt-dlp -g -f "best[height<=?720][width<=?1280]" {ytlink}')
    return stream[0]

async def file_download(event, reply):
    reply = await event.get_reply_message()
    get = reply.media.document.attributes
    title = get[0].title
    performer = get[0].performer
    duration = convert_time(get[0].duration)
    song = await reply.download_media()
    thumb = "http://telegra.ph/file/8d240e71b0d36a6a3a19f.jpg"
    if reply.media.document.thumbs:
        thumb = reply.media.document.thumbs[-1]
    return song, thumb, title, performer, duration, reply.message_link
