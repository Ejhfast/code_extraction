# How to properly handle Redis connections with Python / Python RQ?
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
