# Get foreign key without requesting the whole object
&gt;&gt;&gt; Foo.objects.all().values('user__id')
[{'user__id': 1}, {'user__id' 2}, {'user__id': 3}]
