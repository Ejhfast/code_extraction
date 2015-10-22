# Increment Page Hit Count in Django
from django.db.models import F
...
MyModel.objects.filter(id=...).update(hit_count=F('hit_count')+1)
