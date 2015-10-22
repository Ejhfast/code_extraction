# Find in list in Django. Find single column
A.objects.filter(id=70).values_list('name')
A.objects.get(id=70).name
