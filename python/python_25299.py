# Django MySQL Join to increase performance
DispensaryItem.objects.filter(dispensary__location='Washington', item__product_type__name=category)
