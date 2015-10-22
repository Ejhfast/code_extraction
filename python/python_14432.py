# django - get the latest record with filter
obj= Model.objects.filter(testfield=12).order_by('-id')[0]
