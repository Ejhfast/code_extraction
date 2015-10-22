# Django serializer gives 'str' object has no attribute '_meta' error
objects= Session.objects.aggregate(Max('date'), Min('date'))
print [ type[o] for o in objects ]
result =  serializers.serialize("json", objects, ensure_ascii=False)
