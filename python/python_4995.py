# django pagination and RawQuerySet
paginator = Paginator(files, 12)
paginator._count = len(list(files))
