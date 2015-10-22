# How can I retrieve last x elements in Django
blog_post_list = blogPosts.objects.all().order_by('-pub_date')[:5]
