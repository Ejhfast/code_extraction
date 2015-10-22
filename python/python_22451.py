# How to list all the groups that a user does not belong to in django?
Group.objects.exclude(id__in=request.user.groups.all().values_list('id', flat=True))
