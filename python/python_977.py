# Django: queryset filter for *all* values from a ManyToManyField
Basket.objects.annotate(num_fruits=Count('fruits')).filter(num_fruits=len(Fruit.objects.all()))
