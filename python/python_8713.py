# How can I filter objects by how many objects reference them?
from django.db.models import Count
Article.objects.annotate(num_comments=Count('comment')).filter(num_comments__gt=10)
