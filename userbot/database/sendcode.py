from . import DB

async def change(type):
    if not "SEND_CODE" in keys():
        await DB.insert_one({"SEND_CODE": type})
    else:
        await DB.replace_one({"SEND_CODE": type})

async def keys():
        return DB.list_collection_names()

async def get(key):
    x = await DB.find_one({"SEND_CODE": key})
    return x["value"]
