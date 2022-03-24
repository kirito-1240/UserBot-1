from userbot import app , LOG
from telethon import events
from userbot.database.goodby import add_goodby, get_goodby, del_goodby , clean_goodbys

@app.on(events.ChatAction)
async def send_goodby(event):
    id = get_goodby(event.chat_id)
    if id and (event.user_left or event.user_kicked) and not (await event.get_user()).bot:
        try:
            await event.delete()
        except:
            pass
        try:
            msg = await app.get_messages(LOG, ids=int(id))
        except:
            return
        a_user = await event.get_user()
        chat = await event.get_chat()
        me = await event.client.get_me()
        title = (await event.get_chat()).title
        participants = await event.client.get_participants(chat)
        count = len(participants)
        mention = "[{}](tg://user?id={})".format(a_user.first_name, a_user.id)
        my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{a_user.username}" if a_user.username else mention
        userid = a_user.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        await event.reply(
            msg.text.format(
                mention=mention,
                title=title,
                count=count,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            ),
            file=msg.media,
            formatting_entities=msg.entities,
            link_preview=True,
            parse_mode="html",
        )

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.sgoodby$"))
async def s_goodby(event):
    await event.edit("`• Please Wait . . .`")
    title = (await event.get_chat()).title
    reply = await event.get_reply_message()
    if not reply:
        await event.edit("**• Please Reply To Message!**")
        return
    await app.send_message(LOG , f"**• Goodby Message Was Saved!**\n**• Chat ID:** `{event.chat_id}`\n\n**• The Following Message Is Saved As The Goodby For The ( {title} ):**\n**• Don't Delete This Message!!**")
    forward = await app.forward_messages(LOG , messages=reply , from_peer=event.chat_id , silent=True)
    chat_id = event.chat_id
    msg_id = forward.id
    add_goodby(chat_id, msg_id)
    await event.edit("**• Goodby Message On This Chat Was Saved!**")

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.ggoodby$"))
async def g_goodby(event):
    await event.edit("`• Please Wait . . .`")
    id = get_goodby(event.chat_id)
    if not id:
        await event.edit("**• Goodby Message For This Chat Not Saved!**")
        return
    await event.edit(f"**• Goodby Message In This Chat:**\n**• Chat ID:** `{event.chat_id}`")
    try:
        msg = await app.get_messages(LOG, ids=int(id))
    except:
        return
    await event.reply(msg.text, file=msg.media, formatting_entities=msg.entities,)

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.dgoodby$"))
async def d_goodby(event):
    await event.edit("`• Please Wait . . .`")
    id = del_goodby(event.chat_id)
    if not id:
        await event.edit("**• Goodby Message For This Chat Not Saved!**")
    else:
        await event.edit(f"**• Goodby Message In This Chat Deleted!**")

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.cgoodbys$"))
async def set_goodby(event):
    await event.edit("`• Please Wait . . .`")
    clean_goodbys()
    await event.edit(f"**• Goodby Messages Was Cleaned!**")
