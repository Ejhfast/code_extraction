# How do I use a string as a keyword argument?
d = Image.objects.filter(**{'image__endswith': "jpg"})
