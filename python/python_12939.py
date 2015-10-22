# SyntaxError: non-keyword arg after keyword arg
dates = CalendarDay.objects.filter(calendar = booking.calendar, calendar_date__ge = booking.arrival_date, calendar_date__le = booking.departure_date)
