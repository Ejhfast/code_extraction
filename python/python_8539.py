# convert SQL to django QuerySet
HotelCheck.objects.filter(client=1, status='Complete').values('product','date_booked').annotate(Sum('quantity'))
