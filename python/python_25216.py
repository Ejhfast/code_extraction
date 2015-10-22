# django.db aggregation across multiple fields
sum(Tables.objects.filter(state=MD).aggregate(x=Sum('B'), y=Sum('C')).values())
