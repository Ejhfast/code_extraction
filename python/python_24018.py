# How to get object with User username?
author = UserProfile.objects.get(user__username__iexact='your_username')
