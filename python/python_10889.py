# In django-taggit, how to get tags for objects that are associated with a specific user?
tags = Tag.objects.filter(book__owner=me)
tags |= Tag.objects.filter(journalarticle__owner=me)
tags = tags.distinct()
