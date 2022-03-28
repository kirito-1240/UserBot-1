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
        self.db = Redis(
                host=Config.REDIS_URL,
                password=Config.REDIS_PASSWORD,
                port=Config.REDIS_PORT,
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
        self.dB = MongoClient(Config.MongoDB_URL, serverSelectionTimeoutMS=5000)
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


class SqlDB:
    def __init__(self):
        self.connection = psycopg2.connect(dsn=Config.DATABASE_URL)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Alien ()")
        self.recache()

    @property
    def name(self):
        return "SQL"

    @property
    def usage(self):
        self.cursor.execute("SELECT pg_size_pretty(pg_relation_size('Alien')) AS size")
        data = self.cursor.fetchall()
        return int(data[0][0].split()[0])

    def recache(self):
        self.cache = {}
        for key in self.keys():
            self.cache.update({key: self.get_key(key)})

    def keys(self):
        self.cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name  = 'Alien'")
        data = self.cursor.fetchall()
        return [x[0] for x in data]

    def ping(self):
        return True

    def get_key(self, variable):
        if variable in self.cache:
            return self.cache[variable]
        get = get_data(self, variable)
        self.cache.update({variable: get})
        return get

    def get(self, variable):
        try:
            self.cursor.execute(f"SELECT (%s) FROM Alien", (str(variable),))
        except psycopg2.errors.UndefinedColumn:
            return None
        data = self.cursor.fetchall()
        if not data:
            return None
        if len(data) >= 1:
            for i in data:
                if i[0]:
                    return i[0]

    def set_key(self, key, value):
        try:
            self.cursor.execute(f"ALTER TABLE Alien DROP COLUMN IF EXISTS (%s)", (str(key)))
            self.cursor.execute(f"INSERT INTO Alien (%s) values (%s)", key, value)
        except:
            pass
        self.cache.update({key: value})
        return True

    def del_key(self, key):
        if key in self.cache:
            del self.cache[key]
        try:
            self.cursor.execute(f"ALTER TABLE Alien DROP COLUMN (%s)", (str(key)))
        except psycopg2.errors.UndefinedColumn:
            return False
        return True

    delete = del_key

    def flushall(self):
        self.cache.clear()
        self.cursor.execute("DROP TABLE Alien")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Alien ()")
        return True

    def rename(self, key1, key2):
        name = self.get_key(key1)
        if name:
            self.del_key(key1)
            self.set_key(key2, name)
            return 0
        return 1


if Config.REDIS_URL and Config.REDIS_PASSWORD and Config.REDIS_PORT:
    DB = RedisDB()
elif Config.MongoDB_URL:
    DB = MongoDB()
elif Config.DATABASE_URL:
    DB = SqlDB()
