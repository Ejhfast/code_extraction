# Check if datetime object is present in database
Booking.objects.filter(start_date__lte=start_time, end_date__gte=start_time).count()
