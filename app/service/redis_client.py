import redis 


def get_redis_client():
    redis.Redis(host="localhost", port=6379, decode_responses=True)

r = get_redis_client()

