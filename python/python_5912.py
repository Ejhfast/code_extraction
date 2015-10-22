# Slicing in mongoengine
thread = Thread.objects.fields(slice__comments=10).get(id=thread_id)
