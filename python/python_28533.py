# Unable to group sum value in Django query
Resource.objects.values('start_date').annotate(total=Sum('percentage')).order_by()
