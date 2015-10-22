# optimize this query that selects rows before and after a pk
next_objs = Media.objects.filter(id__gt=image.id).order_by('id')[:2]
prev_objs = Media.objects.filter(id__lt=image.id).order_by('-id')[:2]
