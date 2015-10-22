# Memcache key generation from the query
import hashlib
query = "" #your query here
cache_key = str(int(hashlib.md5(query.lower()).hexdigest(), 16))
