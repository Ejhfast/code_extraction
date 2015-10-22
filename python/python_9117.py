# Django ORM object count
sum([box.quantity_available * box.items_in_box for box in Box.objects.all()]
