from . import app
from pathlib import Path
import time , requests , ffmpeg , sys , os , heroku3 , logging , math , importlib , glob , shlex , asyncio , functools , re
from Config import Config  
from time import sleep
from youtubesearchpython import VideosSearch

def get_xnxx_video(link , quality="480"):
    get = str(requests.get(link).text)
    if quality == "240":
        url = re.search("html5player\.setVideoUrlHigh\('(.*)'\);" , get)[1]
    elif quality == "480":
        url = re.search("html5player\.setVideoUrlHigh\('(.*)'\);" , get)[1]
    elif quality == "720":
        url = re.search("html5player\.setVideoUrlHigh\('(.*)'\);" , get)[1]
    title = re.search('<meta property="og:title" content="(.*)" />' , get)[1]
    thumb = re.search("html5player\.setThumbUrl\('(.*)'\);" , get)[1]
    desc = re.search('<meta name="description" content="(.*)" />' , get)[1]
    return url , title , thumb , desc

def get_alla_video(link , quality="480"):
    get = str(requests.get(link).content)   
    if quality == "240":
        result = re.search('(?i)(https://nodes.alaatv.com/media/)(\d*/)(240p/)(.*)\.mp4"' , get)
        url = result[1] + result[2] + result[3] + result[4] + ".mp4"
    elif quality == "480":
        result = re.search('(https://nodes.alaatv.com/media/)(\d*/)(hq/)(.*)\.mp4(.*)480p"', get)
        url = result[1] + result[2] + result[3] + result[4] + ".mp4"    
    elif quality == "720":
        result = re.search('(https://nodes.alaatv.com/media/)(\d*/)(HD_720p/)(.*)\.mp4(.*)720p"', get)
        url = result[1] + result[2] + result[3] + result[4] + ".mp4"    
        
    thumb = re.search('thumbnailUrl" : "(https://nodes.alaatv.com/media/thumbnails/)(\d*/)(.*)\.jpg", "description"', get)
    thumb = thumb[1] + thumb[2] + thumb[3] +  ".jpg"
    
    serch = re.search('(?i)meta property="og:title" content="(.*)" /><meta property="og:description"', get)
    string = bytes(serch[1] , 'utf-8')
    title = string.decode('unicode-escape').encode('latin1').decode('utf-8')
    
    serch = re.search('(?i)meta property="og:description" content="(.*)" /><meta property="og:type"', get)
    string = bytes(serch[1] , 'utf-8')
    desc = string.decode('unicode-escape').encode('latin1').decode('utf-8') 
    return url , title , thumb , desc

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

async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err

def chunks(elements, size):
    n = max(1, size)
    return (elements[i:i + n] for i in range(0, len(elements), n))

def restart_app():
    Heroku = heroku3.from_key(Config.HEROKU_API)
    app = Heroku.apps()[Config.HEROKU_APP_NAME]
    app.restart()

def load_plugins(plugin_name):
    path = Path(f"userbot/plugins/{plugin_name}.py")
    name = "userbot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["userbot.plugins." + plugin_name] = load

async def progress(current , total, event, start, type):
    diff = time.time() - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        ttcom = round((total - current) / speed) * 1000
        progress_str = "`[{0}{1}] {2}%`\n\n".format("".join("●" for i in range(math.floor(percentage / 5))) , "".join("" for i in range(20 - math.floor(percentage / 5))) , round(percentage, 2))
        tmp = (progress_str + "`{0} of {1}`\n\n`✦ Speed: {2}/s`\n\n`✦ ETA: {3}`\n\n".format(
                convert_bytes(current) , convert_bytes(total) , convert_bytes(speed) , convert_time(ttcom)))
        await event.edit("`✦ {}`\n\n{}".format(type, tmp))

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
