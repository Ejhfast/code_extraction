# Invalid literal for int() in Django model
user_playlists = Everything.objects.filter(profile__username=friend).values('playlist').distinct()
