from youtubesearchpython import Video, ResultMode
from yt_dlp import YoutubeDL
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
            if quality not in list:
                format_id = format["itag"]
                list.update({quality: {"format_id": format_id, "type": "mp4"}})
        elif "video/webm" in format["mimeType"]:
            quality = format["qualityLabel"]
            if quality not in list:
                format_id = format["itag"]
                list.update({quality: {"format_id": format_id, "type": "webm"}})
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
                list.update({quality: {"format_id": format_id, "type": "mp3"}})
        elif "audio/webm" in format["mimeType"]:
            quality = format["audioQuality"].lower().split("_")[-1]
            if quality not in list:
                format_id = format["itag"]
                list.update({quality: {"format_id": format_id, "type": "webm"}})
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
