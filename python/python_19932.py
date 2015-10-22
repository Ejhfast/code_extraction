# Selecting data from few relational tables based on few conditions in Django
objects = Entity.objects.filter(active=True,
                                key__is_valid=True,
                                user__profile__profile_id__isnull=False)
