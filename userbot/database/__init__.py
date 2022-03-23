from redis import Redis
from Config import Config


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
        self.re_cache()

    def re_cache(self):
        self._cache = {}
        for keys in self.keys():
            self._cache.update({keys: self.get_key(keys)})

    @property
    def usage(self):
        return sum(self.db.memory_usage(x) for x in self.keys())

    def set_key(self, key, value):
        value = str(value)
        try:
            value = eval(value)
        except BaseException:
            pass
        self._cache.update({key: value})
        return self.set(str(key), str(value))

    def get_key(self, key):
        if key in self._cache:
            return self._cache[key]
        _ = get_data(self, key)
        self._cache.update({key: _})
        return _

    def del_key(self, key):
        if key in self._cache:
            del self._cache[key]
        return bool(self.delete(str(key)))

DB = RedisDB()
