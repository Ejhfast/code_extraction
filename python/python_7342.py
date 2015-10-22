# sort by count in json
Blog.objects.annotate(comment_count=Count('comments')).order_by('comment_count')
