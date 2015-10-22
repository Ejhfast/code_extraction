# Django ORM: Selecting related set
Poll.objects.filter(category='foo').fetch_reverse_relations('choices_set')
