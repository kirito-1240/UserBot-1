from userbot import app , bot
from userbot.utils import runcmd
from userbot.events import alien
import os
import sys
import io

async def runner(code , event):
    chat = await event.get_chat()
    send = await event.get_sender()
    reply = await event.get_reply_message()
    local = lambda _x: print(_format.yaml_format(_x))
    exec("async def coderunner(event , local, chat_id, send_id, reply): "+ "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["coderunner"](event , local, chat.id, send.id, reply)

@alien(pattern="run(?:\s|$)([\s\S]*)", handler="/")
async def runcodes(event):
    await event.edit("`• Running . . .`")
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
    result = None
    if exc:
        result = exc
    elif stderr:
        result = stderr
    elif stdout:
        result = stdout
    else:
        result = "Success!"
    try:
        await app.send_message(event.chat_id , f"""
**• Code:** 
`/run

{cmd}`

**• Output:** 
`{result}`
""")
    except:
        open('Result.txt', 'w').write(str(result))
        await app.send_file(event.chat_id, "Result.txt" , caption=f"""
**• Code:** 
`/run

{cmd}`

**• Output:** 
__In File!__
""")
        os.remove("Result.txt")
    await event.delete()
