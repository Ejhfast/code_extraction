# Copying contents of a model
object = Emp.objects.get(pk=profile.id)
object.save(force_insert=True)
