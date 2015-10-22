# Problem loading Django fixture: IntegrityError: (1062, "Duplicate entry '4' for key 'user_id'")
def create_user_profile(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        UserProfile.objects.create(user=instance)
