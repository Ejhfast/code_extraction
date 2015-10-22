# django query returns error: expected str instance, ValuesListQuerySet found
list_of_animals = list(MyModel.objects.values_list('title', flat=True))
