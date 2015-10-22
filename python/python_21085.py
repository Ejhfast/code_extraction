# Django get objects for many IDs
objects = SomeModel.objects.filter(id__in=id_set)
