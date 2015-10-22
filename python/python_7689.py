# how to get the datetime.date() value from django model?
s = Booking.objects.values('date_select').distinct('date_select').filter(date_select='2011-12-1')[0]['date_select']
