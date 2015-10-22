# Can i do an order_by on day in month?
UserProfile.objects.select(extra={'birth_day': 'extract(day from birthDate)'}).order_by('-birth_day')
