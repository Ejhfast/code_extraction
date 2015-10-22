# Django, queryset filter ManyToManyField
current_course = Course.objects.get(pk=course)
modules = Module.objects.all().filter(course=current_course)
