from redis import Redis
from Config import Config

DB = Redis(
            host=Config.REDIS_URL,
            password=Config.REDIS_PASSWORD,
            port=Config.REDIS_PORT,
            decode_responses=True,
            socket_timeout=5,
            retry_on_timeout=True,
        )
