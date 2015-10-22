# sql "LIKE" equivalent in django query
result = table.objects.filter(string__contains='pattern')
