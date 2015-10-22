# Pylint: discard cached file state
from astroid import MANAGER
MANAGER.astroid_cache.clear()
