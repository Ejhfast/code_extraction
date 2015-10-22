# Trying to create a tuple of objects create an object and a queryset
album_list.append((album, Photo.objects.filter(album=album).order_by('?')[0]))
