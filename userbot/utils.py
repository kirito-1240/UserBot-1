from . import app , bot
from telethon import functions
from pathlib import Path
import ffmpeg , sys , time , requests , os , heroku3 , logging , math , importlib , glob , shlex , asyncio , functools , re
from Config import Config  
from time import sleep
from youtubesearchpython import VideosSearch

def create_buttons(items):
    buttons = []
    list1 = []
    list2 = []
    for item in items:
        name = os.path.basename(item).replace(".py" , "")
        list.append([[Button.inline(f"• {name.title()} •",data=f"help_{name}")]])
        if len(list) == 2:
            buttons.append([list[0] , list[1]])
            list = []
    if len(list) > 0:
        buttons.append([list[0]])          
    return buttons

def ocr_space_file(filename , language):
    payload = {'apikey': Config.OCR_API_KEY,'language': language}
    with open(filename , 'rb') as file:
        req = requests.post('https://api.ocr.space/parse/image',files={filename: file},data=payload)
    return req.json()

async def take_screen_shot(video , duration , image):
    command = f"ffmpeg -ss {duration} -i '{video}' -vframes 1 '{image}'"
    run = await runcmd(command)
    return run

async def runcmd(cmd):
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )

def chunks(elements, size):
    n = max(1, size)
    return (elements[i:i + n] for i in range(0, len(elements), n))

def restart_app():
    Heroku = heroku3.from_key(Config.HEROKU_API)
    app = Heroku.apps()[Config.HEROKU_APP_NAME]
    app.restart()

def load_plugins(folder):
    files = glob.glob(f"userbot/{folder}/*.py")
    files.remove(f"userbot/{folder}/__init__.py")
    for name in files:
        plugin_name = os.path.basename(name)
        try:
            path = Path(f"userbot/{folder}/{plugin_name}")
            name = "userbot.{}.{}".format(folder , plugin_name.replace(".py" , ""))
            spec = importlib.util.spec_from_file_location(name, path)
            load = importlib.util.module_from_spec(spec)
            load.logger = logging.getLogger(plugin_name)
            spec.loader.exec_module(load)
            sys.modules[name] = load
            print(f"""• Bot Has Imported ( {plugin_name.replace(".py", "")} ) Plugin""")
        except Exception as e:
            print(f"""• Bot Can't Import ( {plugin_name.replace(".py", "")} ) Plugin - Error : < {e} >""")
    
async def AddBot():
    info = await bot.get_me()
    try:
        await app(functions.messages.AddChatUserRequest(Config.LOG_GROUP , user_id=info.username))
    except:
        pass
        

async def get_progress(event, current , total, start, type, filename):
    if type == "d":
        type = f"Downloading {filename} . . ."
    elif type == "u":
        type = f"Uploading {filename} . . ."
    diff = time.time() - start
    if round(diff % 2.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        ttcom = round((total - current) / speed) * 1000
        await event.edit(f"""
`🌐 {type}`\n
`[{"".join("●" for i in range(math.floor(percentage / 5)))}]{round(percentage, 2)}%`\n
**✦ Size: **( `{convert_bytes(current)}` ) **Of** ( `{convert_bytes(total)}` )\n
**✦ Speed: **( `{convert_bytes(speed)}/s` )\n
**✦ ETA: **( `{convert_time(ttcom)}` )""")

def convert_bytes(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def convert_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    months, days = divmod(days, 30)
    result = (
        ((str(months) + "m:") if months else "")
        + ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s") if seconds else "")
    )
    if result.endswith(":"):
        return result[:-1]
    return result
