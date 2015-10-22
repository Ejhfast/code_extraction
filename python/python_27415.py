# How do you extract unique queryset from queryset of objects with ManyToManyField
#add .distinct() if you get duplicate users.
users = User.objects.filter(channels__manager=request.user)
