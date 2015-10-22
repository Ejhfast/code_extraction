# How do I pass in a field to filter a Django model?
kwargs = {filter_field: filter_value}
Alert.objects.filter(**kwargs)
