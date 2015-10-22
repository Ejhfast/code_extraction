# How do I use AND in a Django filter?
mymodel.objects.filter(first_name__icontains="Foo", first_name__icontains="Bar")
