from yt_dlp import YoutubeDL
from userbot.functions.core import progress
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
import asyncio
import time

async def my_hook(d, event):
    print(d["status"])
    print(event)

def yt_info(url):
    info = YoutubeDL().extract_info(url, download=False)
    upload_date = int(info["upload_date"])
    upload_date = datetime.fromtimestamp(upload_date)
    upload_date = upload_date.strftime("%Y/%m/%d - %H:%M:%S")
    result = {
        "title": info["title"],
        "id": info["id"],
        "duration": info["duration"],
        "description": info["description"],
        "thumbnail": info["thumbnail"],
        "uploader": info["uploader"],
        "uploader_url": info["uploader_url"],
        "channel_url": info["channel_url"],
        "width": info["width"],
        "height": info["height"],
        "like_count": info["like_count"],
        "view_count": info["view_count"],
        "subs_count": info["channel_follower_count"],
        "upload_date": upload_date,
    }
    return result

def yt_video_down(url, filename):
    ctime = time.time()
    opts = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "ignore_errors": True,
            "nocheckcertificate": True,
            "progress_hooks":  [my_hook(d , filename)],
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": filename,
            "logtostderr": False,
            "quiet": True,
        }
    with YoutubeDL(opts) as ytdl:
        ytdl.download([url])

def yt_audio_down(url, filename):
    ctime = time.time()
    opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "ignore_errors": True,
            "nocheckcertificate": True,
            "progress_hooks":  [lambda prog: progress(prog["downloaded_bytes"], prog["total_bytes"], event, ctime, "d", filename)],
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "480",
                }
            ],
            "outtmpl": filename,
            "logtostderr": False,
            "quiet": True,
        }
    with YoutubeDL(opts) as ytdl:
        ytdl.download([url])


PPE = ProcessPoolExecutor()

async def yt_video(url, filename):
    loop = asyncio.get_event_loop()
    fucs = loop.run_in_executor(PPE, yt_video_down, url, filename)
    return await asyncio.gather(fucs)

async def yt_audio(url, filename):
    loop = asyncio.get_event_loop()
    fucs = loop.run_in_executor(PPE, yt_audio_down, url, filename)
    return await asyncio.gather(fucs)
