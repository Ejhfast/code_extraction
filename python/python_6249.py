# Order by method in model
Car.objects.annotate(score=Avg('rating__score').order_by('-score')
