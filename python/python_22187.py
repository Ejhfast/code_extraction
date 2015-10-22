# Getting products with at least one image
products = Product.objects.filter(status='PU', images__isnull=False).order_by('?')[:4]
