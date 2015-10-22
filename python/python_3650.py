# Grouping a queryset by another related model
Stop.objects.filter(approved_ts__isnull=False).order_by('line')
