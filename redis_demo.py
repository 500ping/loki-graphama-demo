import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
while p.listen():
    pass
