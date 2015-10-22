# Django - is it possible to quickly code this query through Django's models?
results = SourceBusiness.objects.filter(resultbusiness__isnull=False).distinct().values_list('source', flat=True)
