# Django reverse relationship name gives invalid keyword argument error
params = Params.objects.create(name="Test")
object_cat.params = params
object_cat.save()
