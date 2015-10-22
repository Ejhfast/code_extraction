# Django To Filter distinct content with counts
from django.db.models import Count
jobs.objects.values('states').annotate(count=Count('states'))
