# Using database values in django queryset
from django.db.models import F
Entry.objects.filter( n_comments__gt=F('n_pingbacks') )
