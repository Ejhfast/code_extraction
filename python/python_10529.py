# Getting all objects referenced in a foreign key field
Person.objects.exclude(director__set=None)
