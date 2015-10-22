# Do Django models have a data dict containing all the current values?
&gt;&gt;&gt; Blog.objects.filter(name__startswith='Beatles').values()
[{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]
