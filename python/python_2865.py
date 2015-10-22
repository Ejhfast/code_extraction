# Django aggregate and grouping : code cleanliness problem
from django.db.models import Count
Song.objects.values('author','author__instrument').annotate(Count("id"))
