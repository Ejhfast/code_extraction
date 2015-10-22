# List comprehension not working?
a_list = [User.objects.filter(id__in= Share.objects.filter(users_id = log_id, files__file_name=k).values_list('shared_user_id', flat=True)) for k in file1]
