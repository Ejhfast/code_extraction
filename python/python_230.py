# Refactor this Python code to iterate over a container
results = [(getattr(obj, field.attname), obj.pk) for obj in queryset or []]
