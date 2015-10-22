# Python - Django Select From Table Where Value "IN" - Error invalid literal for int() with base 10: ','
n = request.POST['gcn']
n = n.replace(' ', '').split(',')
results = MyTable.objects.filter(gcn__in=n)
