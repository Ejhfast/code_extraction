# Accessing values from many-to-many fields in django
obj_list = VM.objects.filter(d_store__type='rbd')
