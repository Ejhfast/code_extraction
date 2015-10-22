# Django ORM Table Relationships
from django.db.models import Count
Games.objects.filter(owned=0).annotate(vote=Count('votes')).order_by('-vote')
