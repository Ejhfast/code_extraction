# How do I clone a Django model instance object and save it to the database?
obj = Foo.objects.get(pk="foo")
obj.pk = "bar"
obj.save()
