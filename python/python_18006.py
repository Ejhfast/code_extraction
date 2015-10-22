# prefetch_related with Django 1.5 + django-model-utils
Post.objects.filter(user=user)\
    .select_subclasses()\
    .prefetch_related('photopost__photo')
