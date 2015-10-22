# Updating a Haystack search index with Django + Celery
from haystack.management.commands import update_index
update_index.Command().handle()
