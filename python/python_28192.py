# Shuffle queryset in Django
shuffled = sorted(qs, key=lambda item: item.order if item.order != 999 else 999 + random.random())
