# How to select all objects that are foreign keyed from another model in django?
Person.objects.filter(teacher__isnull=False)
# return Person who has a teacher pointing to it
