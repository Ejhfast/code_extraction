# Total Objects based on Value of Another Object
count = Email.objects.filter(recipients__gt=0).values('month').distinct().count()
