# How can i filter a ManyToManyField if it contains a specified user?
Post.objects.filter(followers__in=[user])
