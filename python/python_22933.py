# Reverse lookup of foreign key in python django
return Dept.objects.filter(employees_set__name='XYZ')
