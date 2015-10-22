# Django serializer for one object
job = Job.objects.get(pk=1)
array_result = serializers.serialize('json', [job], ensure_ascii=False)
just_object_result = array_result[1:-1]
