# Matching a datetime against a date in django
Samples.objects.filter(when__year = mydate.year, when__month = mydate.month, when__day = mydate.day)
