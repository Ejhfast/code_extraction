# how to subquery in queryset in django?
ids = Employee.objects.filter(company='Private').values_list('id', flat=True)
Person.objects.filter(id__in=ids).values('name', 'age')
