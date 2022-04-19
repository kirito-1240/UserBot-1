from yt_dlp import YoutubeDL
from datetime import datetime

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

async def yt_video_down(url, filename):
    opts = {
            "format": "best",
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
        data = ytdl.extract_info(url)
    return data

async def yt_audio_down(url, filename):
    opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "ignore_errors": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": filename,
            "logtostderr": False,
            "quiet": True,
        }
    with YoutubeDL(opts) as ytdl:
        data = ytdl.extract_info(url)
    return data
