# Django 1.6 ORM count subset of related items
BlogEntry.objects.filter(tags__in=tag_list).annotate(match=Count(tags))
