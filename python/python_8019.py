# Get a list of filtered values for a single field from a Django model
MyObject.objects.filter(name='Mike').values_list('address', flat=True)
