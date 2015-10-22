# How do I filter with active data? Django
Promo.objects.filter(expiration__gte=datetime.date.now())
