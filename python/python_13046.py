# Select values which not in another table with Django
inner_qs = table2.objects.all()
results = table1.objects.exclude(field1__in=inner_qs)
