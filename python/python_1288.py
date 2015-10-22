# Django / Python / PIL / sorl-thumbnail generation in bulk - memory error
all = Picture.objects.all().iterator()
for i in all:
    i.image.generate_thumbnails()
