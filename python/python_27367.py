# Django count foreign key through relation
forum_posts = Post.objects.filter(thread__forum=my_forum)
forum_post_count = forum_posts.count()
