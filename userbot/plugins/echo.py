from userbot import app , LOG
from telethon import events
from userbot.database.echo import add_echo, get_echo, del_echo , clean_echos

@app.on(events.NewMessage(incoming=True))
async def send_echo(event):
    get = get_echo(event.chat_id)
    if get and event.from_id.user_id == int(get):
        await app.send_message(event.chat_id , event.text , file=event.media , formatting_entities=event.entities , parse_mode="html")

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.addecho ?(.*)?$"))
async def a_echo(event):
    await event.edit("`• Please Wait . . .`")
    if event.pattern_match.group(1):
        info = await app.get_entity(event.pattern_match.group(1))
        user_id = info.id
    else:
        info = await app.get_entity((await event.get_reply_message()).from_id.user_id)
        user_id = (await event.get_reply_message()).from_id.user_id
    add_echo(event.chat_id, user_id)
    await event.edit("**• Echo Mode For User [{info.first_name}](tg://user?id={info.id}) Has Been Actived!**")

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.delecho ?(.*)?$"))
async def d_echo(event):
    await event.edit("`• Please Wait . . .`")
    if event.pattern_match.group(1):
        info = await app.get_entity(event.pattern_match.group(1))
        user_id = info.id
    else:
        info = await app.get_entity((await event.get_reply_message()).from_id.user_id)
        user_id = (await event.get_reply_message()).from_id.user_id
    del_echo(event.chat_id, user_id)
    await event.edit("**• Echo Mode For User [{info.first_name}](tg://user?id={info.id}) Has Been DeActived!**")

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^\.cechos$"))
async def c_echo(event):
    await event.edit("`• Please Wait . . .`")
    clean_echos(event.chat_id)
    await event.edit(f"**• Echo Mode For User In This Chat Was Cleaned!**")
