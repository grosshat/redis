import redis

r_server = redis.Redis("localhost")
r_server.set("counter", 1)

counter = r_server.incr("counter")

print counter

counter = r_server.decr("counter")

print counter
