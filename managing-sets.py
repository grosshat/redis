import redis

r_server = redis.Redis("localhost")

r_server.delete("personas")

personas = r_server.sadd("personas", "Sullivan")
print personas

personas = r_server.sadd("personas", "Wasowsky")
print personas

"""
It outputs False, since sets can only have unique values.
"""
personas = r_server.sadd("personas", "Sullivan")
print personas
