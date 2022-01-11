from pathlib import Path
import ffmpeg , sys , os , heroku3 , logging , math , importlib , glob , shlex , asyncio , functools
from Config import Config  
from time import sleep
from youtubesearchpython import VideosSearch
from telethon.tl import functions, types

async def get_chat_info(chat):
    if isinstance(chat, types.Channel):
        chat_info = await app(functions.channels.Getchat_infoChannelRequest(chat))
    elif isinstance(chat, types.Chat):
        chat_info = await app(functions.messages.Getchat_infoChatRequest(chat))
    else:
        return "**• Please Input Or Send On Group/Channel!**"
    chat_info = chat_info.full_chat
    broadcast = getattr(chat, "broadcast", False)
    chat_type = "Channel" if broadcast else "Group"
    msg_info = await app(functions.messages.GetHistoryRequest(peer=chat.id,offset_id=0,offset_date=None,add_offset=-0,limit=0,max_id=0,min_id=0,hash=0))
    first_msg_valid = bool(msg_info and msg_info.messages and msg_info.messages[0].id == 1)
    creator_valid = bool(first_msg_valid and msg_info.users)
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = (msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Deleted Account")
    created = msg_info.messages[0].date if first_msg_valid else None
    restricted_users = getattr(chat_info, "banned_count", None)
    members = getattr(chat_info, "participants_count", chat.participants_count)
    admins = getattr(chat_info, "admins_count", None)
    kicked_users = getattr(chat_info, "kicked_count", None)
    members_online = getattr(chat_info, "online_count", 0)
    group_stickers = (chat_info.stickerset.title if getattr(chat_info, "stickerset", None) else None)
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = getattr(chat_info, "read_inbox_max_id", None)
    messages_sent_alt = getattr(chat_info, "read_outbox_max_id", None)
    exp_count = getattr(chat_info, "pts", None)
    supergroup = "Yes" if getattr(chat, "megagroup", None) else "No"
    if admins is None:
        participants_admins = await app(functions.channels.GetParticipantsRequest(    channel=chat.id , filter=types.ChannelParticipantsAdmins() , offset=0 , limit=0 , hash=0))
        admins = participants_admins.count if participants_admins else None
    result = "ℹ️ **CHAT INFO:**\n\n"
    result += f"🆔 **ID:** ( `{chat.id}` )\n"
    if chat_title is not None:
        result += f"💡 **{chat_type} Name:** ( `{chat.title}` )\n"
    result += f"🦸‍♂ **Supergroup:** ( `{supergroup}` )\n"
    if chat.username:
        result += f"🔗 **Username:** ( @{chat.username} )\n"
    else:
        result += f"🗳 **{chat_type} Type:** ( `Private` )\n"
    if creator_id:
        result += f'🖌 **Creator:** ( [{creator_firstname}](tg://user?id={creator_id}) )\n'
    if created:
        result += f"🖌 **Created:** ( `{created.date().strftime('%b %d, %Y')} - {created.time()}` )\n"
    else:
        result += f"🖌 **Created:** ( `{chat.date.date().strftime('%b %d, %Y')} - {chat.date.time()}` )\n"
    if exp_count is not None:
        chat_level = int((1 + math.sqrt(1 + 7 * exp_count / 14)) / 2)
        result += f"⭐️ **{chat_type} Level:** ( `{chat_level}` )\n"
    if messages_viewable is not None:
        result += f"💬 **Viewable Messages:** ( `{messages_viewable}` )\n"
    if messages_sent:
        result += f"💬 **Messages Sent:** ( `{messages_sent}` )\n"
    elif messages_sent_alt:
        result += f"💬 **Messages Sent:** ( `{messages_sent_alt}` ) ⚠\n"
    if members is not None:
        result += f"👥 **Members:** ( `{members}` )\n"
    if admins:
        result += f"👮 **Administrators:** ( `{admins}` )\n"
    if chat_info.bot_info:
        result += f"🤖 **Bots:** ( `{len(chat_info.bot_info)}` )\n"
    if members_online:
        result += f"👀 **Currently Onlines:** ( `{members_online}` )\n"
    if restricted_users is not None:
        result += f"🔕 **Restricted Users:** ( `{restricted_users}` )\n"
    if banned_users:
        result += f"⛔️ **Banned Users:** ( `{kicked_users}` )\n"
    if group_stickers:
        result += f'📹 **{chat_type} Stickers:** [{group_stickers}](t.me/addstickers/{chat_info.stickerset.short_name})\n'
    if not broadcast:
        if getattr(chat, "slowmode_enabled", None):
            result += f"👉 **Slow Mode:** ( `{chat_info.slowmode_seconds}s`\n"
    if chat_info.about:
        result += f"🗒 **Description:** ( `{chat_info.about}` )\n"
    return result

def ytvideo_info(query , limit):
    output = VideosSearch(query.lower() , limit=int(limit))
    result =  output.result()
    return result

def take_screen_shot(video_file , duration , thumb_image_path):
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    run = runcmd(command)
    return run

async def runcmd(cmd):
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err

def restart_app():
    Heroku = heroku3.from_key(Config.HEROKU_API)
    app = Heroku.apps()[Config.HEROKU_APP_NAME]
    app.restart()

def load_plugins(plugin_name):
    path = Path(f"userbot/plugins/{plugin_name}.py")
    name = "userbot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["userbot.plugins." + plugin_name] = load

def convert_bytes(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def convert_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    result = (
        ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s") if seconds else "")
    )
    if result.endswith(":"):
        return result[:-1]
    return result
