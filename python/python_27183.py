# Annote and count posts related to a specific class, in Django
entry_count = Topic.objects.values('title').annotate(Count('entry')).order_by('-entry__count')
