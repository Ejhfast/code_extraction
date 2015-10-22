# How to mark every favorited item?
images_not_in_users_albums = Image.objects.exclude(album__user=user)
