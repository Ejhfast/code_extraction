# How to filter query by pair of foreign keys in Django?
Post.objects.exclude(user=F('topic__user')).values('user').annotate(Count('id'))
