import redis

r_server = redis.Redis("localhost")

r_server.rpush("personas", "Sullivan")
r_server.rpush("personas", "Wasowsky")

range = r_server.lrange("personas", 0, 1)

print range

len = r_server.llen("personas")

print len

index = r_server.lindex("personas", 1)

print index
