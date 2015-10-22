# Django select database objects based on previous query
posts = Post.objects.filter(user__following__user=request.user)
