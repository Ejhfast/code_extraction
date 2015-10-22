# Django filter on related field using annotate
Blog.objects.filter(reader__type__name='male').annotate(reader_count=Count('reader')).filter(reader_count__gte=2)
