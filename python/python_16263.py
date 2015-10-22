# Django objects queryset filter by matching datetime
MyModelName.objects.filter(timestamp__gte=(datetime.datetime.now() - datetime.timedelta(seconds=30)))
