# Django: follow relations backwards
galleries = Galleries.objects.get(id=1)
values = galleries.gallery_type.values_set.filter(language='language')
