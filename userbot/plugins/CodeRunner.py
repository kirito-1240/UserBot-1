from . import *

async def aexec(code , status):
    message = event = status
    p = lambda _x: print(_format.yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        (
            "async def __aexec(message, event , reply , client , p , chat): "
            + "".join(f"\n {l}" for l in code.split("\n"))
        )
    )

    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )


@app.on(events.NewMessage(outgoing=True , pattern="(?i)^/run(?:\s|$)([\s\S]*)$"))
async def CodeRunner(event):
    await event.edit("`• Please Wait ...`")
    if event.text[4:]:
        cmd = "".join(event.message.message.split(maxsplit=1)[1:])
    elif not event.reply_to == None:
        reply = await event.get_reply_message()
        if reply.media and reply.document.mime_type == "text/plain":
            media = reply.media
            await app.download_media(media , "input.txt")
            file = open("input.txt")
            cmd = file.read()
        else:
            cmd = reply.text
    else:
        return await event.edit("`• What Should I Run ?`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd , event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success!"
    output = f"""**✮  Your Code : ** \n `/run\n\n{cmd}`\n\n**✮  Result : ** \n `{evaluation}`"""
    await event.delete()
    if len(str(output)) < 4000:
        await app.send_message(event.chat_id , output)
    else:
        output = f"""✮  Your Code : \n /run\n\n{cmd}\n\n✮  Result : \n {evaluation}"""
        with open('Result.txt', 'w') as f:
            f.write(str(output))
            f.close()
        await app.send_file(event.chat_id, "Result.txt" , caption="**• Your Code Reply Exceeded One Message! \n • See The Answer In The File!**" , reply_to=event.message.id)
        os.remove("./Result.txt")
