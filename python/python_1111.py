# In Django, how to clear all the memcached keys and values?
from django.core.cache import cache
cache._cache.flush_all()
