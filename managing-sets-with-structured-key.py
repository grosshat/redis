import redis

r_server = redis.Redis("localhost")

upvotes = r_server.sadd("story:999:upvotes", "userid:12")
print upvotes

upvotes = r_server.sadd("story:999:upvotes", "userid:27")
print upvotes

upvotes = r_server.sadd("story:999:upvotes", "userid:45")
print upvotes

howmany = r_server.scard("story:999:upvotes")
print howmany

"""
It outputs False, since sets can only have unique values.
"""
upvotes = r_server.sadd("story:999:upvotes", "userid:12")
print upvotes

upvotes = r_server.smembers("story:999:upvotes")
print upvotes
