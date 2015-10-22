# TypeError can't pickle function objects (Django caching)
foo = list(Foo.objects.annotate(bar_count=Count('bar')).filter(bar_count__gte=1))
