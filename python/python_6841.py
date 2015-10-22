# django list of unicode string to pure string
MyModel.objects.filter(countries__in=unicode_countries)
