# django count a field but group by another
results = MyModel.objects.all()\
    .values('region')\
    .annotate(total=Count('id'))
