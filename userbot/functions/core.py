import time
import math
from userbot.utils import convert_time, convert_bytes

async def progress(current, total, event, start, type, filename):
    if type == "d":
        act = "• Downloading . . ."
    elif type == "u":
        act = "• Uploading . . ."
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elaptime = round(diff) * 1000
        tcom = round((total - current) / speed) * 1000
        eta = convert_time(elaptime + tcom)
        com = "".join(["●" for i in range(math.floor(percentage / 5))])
        percent = round(percentage, 2)
        frem = convert_bytes(current)
        ftotal = convert_bytes(total)
        text = "`{}`\n\n**• File Name:** ( `{}` )\n\n`[{}]` - `{}%`\n\n**• Size:** ( `{}` **Of** `{}` )\n\n**• ETA:** ( `{}` )"
        await event.edit(text.format(act, filename, com , percent, frem, ftotal, eta))
