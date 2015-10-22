# How to query data rows with id is specified by another query with Django queryset
User.objects.filter(id__in=SomeModel.objects.filter(field=something).values_list('user_id', flat=True))
