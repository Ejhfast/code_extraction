# linux - export tree directory list with links to file
Django - Query models where id equals attribute on python list
ids = [i['id'] for i in json_array]
qs = model.objects.exclude(id__in=ids)
