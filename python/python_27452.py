# Django: show value of dictionary in dropdown
CollectionPoint.objects.order_by().values_list('city', flat=True).distinct()
