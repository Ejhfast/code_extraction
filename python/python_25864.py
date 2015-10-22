# Correct way to manage redis connections in django
pool = ConnectionPool(host='localhost', port=6379, db=0)
r = Redis(connection_pool=pool)
