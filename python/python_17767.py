# Filter data from models based on some condition
included_clients = clientData.objects.values_list('client', flat=True)
