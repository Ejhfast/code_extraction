# Filter by presence in a model's set
Customer.objects.filter(location__in=your_customer_instance.location_set.all()).exclude(pk=your_customer_instance.pk)
