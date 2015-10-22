# Fetching data from Many to Many relationship (intermediate table)
category = Category.objects.get(pk=10)
products = category.product_set.all()  # note that this is a queryset
