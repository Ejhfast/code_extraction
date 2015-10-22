# How to query filter in django without multiple occurrences
ParentModel.objects.filter(childmodel__in=ChildModel.objects.all()).distinct()
