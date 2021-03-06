from userbot.core.logger import LOGS
from bs4 import BeautifulSoup
from userbot.functions.github import GITAPP
from userbot.other.emojis_index import indexs
import os
import re
import random
import aiohttp
import aiofiles
import requests

async def download_file(link, name):
    async with aiohttp.ClientSession() as ses:
        async with ses.get(link) as re_ses:
            file = await aiofiles.open(name, "wb")
            await file.write(await re_ses.read())
            await file.close()
    return name

async def async_searcher(url, post=False, headers=None, params=None, json=None, data=None, re_json=False, re_content=False, real=False):
    async with aiohttp.ClientSession(headers=headers) as client:
        if post:
            data = await client.post(url, json=json, data=data)
        else:
            data = await client.get(url, params=params)
        if re_json:
            return await data.json()
        if re_content:
            return await data.read()
        if real:
            return data
        return await data.text()

random_headers = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) ",
    "Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) ",
    "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
]

async def google_search(query):
    query = query.replace(" ", "+")
    _base = "https://google.com"
    headers = {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "User-Agent": random.choice(random_headers),
    }
    con = await async_searcher(_base + "/search?q=" + query, headers=headers)
    soup = BeautifulSoup(con, "html.parser")
    result = []
    pdata = soup.find_all("a", href=re.compile("url="))
    for data in pdata:
        if not data.find("div"):
            continue
        try:
            result.append(
                {
                    "title": data.find("div").text,
                    "link": data["href"].split("&url=")[1].split("&ved=")[0],
                    "description": data.find_all("div")[-1].text,
                }
            )
        except:
            pass
    return result

async def unsplashsearch(query):
    query = query.replace(" ", "-")
    link = "https://unsplash.com/s/photos/" + query
    extra = await async_searcher(link, re_content=True)
    res = BeautifulSoup(extra, "html.parser", from_encoding="utf-8")
    all = res.find_all("img", "YVj9w")
    return [image["src"] for image in all]

def rgba(r: int, g: int, b: int, a: float) -> str:
    return f'rgba({r}, {g}, {b}, {a})'

async def Carbon(code, file_name="carbonAlien.png", lang="Python"):
    color= rgba(random.randint(20,255), random.randint(20,255), random.randint(20,255), random.randint(20,255))
    font = random.choice(["Hack", "Anonymous Pro", "Cascadia Code", "Droid Sans Mono", "Fantasque Sans Mono", "Fira Code", "Ibm Plex Mono", "Monoid", "Source Code Pro", "Space Mono", "Inconsolata", "Jetbrains Mono", "Ubuntu Mono"])
    theme = random.choice(["3024-night", "a11y-dark", "blackboard", "base16-dark", "base16-light", "cobalt", "dracula", "duotone-dark", "hopscotch", "lucario", "material", "monokai", "night-owl", "nord", "oceanic-next", "one-light", "one-dark", "panda-syntax", "paraiso-dark", "seti", "shades-of-purple", "solarized", "solarized%20light", "synthwave-84", "twilight", "verminal", "vscode", "yeti", "zenburn"])
    options = {
        'code': code,
        'language': lang,
        'backgroundColor': color,
        'fontFamily': font,
        'theme': theme,
    }
    image = await async_searcher("https://carbonara-42.herokuapp.com/api/cook", post=True, headers={'Content-Type': 'application/json'}, json=options, re_content=True)
    open(file_name, 'wb').write(image)
    return file_name

async def get_emoji_link(emoji, type="apple"):
    headers = {"User-Agent": random.choice(random_headers)}
    get = await async_searcher(f"https://www.emojiall.com/en/image/{emoji}", headers=headers)
    res = re.search(f'<img alt="(.*)" title="(.*{type}.*)" src="(.*)" height="(.*)" width="(.*)" class="(.*)" data-ezsrc="(.*)" /> <p class="(.*)">', str(get))
    if res:
        return "https://www.emojiall.com" + res[7]
    return None

async def get_emoji_code(emoji):
    headers = {"User-Agent": random.choice(random_headers)}
    get = await async_searcher(f"https://www.emojiall.com/en/image/{emoji}", headers=headers)
    res = re.search('<img alt="(.*)" title="(.*apple.*)" src="(.*)" height="(.*)" width="(.*)" class="(.*)" data-ezsrc="(.*)" /> <p class="(.*)">', str(get))
    if res:
        code = res[7].split("/")[-1].replace(".png", "")
        if emoji not in indexs:
            indexs.update({emoji: code})
            filepath = "userbot/other/emojis_index.py"
            GITAPP("MxAboli/UserBot").create(filepath, filepath)
        return code
    return None

async def get_emoji_gif(emoji):
    headers = {"User-Agent": random.choice(random_headers)}
    get = await async_searcher(f"https://www.emojiall.com/en/image/{emoji}", headers=headers)
    res = re.search('<img alt="(.*)" title="(.*telegram.*)" src="(.*)" height="(.*)" width="(.*)" class="(.*)" data-ezsrc="(.*)" /> <p class="(.*)">', str(get))
    if res:
        return "https://www.emojiall.com" + res[7]
    return None
