import os , sys
from Config import Config
os.system("pip install redis")
from redis import Redis

DB = Redis(
            host="redis-15411.c251.east-us-mz.azure.cloud.redislabs.com:15411",
            password="wIYq4gH5lxQmGVgyk24LZiihAeMNVkVQ",
            port=15411,
            decode_responses=True,
            socket_timeout=5,
            retry_on_timeout=True,
        )
        
set_key = DB.set
get_key = DB.get
get_keys = DB.keys
del_key = DB.delete
