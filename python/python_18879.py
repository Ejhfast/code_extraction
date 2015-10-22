# Filter objects queryset by foreign key django
Auther.objects.filter(book__isnull=False).distinct()
