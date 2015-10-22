# Django queryset ordering by _set
from django.db.models import Count
Image.objects.annotate(Count("person")).order_by("person__count")
