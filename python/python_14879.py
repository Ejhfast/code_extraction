# How to get foreign key object of a queryset?
User.objects.filter(member__isAdmin=True, member__project=p)
