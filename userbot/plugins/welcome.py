from userbot import app , LOG
from telethon import events
from userbot.database.welcome import set_welcome , get_welcome , get_chats , del_welcome

@app.on(events.ChatAction)
async def send_welcome(event):
    id = get_welcome(event.chat_id)
    if id and (event.user_joined or event.user_added) and not (await event.get_user()).bot:
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
        mention = "<a href='tg://user?id={}'>{}</a>".format(a_user.id, a_user.first_name)
        my_mention = "<a href='tg://user?id={}'>{}</a>".format(me.id, me.first_name)
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
