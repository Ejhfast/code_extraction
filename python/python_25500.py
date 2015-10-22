# Django Many to Many Query Set Filter
for author in Author.objects.filter(post__isnull=False):
    print author
