# Django query datetime < '2014-12-22'
obj = Showtime.objects.filter(source=1,movietme__lt=tomorrow)
