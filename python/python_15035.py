# Sort and show objects with True in BooleanField first
Foo.objects.all().order_by('-field')
