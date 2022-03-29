from userbot.core.logger import LOGS
import os, re, random
from bs4 import BeautifulSoup
import aiohttp, aiofiles

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
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) "
    "Chrome/19.0.1084.46 Safari/536.5",
    "Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) "
    "Chrome/19.0.1084.46 Safari/536.5",
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
