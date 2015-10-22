# ValueError: need more than 1 value to unpack, django email error
addresses = User.objects.filter(group__group='Operations').values_list('email', flat=True)
