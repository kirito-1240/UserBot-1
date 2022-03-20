from redis import Redis

DB = Redis(
            host="redis-15411.c251.east-us-mz.azure.cloud.redislabs.com",
            password="wIYq4gH5lxQmGVgyk24LZiihAeMNVkVQ",
            port=15411,
            decode_responses=True,
            socket_timeout=5,
            retry_on_timeout=True,
        )
        
def keys():
    return DB.keys

def set_key(key, value):
    return DB.set(str(key) , str(value))

def get_key(key):
    return DB.get(str(key))

def del_key(self, key):
    return DB.delete(str(key))
