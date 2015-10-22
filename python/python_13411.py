# Django db search keywords, not exact text
results = Path.objects.all()
for s in search.split():
    results = results.filter(path__icontains = s)
