# Django: How to order comments of a post directly under each original post object?
for post in username.newpost_set.all():
    comments = postcomment.objects.filter(commenttag=post).order_by('-postcommentdate')
    # your code here
