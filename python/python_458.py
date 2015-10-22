# How to compare value of 2 fields in Django QuerySet?
players = Player.objects.filter(batting__gt=F('bowling'))
