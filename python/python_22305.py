# Select_Related and JSON - How to serialize foreign key objects
e = Entry.objects.select_related('blog').filter(...)
return serializers.serialize('json', [x.blog for x in e])
