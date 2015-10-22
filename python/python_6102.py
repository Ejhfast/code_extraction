# How to perform OR condition in django queryset?
from django.db.models import Q
User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))
