# Query ManyToMany relations without a named through field
topics = Topic.objects.filter(article__authors=author).distinct()
