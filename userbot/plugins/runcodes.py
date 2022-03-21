from userbot import app , bot
from userbot.utils import runcmd
from telethon import events

async def runner(code , event):
    local = lambda _x: print(_format.yaml_format(_x))
    exec("async def coderunner(event , local): "+ "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["coderunner"](event , local)

@app.on(events.NewMessage(outgoing=True , pattern="(?i)^/run(?:\s|$)([\s\S]*)$"))
async def runcodes(event):
    await event.edit("`• Running . . .`")
    reply = await event.get_reply_message()
    if event.text[4:]:
        cmd = "".join(event.text.split(maxsplit=1)[1:])
    else:
        return await event.edit("`• What Should I Run ?`")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await runner(cmd , event)
    except Exception as e:
        exc = e
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = None
    tr = "Results"
    if exc:
        evaluation = exc
        tr = "Errors"
    elif stderr:
        evaluation = stderr
        tr = "Errors"
    elif stdout:
        evaluation = stdout
        tr = "Results"
    else:
        evaluation = "Success!"
        tr = "Results"
    output = f"""**✮  Your Code : ** \n `/run\n\n{cmd}`\n\n**✮  {tr} : ** \n `{evaluation}`"""
    await event.delete()
    if len(str(output)) < 4000:
        await app.send_message(event.chat_id , output)
    else:
        output = f"""✮  Your Code : \n /run\n\n{cmd}\n\n✮  {tr} : \n {evaluation}"""
        with open('Result.txt', 'w') as f:
            f.write(str(output))
            f.close()
        await app.send_file(event.chat_id, "Result.txt" , caption="**• Your Code Reply Exceeded One Message! \n • See The Answer In The File!**")
        os.remove("./Result.txt")
