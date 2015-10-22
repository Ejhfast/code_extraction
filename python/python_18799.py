# list.reverse() doesn't work properly in Django
posts = Post.objects.all().order_by('-id')
