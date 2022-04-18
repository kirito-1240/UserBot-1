from yt_dlp import YoutubeDL

def yt_formats(url):
    info = YoutubeDL().extract_info(url, download=False)
    video = {
        "title": info["title"],
        "id": info["id"],
        "duration": info["duration"],
        "description": info["description"],
        "thumbnail": info["thumbnail"],
        "formats": [],
    }
    audio = {
        "title": info["title"],
        "id": info["id"],
        "duration": info["duration"],
        "description": info["description"],
        "thumbnail": info["thumbnail"],
        "formats": [],
    }
    for res in info["formats"]:  
        if str(res["ext"]) == "mp4" or str(res["ext"]) == "mkv":
            video["formats"].append(
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
            audio["formats"].append(
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
    return video, audio
