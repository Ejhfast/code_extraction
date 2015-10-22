# How to Update a Many-Many Field in Django
# let publication be your existing Pets publication instance
cats_tag, created = Tag.objects.get_or_create(title='cats')
publication.tags.add(cats_tag)
