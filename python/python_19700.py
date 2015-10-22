# Django order by most frequent value
from django.db import Count
FoodTruck.objects.values_list('name').annotate(truck_count=Count('name')).order_by('-truck_count')
