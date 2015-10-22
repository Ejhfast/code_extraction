# Sorting based on the count in a related field in Django
from django.db.models import Count
Tag.objects.annotate(img_count=Count('image')).order_by('img_count')
