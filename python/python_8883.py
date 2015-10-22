# How do I filter based on dict contents in a DictField on a model using the Django-MongoDB Engine?
Post.objects.raw_query({'author.name': "Ralph"})
