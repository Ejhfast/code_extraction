# Django JSON string to json object
data = list(Data.objects.all().values('deviceId','payload'))
