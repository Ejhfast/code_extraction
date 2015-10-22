# Combine query result
results = []
for language in categories.language.all():
    results.append(Movie.objects.filter(title__istartswith=q, language=language)[:10])
