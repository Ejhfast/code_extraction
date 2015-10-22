# how to count all distinct records in many-to-many relations in django ORM?
Category.objects.filter(project__in=query).annotate(Count('project'))
