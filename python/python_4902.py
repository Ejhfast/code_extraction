# Retrieving date from a datetime column in python/django
queryset = MyModel.objects.filter(date__year=2011, date__month=3, date__day=18)
