from userbot import app
from userbot.events import alien
from userbot.vcbot.helper import Player, add_to_queue, download, file_download
from userbot.functions.helper import media_type
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError, MessageIdInvalidError

@alien(pattern="play ?(.*)?")
async def googlesearch(event):
    await event.edit("`• Please Wait . . .`")
    reply = await event.get_reply_message()
    if reply and reply.media and media_type(reply) in ["Video", "Voice", "Audio"]:
        song, thumb, song_name, link, duration = await file_download(event, reply)
    elif event.pattern_match.group(1):
        song, thumb, song_name, link, duration = await download(event.pattern_match.group(1))
    else:
        return await event.edit("**• Please Input A Youtube Link Or Reply To A Song!**")
    from_user = (await app.get_entity(event.sender_id)).mention
    player = Player(event.chat_id, event)
    song_name = song_name[:30] + "..."
    if not player.group_call.is_connected:
        if not (await player.vc_joiner()):
            return
        await player.group_call.start_audio(song)
        if isinstance(link, list):
            for lin in link[1:]:
                add_to_queue(chat, song, lin, lin, None, from_user, duration)
            link = song_name = link[0]
        text = "🎸 <strong>Now playing: <a href={}>{}</a>\n⏰ Duration:</strong> <code>{}</code>\n👥 <strong>Chat:</strong> <code>{}</code>\n🙋‍♂ <strong>Requested by: {}</strong>".format(link, song_name, duration, chat, from_user)
        await event.reply(text, file=thumb, parse_mode="html")
        await event.delete()
        if thumb and os.path.exists(thumb):
            os.remove(thumb)
    else:
        if isinstance(link, list):
            for lin in link[1:]:
                add_to_queue(event.chat_id, song, lin, lin, None, from_user, duration)
            link = song_name = link[0]
        add_to_queue(event.chat_id, song, song_name, link, thumb, from_user, duration)
        return await event.edit(f"▶ Added 🎵 <a href={link}>{song_name}</a> to queue at #{list(VC_QUEUE[chat].keys())[-1]}.",parse_mode="html")
