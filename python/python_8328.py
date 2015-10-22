# Making a query for all objects that don't have `None` for a certain field
Chair.objects.filter(datetime__isnull=False)
