# Serializing a queryset in dehydrate
bundle.data['stuff'] = [st.__dict__ for st in Stuff.objects.all()]
