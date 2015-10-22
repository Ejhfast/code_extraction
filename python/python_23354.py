# Django - Exclude two conditions in query
status = ['deleted', '']
Object.objects.filter(country_send=country).exclude(status__in=status).order_by('-id')
