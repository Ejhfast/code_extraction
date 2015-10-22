# Comparing two QuerySets in Python/Django
attrs_list = Entity.objects.filter(**filters).distinct().values_list('someattr', flat=True)
a = Character.objects.filter(someotherattr__in=attrs_list)
