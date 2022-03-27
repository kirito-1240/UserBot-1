from redis import Redis
import os
os.system("pip3 install motor")
from motor import motor_asyncio
from Config import Config

async def get_data(self, key):
    data = await self.get(str(key))
    if data:
        try:
            data = eval(data)
        except BaseException:
            pass
    return data

class RedisDB:
    def __init__(self, REDIS_URL, REDIS_PASSWORD, REDIS_PORT):
        self.db = Redis(
                host=REDIS_URL,
                password=REDIS_PASSWORD,
                port=REDIS_PORT,
                decode_responses=True,
                socket_timeout=5,
                retry_on_timeout=True,
            )
        self.set = self.db.set
        self.get = self.db.get
        self.keys = self.db.keys
        self.ping = self.db.ping
        self.delete = self.db.delete
        self.recache()

    def recache(self):
        self.cache = {}
        for keys in self.keys():
            self.cache.update({keys: self.get_key(keys)})

    @property
    def name(self):
        return "Redis"

    @property
    def usage(self):
        allusage = 0
        for x in self.keys():
            usage = self.db.memory_usage(x)
            allusage += usage
        return allusage

    def set_key(self, key, value):
        value = str(value)
        try:
            value = eval(value)
        except BaseException:
            pass
        self.cache.update({key: value})
        return self.set(str(key), str(value))

    def get_key(self, key):
        if key in self.cache:
            return self.cache[key]
        get = get_data(self, key)
        self.cache.update({key: get})
        return get

    def del_key(self, key):
        if key in self.cache:
            del self.cache[key]
        return bool(self.delete(str(key)))
        
    def flushall(self):
        for x in self.keys():
            self.del_key(x)
        return True

class MongoDB:
    def __init__(self, MongoDB_URL):
        self.dB = motor_asyncio.AsyncIOMotorClient(MongoDB_URL)
        self.db = self.dB["AlienUserBot"]
        self.recache()

    @property
    def name(self):
        return "Mongo"

    @property
    def usage(self):
        return (await self.db.command("dbstats")["dataSize"])

    def recache(self):
        self.cache = {}
        for key in self.keys():
            self.cache.update({key: self.get_key(key)})

    def ping(self):
        if self.dB.server_info():
            return True

    async def keys(self):
        return (await self.db.list_collection_names())

    async def set_key(self, key, value):
        if key in self.keys():
            await self.db[key].replace_one({"_id": key}, {"value": str(value)})
        else:
            await self.db[key].insert_one({"_id": key, "value": str(value)})
        self.cache.update({key: value})
        return True

    async def del_key(self, key):
        if key in await self.keys():
            try:
                del self.cache[key]
            except KeyError:
                pass
            await self.db.drop_collection(key)
            return True

    async def get_key(self, key):
        if key in self.cache:
            return self.cache[key]
        if key in await self.keys():
            value = await get_data(self, key)
            self.cache.update({key: value})
            return value
        return None

    async def get(self, key):
        if x := await self.db[key].find_one({"_id": key}):
            return x["value"]

    async def flushall(self):
        await self.dB.drop_database("AlienUserBot")
        self.cache = {}
        return True

if Config.REDIS_URL:
    DB = RedisDB(Config.REDIS_URL, Config.REDIS_PASSWORD, Config.REDIS_PORT)
else:
    DB = MongoDB(Config.MongoDB_URL)
