# Creating and managing multiple connections in Redis Python
&gt;&gt;&gt; pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
&gt;&gt;&gt; r = redis.StrictRedis(connection_pool=pool)
