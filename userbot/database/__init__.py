from userbot import LOGS
from redis import Redis
from pymongo import MongoClient
import psycopg2
import os
from Config import Config

def get_data(self, key):
    data = self.get(str(key))
    if data:
        try:
            data = eval(data)
        except BaseException:
            pass
    return data

class RedisDB:
    def __init__(self):
        URL = (Config.REDIS_URL).split(":")[0]
        PORT = (Config.REDIS_URL).split(":")[-1]
        self.db = Redis(
                host=URL,
                password=Config.REDIS_PASSWORD,
                port=int(PORT),
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
    def __init__(self):
        self.dB = MongoClient(Config.MongoDB_URL)
        self.db = self.dB["AlienUserBot"]
        self.recache()

    @property
    def name(self):
        return "Mongo"

    @property
    def usage(self):
        return self.db.command("dbstats")["dataSize"]

    def recache(self):
        self.cache = {}
        for key in self.keys():
            self.cache.update({key: self.get_key(key)})

    def ping(self):
        if self.dB.server_info():
            return True

    def keys(self):
        return self.db.list_collection_names()

    def set_key(self, key, value):
        if key in self.keys():
            self.db[key].replace_one({"id": key}, {"value": str(value)})
        else:
            self.db[key].insert_one({"id": key, "value": str(value)})
        self.cache.update({key: value})
        return True

    def del_key(self, key):
        if key in self.keys():
            try:
                del self.cache[key]
            except KeyError:
                pass
            self.db.drop_collection(key)
            return True

    def get_key(self, key):
        if key in self.cache:
            return self.cache[key]
        if key in self.keys():
            value = get_data(self, key)
            self.cache.update({key: value})
            return value
        return None

    def get(self, key):
        if x := self.db[key].find_one({"id": key}):
            return x["value"]

    def flushall(self):
        self.dB.drop_database("AlienUserBot")
        self.cache = {}
        return True


if Config.REDIS_URL and Config.REDIS_PASSWORD:
    DB = RedisDB()
elif Config.MongoDB_URL:
    DB = MongoDB()
