import os
import sys
from redis import Redis
from Config import Config

class RedisConnection(Redis):
    def __init__(
        self,
        host,
        port,
        password,
        platform=None,
        logger=LOGS,
        *args,
        **kwargs,
    ):
        if host and ":" in host:
            spli_ = host.split(":")
            host = spli_[0]
            port = int(spli_[-1])
            if host.startswith("http"):
                logger.error("Your REDIS_URI should not start with http !")
                import sys

                sys.exit()
        elif not host or not port:
            logger.error("Port Number not found")
            import sys

            sys.exit()
        kwargs["host"] = host
        kwargs["password"] = password
        kwargs["port"] = port

        if platform.lower() == "qovery" and not host:
            var, hash_, host, password = "", "", "", ""
            for vars_ in os.environ:
                if vars_.startswith("QOVERY_REDIS_") and vars.endswith("_HOST"):
                    var = vars_
            if var:
                hash_ = Config.split("_", maxsplit=2)[1].split("_")[0]
            if hash:
                kwargs["host"] = os.environ(f"QOVERY_REDIS_{hash_}_HOST")
                kwargs["port"] = os.environ(f"QOVERY_REDIS_{hash_}_PORT")
                kwargs["password"] = os.environ(f"QOVERY_REDIS_{hash_}_PASSWORD")
        super().__init__(**kwargs)
        self.re_cache()

    def re_cache(self):
        self._cache = {}
        for keys in self.keys():
            self._cache.update({keys: self.get_key(keys)})

    @property
    def name(self):
        return "Redis"

    @property
    def usage(self):
        return sum(self.memory_usage(x) for x in self.keys())

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

def UserBotDB():
    return RedisConnection(
        host=Config.REDIS_URI,
        password=Config.REDIS_PASSWORD,
        port=None,
        platform=None,
        decode_responses=True,
        socket_timeout=5,
        retry_on_timeout=True,
    )
