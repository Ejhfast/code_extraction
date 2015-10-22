# Django non-distinct query
from django.db.models import Count
qs = FooBar.objects.filter(example__pk__lt=50)
qs = qs.annotate(num_examples=Count('example')).filter(num_examples__gt=1)
