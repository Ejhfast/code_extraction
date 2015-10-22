# Fastest Way to Update a bunch of records in queryset in Django
Entry.objects.all().update(value= not F('value'))
