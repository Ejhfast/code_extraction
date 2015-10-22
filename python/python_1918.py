# How to filter a query by property of user profile in Django?
designs = Design.objects.filter(author__user__profile__screenname__icontains=w)
