# Django - getting object by its related fields' IDs
z = models.Zomg.objects.get(foo__id=1, bar__id=1)
