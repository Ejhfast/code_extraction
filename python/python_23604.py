# Average Number of days between 2 dates in SQL Alchemy with Postgres
func.avg(func.justify_days(Booking.departure_date - Booking.booking_date)).label('average_lead_time')).\
