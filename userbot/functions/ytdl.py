from youtubesearchpython import Video, ResultMode
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
                size = format["contentLength"]
                list.update({quality: size})
    return list

def get_audio_formats(url):
    get = Video.getFormats(url)
    info = get["streamingData"]["adaptiveFormats"]
    list = {}
    for format in info:
        if "audio/mp4" in format["mimeType"]:
            quality = format["audioQuality"].lower().split("_")[-1]
            if quality not in list:
                size = format["contentLength"]
                list.update({quality: size})
    return list

def get_video_link(url, quality):
    get = Video.getFormats(url)
    info = get["streamingData"]["adaptiveFormats"]
    for format in info:
        if "video/mp4" in format["mimeType"]:
            qua = format["qualityLabel"]
            if qua == quality:
                return format["url"]
    return None

def get_audio_link(url, qua):
    get = Video.getFormats(url)
    info = get["streamingData"]["adaptiveFormats"]
    for format in info:
        if "audio/mp4" in format["mimeType"]:
            qua = format["audioQuality"].lower().split("_")[-1]
            if qua == quality:
                return format["url"]
    return None
