# Getting the "str" has no property "_default_manager" on a Django app just on startup
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()
