# Ordering Django queryset by an @property
sorted(Thing.objects.all(), key=lambda t: t.name)
