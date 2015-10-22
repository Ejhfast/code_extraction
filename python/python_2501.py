# In Django, how do I filter where language column = "null"?
MyTable.objects.filter(language__isnull=True)
