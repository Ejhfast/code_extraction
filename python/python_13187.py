# How can you refresh all regions in Beaker cache in Pyramid?
from beaker.cache import cache_managers
for _cache in cache_managers.values():
    _cache.clear()
