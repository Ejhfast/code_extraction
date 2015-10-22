# Django : Syncdb incorrectly warns that many-to-many field is stale
from django.contrib.contenttypes.models import ContentType
ct = ContentType.objects.get(app_label='Apps', model='app_users')
ct.delete()
