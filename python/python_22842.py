# Sort Django query result by number of matches
BlogPost.objects.filter(q1 | q2).annotate(blog_times=Count('id')).order_by('blog_times')
