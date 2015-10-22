# Retrieve UNIX TIMESTAMP in django api call
Analytics.objects.extra(select={'timestamp': "CONCAT(UNIX_TIMESTAMP(date), '000')"}).order_by('date').values('timestamp', 'users')
