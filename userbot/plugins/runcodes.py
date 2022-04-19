from userbot import app , bot
from userbot.utils import runcmd
from userbot.events import alien
import os
import sys
import io
import traceback

async def runner(code , event):
    chat = await event.get_chat()
    send = await event.get_sender()
    reply = await event.get_reply_message()
    local = lambda _x: print(_format.yaml_format(_x))
    exec("async def coderunner(event , local, chat_id, send_id, reply): "+ "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["coderunner"](event , local, chat.id, send.id, reply)

@alien(pattern="run(?:\s|$)([\s\S]*)")
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
        await asyncio.gather(runner(cmd , event))
    except Exception as e:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    result = None
    if exc:
        result = exc
        res = "Errors"
    elif stderr:
        result = stderr
        res = "Errors"
    elif stdout:
        result = stdout
        res = "Results"
    else:
        result = "Success!"
        res = "Results"
    try:
        await event.edit(f"""
**• Code:** 
`{event.text}`

**• {res}:** 
`{result}`
""")
    except:
        f = open(f"{res}.txt", "w")
        f.write(str(result))
        await app.send_file(event.chat_id, f"{res}.txt" , caption=f"""
**• Code:** 
`{event.text}`

**• {res}:** 
__In File!__
""")
        os.remove(f"{res}.txt")
        await event.delete()

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Run Python Codes!",
        "commands": {
            "{cmdh}run [code]": "To Run Given Python Code!",
        },
    }
})
