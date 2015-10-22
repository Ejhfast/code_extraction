# django error validation datetime.datetime, tz format
data = Entry.objects.filter(date_publication__gte=from_date, date_publication__lte=datetime.now())
