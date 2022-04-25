from userbot import app
from telethon import events
from userbot.events import alien
from userbot.database import DB
from userbot.database.fcom import add_fcom, get_fcom, del_fcom , clean_fcoms

@alien(outgoing=False, incoming=True)
async def send_fcom(event):
    id = get_fcom(event.chat_id)
    if id and event.fwd_from and event.fwd_from.saved_from_peer:
        try:
            msg = await app.get_messages(DB.get_key("LOG_GROUP"), ids=int(id))
        except:
            return
        chat = await event.get_chat()
        me = await event.client.get_me()
        title = (await event.get_chat()).title
        participants = await event.client.get_participants(chat)
        count = len(participants)
        my_mention = "<a href='tg://user?id={}'>{}</a>".format(me.id, me.first_name)
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        await event.reply(
            msg.text.format(
                title=title,
                count=count,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            ),
            file=msg.media,
            link_preview=True,
            parse_mode='html',
        )

@alien(pattern="sfcom")
async def s_fcom(event):
    await event.edit("`• Please Wait . . .`")
    title = (await event.get_chat()).title
    reply = await event.get_reply_message()
    if not reply:
        await event.edit("**• Please Reply To Message!**")
        return
    await app.send_message(DB.get_key("LOG_GROUP") , f"**• First Comment Message Was Saved!**\n**• Chat ID:** `{event.chat_id}`\n\n**• The Following Message Is Saved As The First Comment For The ( {title} ):**\n**• Don't Delete This Message!!**")
    forward = await app.forward_messages(DB.get_key("LOG_GROUP") , messages=reply , from_peer=event.chat_id , silent=True)
    chat_id = event.chat_id
    msg_id = forward.id
    add_fcom(chat_id, msg_id)
    await event.edit("**• First Comment Message On This Chat Was Saved!**")

@alien(pattern="gfcom")
async def g_fcom(event):
    await event.edit("`• Please Wait . . .`")
    id = get_fcom(event.chat_id)
    if not id:
        await event.edit("**• First Comment Message For This Chat Not Saved!**")
        return
    await event.edit(f"**• First Comment Message In This Chat:**\n**• Chat ID:** `{event.chat_id}`")
    try:
        msg = await app.get_messages(DB.get_key("LOG_GROUP"), ids=int(id))
    except:
        return
    await event.reply(msg.text, file=msg.media, formatting_entities=msg.entities,)

@alien(pattern="dfcom")
async def d_fcom(event):
    await event.edit("`• Please Wait . . .`")
    id = del_fcom(event.chat_id)
    if not id:
        await event.edit("**• First Comment Message For This Chat Not Saved!**")
    else:
        await event.edit(f"**• First Comment Message In This Chat Deleted!**")

@alien(pattern="cfcoms")
async def c_fcom(event):
    await event.edit("`• Please Wait . . .`")
    clean_fcoms()
    await event.edit(f"**• First Comment Messages Was Cleaned!**")

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To First Comment Message For New Members!",
        "commands": {
            "{cmdh}sfcom [reply]": "To Set First Comment Message For Chat!",
            "{cmdh}gfcom": "To Get First Comment Message In Chat!",
            "{cmdh}dfcom": "To Delete First Comment Message From Chat!",
            "{cmdh}cfcoma": "To Clean First Comment Messages On All Chats!",
        },
    }
})
