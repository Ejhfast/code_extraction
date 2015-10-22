# Exclude on a many-to-many relationship through a third table
Person.objects.exclude(id__in=Person.objects.filter(project=p, status__is_red=True).values(id))
