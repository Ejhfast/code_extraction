# Retrieving newest object for persons
returned = Person.objects.filter( carusage__end__isnull=True ).annotate(Max('carusage__start'))
not_returned = Person.objects.filter( carusage__end__isnull=False ).annotate(Max('carusage__end'))
