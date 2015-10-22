# Django queryset filter from two models
your_queryset = tab1.objects.filter(tab2__type=value)
