import redis 
from app.config.settings import Settings


def get_redis_client():
    return redis.Redis(host=Settings().REDIS_HOST, port=Settings().REDIS_PORT, decode_responses=True)

r = get_redis_client()

