# In Django, Can I `defer()` fields in an object that's being queried by `select_related()`
FooModel.objects.all().select_related('bar').defer('bar__blah', ...)
