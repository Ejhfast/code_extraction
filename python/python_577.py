# How do I update an object's members using a dict?
for key,value in request.GET.items():
    setattr(foo, key, value)
