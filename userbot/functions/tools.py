import os
try:
    import aiohttp
except:
    os.system("pip install aiohttp")
    import aiohttp

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
