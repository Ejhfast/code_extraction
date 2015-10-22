# Django: Get all model instances of top level category
items = Item.objects.filter(category__parent=parent_category)
