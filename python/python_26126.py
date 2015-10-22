# Django __iregex Returns Empty Response
articles = Articles.objects.filter(content__iregex=r"^[^.]*{0}*[[:&gt;:]]".format(hash_tag))
