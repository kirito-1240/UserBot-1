from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player, youtube_download, file_download
from userbot.functions.helper import media_type

@alien(pattern="play ?(.*)?")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    reply = await event.get_reply_message()
    if reply and reply.media and media_type(reply) in ["Video", "Voice", "Audio"]:
        song, thumb, song_name, link, duration = await file_download(reply)
    elif event.pattern_match.group(1):
        song, thumb, song_name, link, duration = await youtube_download(event.pattern_match.group(1))
    else:
        return await event.edit("**• Please Input A Youtube Link Or Reply To A Song!**")
    player = Player(event.chat_id)
    song_name = song_name[:30] + " . . ."
    start_call = await player.startCall()
    if not start_call:
        return await event.edit("**• Error, Please Try Again!**")
    await player.group_call.start_audio(song)
    await event.edit(f"Playing - {song_name}")
