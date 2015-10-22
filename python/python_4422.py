# Django - filter ManyToManyField?
james = User.objects.get(pk= 123)
james_groups = james.group_set.all()
