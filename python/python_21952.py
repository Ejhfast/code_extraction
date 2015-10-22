# Use Django ORM to select rows if a value is in a range stored in columns
GeoIP.objects.filter(start_ip__lte='68.180.194.242', end_ip__gte='68.180.194.242')
