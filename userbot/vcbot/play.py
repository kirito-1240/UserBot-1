from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player, add_to_queue, VC_QUEUE, youtube_download, file_download
from userbot.functions.helper import media_type
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError, MessageIdInvalidError
import os

@alien(pattern="play ?(.*)?")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    reply = await event.get_reply_message()
    if reply and reply.media and media_type(reply) in ["Video", "Voice", "Audio"]:
        song, thumb, song_name, performer, duration, link = await file_download(event, reply)
    elif event.pattern_match.group(1):
        song, thumb, song_name, performer, duration, link = await youtube_download(event.pattern_match.group(1))
    else:
        return await event.edit("**• Please Input A Youtube Link Or Reply To A Song!**")
    from_user = (await app.get_entity(event.sender_id)).mention
    player = Player(event.chat_id, event)
    song_name = song_name[:50] + "..."
    if not player.group_call.is_connected:
        if not (await player.vc_joiner()):
            return
        await player.group_call.start_audio(song)
        if isinstance(link, list):
            for lin in link[1:]:
                add_to_queue(chat, song, lin, lin, None, from_user, duration)
            link = song_name = link[0]
        text = "**🎵 Start Playing:** [{}]({})\n\n**⏰ Duration:** ( `{}` )\n**👥 Chat ID:** ( `{}` )\n**🙋‍♂ By:** ( {} )".format(song_name, link, duration, event.chat_id, from_user)
        await event.reply(text, file=thumb)
        await event.delete()
        if thumb and os.path.exists(thumb):
            os.remove(thumb)
    else:
        if isinstance(link, list):
            for lin in link[1:]:
                add_to_queue(event.chat_id, song, lin, lin, None, from_user, duration)
            link = song_name = link[0]
        add_to_queue(event.chat_id, song, song_name, link, thumb, from_user, duration)
        return await event.edit("**🎵 Added To Queue:** ( [{}]({}) )\n\n**• Queue:** ( `#{}` )".format(song_name, link , (list(VC_QUEUE[event.chat_id].keys())[-1])))
