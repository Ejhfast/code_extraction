# How to get the user email from auth.User when filterring a field in UserProfile?
groups_list = User.objects.filter(userprofile__status__in=group_list).values_list('email',    flat=True)
