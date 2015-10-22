# Get everything that a Many-To-Many Field does not point to
UserProfile.objects.exclude(id__in=chris.pageView.userList.all())
