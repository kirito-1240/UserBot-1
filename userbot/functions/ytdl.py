from youtubesearchpython import Video, ResultMode
from yt_dlp import YoutubeDL
from concurrent.futures import ProcessPoolExecutor
import asyncio
import time

def yt_info(url):
    info = Video.getInfo(url, mode=ResultMode.json)
    result = {
        "title": info["title"],
        "id": info["id"],
        "duration": info["duration"]["secondsText"],
        "description": info["description"],
        "thumbnail": info["thumbnails"][-1]["url"],
        "uploader": info["channel"]["name"],
        "width": info["thumbnails"][-1]["width"],
        "height": info["thumbnails"][-1]["height"],
        "view_count": info["viewCount"]["text"],
        "upload_date": info["uploadDate"],
    }
    return result

def get_video_formats(url):
    get = Video.getFormats(url)
    info = get["streamingData"]["adaptiveFormats"]
    list = {}
    for format in info:
        if "video/mp4" in format["mimeType"]:
            quality = format["qualityLabel"]
            if not quality.endswith("p"):
                quality = (format["qualityLabel"])[:-2]
            if quality not in list:
                format_id = format["itag"]
                quality = f"{quality} - mp4"
                list.update({quality: format_id})
        elif "video/webm" in format["mimeType"]:
            quality = format["qualityLabel"]
            if not quality.endswith("p"):
                quality = (format["qualityLabel"])[:-2]
            if quality not in list:
                format_id = format["itag"]
                quality = f"{quality} - webm"
                list.update({quality: format_id})
    return list

def get_audio_formats(url):
    get = Video.getFormats(url)
    info = get["streamingData"]["adaptiveFormats"]
    list = {}
    for format in info:
        if "audio/mp4" in format["mimeType"]:
            quality = format["audioQuality"].lower().split("_")[-1]
            if quality not in list:
                format_id = format["itag"]
                quality = f"{quality} - mp3"
                list.update({quality: format_id})
        elif "audio/webm" in format["mimeType"]:
            quality = format["audioQuality"].lower().split("_")[-1]
            if quality not in list:
                format_id = format["itag"]
                quality = f"{quality} - webm"
                list.update({quality: format_id})
    return list

def yt_video_down(url, format_id, filename):
    opts = {
            "format": f"{format_id}+bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "ignore_errors": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": filename,
            "logtostderr": False,
            "quiet": True,
        }
    with YoutubeDL(opts) as ytdl:
        ytdl.download([url])

def yt_audio_down(url, format_id, filename):
    opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "ignore_errors": True,
            "nocheckcertificate": True,
            "audio_quality": format_id,
            "postprocessors": [
                {"key": "FFmpegExtractAudio", "preferredcodec": "mp3"},
            ],
            "outtmpl": filename,
            "logtostderr": False,
            "quiet": True,
        }
    with YoutubeDL(opts) as ytdl:
        ytdl.download([url])

PPE = ProcessPoolExecutor()

async def yt_video(url, format_id, filename):
    loop = asyncio.get_event_loop()
    futs = loop.run_in_executor(PPE, yt_video_down, url, format_id, filename)
    return await asyncio.gather(futs)

async def yt_audio(url, format_id, filename):
    loop = asyncio.get_event_loop()
    futs = loop.run_in_executor(PPE, yt_audio_down, url, format_id, filename)
    return await asyncio.gather(futs)
