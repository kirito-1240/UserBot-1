from . import *

async def runner(code , event):
    local = lambda _x: print(_format.yaml_format(_x))
    exec("async def coderunner(event , local , chat_id , msg_id , from_id): "+ "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["coderunner"](event , local , event.chat.id , event.message.id , event.sender_id)

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^/run(?:\s|$)([\s\S]*)$"))
async def CodeRunner(event):
    await event.edit("`• Running . . .`")
    reply = await event.get_reply_message()
    if event.text[4:]:
        cmd = "".join(event.text.split(maxsplit=1)[1:])
    elif not event.reply_to == None:
        if event.reply_to_message.document and event.reply_to_message.document.mime_type == "text/plain":
            media = event.reply_to_message.document
            media = await app.download_media(media)
            file = open(media , "r")
            cmd = file.read()
        else:
            cmd = reply.text
    else:
        return await event.edit_text("`• What Should I Run ?`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await runner(cmd , event)
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
        await app.send_file(event.chat_id, "Result.txt" , caption="**• Your Code Reply Exceeded One Message! \n • See The Answer In The File!**")
        os.remove("./Result.txt")
