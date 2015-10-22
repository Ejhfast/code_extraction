# Efficient way to check for a M2M intersection in Django?
profile_a.genres.all().filter(id__in=profile_b.genres.all())
