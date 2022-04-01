from userbot import app
from userbot.utils import convert_time , convert_bytes
from userbot.events import alien
from datetime import datetime
import re
import psutil
import platform
import socket
import uuid

@alien(pattern="sysinfo")
async def sysinfo(event):
    await event.edit("`• Please Wait . . .`")
    text = "**• 💻 System Information:**\n"
    uname = platform.uname()
    text += f"**• System:** ( `{uname.system}` )\n"
    text += f"**• Node Name:** ( `{uname.node}` )\n"
    text += f"**• Release:** ( `{uname.release}` )\n"
    text += f"**• Version:** ( `{uname.version}` )\n"
    text += f"**• Machine:** ( `{uname.machine}` )\n"
    text += f"**• Processor:** ( `{uname.processor}` )\n"
    text += f"**• Ip-Address:** ( `{socket.gethostbyname(socket.gethostname())}` )\n"
    text += f"**• Mac-Address:** ( `{':'.join(re.findall('..', '%012x' % uuid.getnode()))}` )\n\n"
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    text += "**• 📀 Cpu Information:**\n"
    text += f"**• Boot Time:** ( `{bt.year}/{bt.month}/{bt.day}` - `{bt.hour}:{bt.minute}:{bt.second}` )\n"
    text += f"**• Physical Cores:** ( `{psutil.cpu_count(logical=False)}` )\n"
    text += f"**• Total Cores:** ( `{psutil.cpu_count(logical=True)}` )\n"
    cpufreq = psutil.cpu_freq()
    text += f"**• Max Frequency:** ( `{cpufreq.max:.2f}Mhz` )\n"
    text += f"**• Min Frequency:** ( `{cpufreq.min:.2f}Mhz` )\n"
    text += f"**• Current Frequency:** ( `{cpufreq.current:.2f}Mhz` )\n\n"
    text += "**• CPU Usage Per Core:**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        text += f"**    Core {i}:** ( `{percentage}%` )\n"
    text += f"**• Total CPU Usage:** ( `{psutil.cpu_percent()}%` )\n\n"
    text += "**💾 Memory Information:**\n"
    svmem = psutil.virtual_memory()
    text += f"**• Total:** ( `{convert_bytes(svmem.total)}` )\n"
    text += f"**• Available:** ( `{convert_bytes(svmem.available)}` )\n"
    text += f"**• Used:** ( `{convert_bytes(svmem.used)}` )\n"
    text += f"**• Percentage:** ( `{svmem.percent}%` )\n\n"
    text += "**📱 Swap:**\n"
    swap = psutil.swap_memory()
    text += f"**• Total:** ( `{convert_bytes(swap.total)}` )\n"
    text += f"**• Free:** ( `{convert_bytes(swap.free)}` )\n"
    text += f"**• Used:** ( `{convert_bytes(swap.used)}` )\n"
    text += f"**• Percentage:** ( `{swap.percent}%` )\n\n"
    text += "**💿 Disk Information:**\n"
    partition = psutil.disk_partitions()[0]
    partition_usage = psutil.disk_usage(partition.mountpoint)
    text += f"**• Total Size:** ( `{convert_bytes(partition_usage.total)}` )\n"
    text += f"**• Used:** ( `{convert_bytes(partition_usage.used)}` )\n"
    text += f"**• Free:** ( `{convert_bytes(partition_usage.free)}` )\n"
    text += f"**• Percentage:** ( `{partition_usage.percent}%` )"
    await event.edit(text)

from userbot.database import PLUGINS_HELP
name = (__name__).split(".")[-1]
PLUGINS_HELP.update({
    name:{
        "info": "To Get System Information!",
        "commands": {
            "{cmdh}sysinfo": "To Get System Information!",
        },
    }
})
