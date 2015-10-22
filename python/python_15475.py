# filter function- how to pass foreign key objects attribute as Keyword
inner_qs = Blog.objects.filter(writer__name__icontains='John')
