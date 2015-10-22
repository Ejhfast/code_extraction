# Database query across django ManyToManyField
pics = Picture.objects.filter(categories__in = [1,2,3]).filter(visible=True)
