# How to get all 'Post' objects where 'User' has replied?
posts = Post.objects.filter(postreply__owner=self.request.user, postreply__accepted=True)
