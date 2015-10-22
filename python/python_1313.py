# Django: check whether an object already exists before adding
role, created = UserToUserRole.objects.get_or_create(
    from_user=current_user, to_user=user, role='follow')
