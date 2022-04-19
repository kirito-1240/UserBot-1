from yt_dlp import YoutubeDL

def yt_video_down(url, format, filename):
    opts = {
            "format": f"{format}+bestaudio",
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

def yt_audio_down(url, format, filename):
    opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "ignore_errors": True,
            "audio_quality": format,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                }
            ],
            "outtmpl": filename,
            "logtostderr": False,
            "quiet": True,
        }
    with YoutubeDL(opts) as ytdl:
        ytdl.download([url])

def yt_info(url):
    info = YoutubeDL().extract_info(url, download=False)
    result = {
        "title": info["title"],
        "id": info["id"],
        "duration": info["duration"],
        "description": info["description"],
        "thumbnail": info["thumbnail"],
        "video_formats": [],
        "audio_formats": [],
        "other_formats": [],
    }
    for res in info["formats"]:  
        if str(res["ext"]) == "mp4" or str(res["ext"]) == "mkv":
            result["video_formats"].append(
                    {
                "url": res["url"],
                "format": res["format"],
                "format_note": res["format_note"],
                "size": res["filesize"],
                "format_id": res["format_id"],
                "ext": res["ext"],
                "resolution": res["resolution"],
            }
        )
        elif str(res["ext"]) == "mp3" or str(res["ext"]) == "m4a":
            result["audio_formats"].append(
                    {
                "url": res["url"],
                "format": res["format"],
                "format_note": res["format_note"],
                "size": res["filesize"],
                "format_id": res["format_id"],
                "ext": res["ext"],
                "resolution": res["resolution"],
            }
        )
        else:
            result["other_formats"].append(
                    {
                "url": res["url"],
                "format": res["format"],
                "format_note": res["format_note"],
                "size": res["filesize"],
                "format_id": res["format_id"],
                "ext": res["ext"],
                "resolution": res["resolution"],
            }
        )
    return result
