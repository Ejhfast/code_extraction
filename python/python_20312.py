# Perform a Django query on a part of a field
Product.objects.filter(version__regex=r'^[5-9]\.')
