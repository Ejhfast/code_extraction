# Only show the latest 3 posts in Django?
posts = Post.objects.filter(published=True).order_by('-pub_date')[0:3]
