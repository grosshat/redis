import redis

r_server = redis.Redis("localhost")
r_server.set("environment", "localhost")
value = r_server.get("environment")

print value
