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
from userbot.database import DB
from userbot.utils import runcmd, convert_time
from telethon import events
from telethon.tl import functions, types
from telethon.utils import get_display_name
from youtubesearchpython import Playlist, VideosSearch
from yt_dlp import YoutubeDL

def get_videos_link(url):
    to_return = []
    regex = re.search(r"\?list=([(\w+)\-]*)", url)
    if not regex:
        return to_return
    playlist_id = regex.group(1)
    videos = Playlist(playlist_id)
    for vid in videos.videos:
        link = re.search(r"\?v=([(\w+)\-]*)", vid["link"]).group(1)
        to_return.append(f"https://youtube.com/watch?v={link}")
    return to_return
     
ACTIVE_CALLS, VC_QUEUE = [], {}
MSGID_CACHE, VIDEO_ON = {}, {}
CLIENTS = {}

class Player:
    def __init__(self, chat, event=None, video=False):
        self._chat = chat
        self._current_chat = event.chat_id if event else DB.get_key("LOG_GROUP")
        self._video = video
        if CLIENTS.get(chat):
            self.group_call = CLIENTS[chat]
        else:
            _client = GroupCallFactory(
                app, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON,
            )
            self.group_call = _client.get_group_call()
            CLIENTS.update({chat: self.group_call})

    async def make_vc_active(self):
        try:
            await app(
                functions.phone.CreateGroupCallRequest(
                    self._chat, title="🎧 Alien Music 🎶"
                )
            )
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
            song, title, link, thumb, from_user, pos, dur = await get_from_queue(
                chat_id
            )
            try:
                await self.group_call.start_audio(song)
            except ParticipantJoinMissingError:
                await self.vc_joiner()
                await self.group_call.start_audio(song)
            if MSGID_CACHE.get(chat_id):
                await MSGID_CACHE[chat_id].delete()
                del MSGID_CACHE[chat_id]
            text = "<strong>🎧 Now playing #{}: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👤 <strong>Requested by:</strong> {}".format(
                pos, link, title, dur, from_user
            )
            try:
                xx = await app.send_message(
                    self._current_chat,
                    "<strong>🎧 Now playing #{}: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👤 <strong>Requested by:</strong> {}".format(
                        pos, link, title, dur, from_user
                    ),
                    file=thumb,
                    link_preview=False,
                    parse_mode="html",
                )
            except ChatSendMediaForbiddenError:
                xx = await app.send_message(
                    self._current_chat, text, link_preview=False, parse_mode="html"
                )
            MSGID_CACHE.update({chat_id: xx})
            VC_QUEUE[chat_id].pop(pos)
            if not VC_QUEUE[chat_id]:
                VC_QUEUE.pop(chat_id)

        except (IndexError, KeyError):
            await self.group_call.stop()
            del CLIENTS[self._chat]
            await app.send_message(
                self._current_chat,
                f"• Successfully Left Vc : <code>{chat_id}</code> •",
                parse_mode="html",
            )
        except Exception as er:
            LOGS.error(er)
            await app.send_message(
                self._current_chat,
                f"<strong>ERROR:</strong> <code>{format_exc()}</code>",
                parse_mode="html",
            )

    async def vc_joiner(self):
        chat_id = self._chat
        done, err = await self.startCall()

        if done:
            await app.send_message(
                self._current_chat,
                "• Joined VC in <code>{}</code>".format(chat_id),
                parse_mode="html",
            )
            return True
        await app.send_message(
            self._current_chat,
            f"<strong>ERROR while Joining Vc -</strong> <code>{chat_id}</code> :\n<code>{err}</code>",
            parse_mode="html",
        )
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
    if not song:
        song = await get_stream_link(link)
    return song, title, link, thumb, from_user, play_this, duration

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

async def dl_playlist(chat, from_user, link):
    links = await get_videos_link(link)
    try:
        search = VideosSearch(links[0], limit=1).result()
        vid1 = search["result"][0]
        duration = vid1.get("duration") or "♾"
        title = vid1["title"]
        song = await get_stream_link(vid1["link"])
        thumb = f"https://i.ytimg.com/vi/{vid1['id']}/hqdefault.jpg"
        return song, thumb, title, vid1["link"], duration
    finally:
        for z in links[1:]:
            try:
                search = VideosSearch(z, limit=1).result()
                vid = search["result"][0]
                duration = vid.get("duration") or "♾"
                title = vid["title"]
                thumb = f"https://i.ytimg.com/vi/{vid['id']}/hqdefault.jpg"
                add_to_queue(chat, None, title, vid["link"], thumb, from_user, duration)
            except Exception as er:
                LOGS.error(er)

async def file_download(event, reply):
    thumb = "https://telegra.ph/file/22bb2349da20c7524e4db.mp4"
    title = reply.file.title or reply.file.name or str(time()) + ".mp4"
    file = reply.file.name or str(time()) + ".mp4"
    dl = await reply.download_media()
    duration = (convert_time(reply.file.duration * 1000) if reply.file.duration else "🤷‍♂️")
    if reply.document.thumbs:
        thumb = await reply.download_media("vcbot/downloads/", thumb=-1)
    return dl, thumb, title, reply.message_link, duration
