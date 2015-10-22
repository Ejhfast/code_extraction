# Number of times each day occurs between two dates
service_start = datetime.date(2012, 5, 6)
service_end = datetime.date(2015, 7, 24)
first_days = (service_end.year - service_start.year) + (1 if service_start.month == 1 and service_start.day == 1 else 0)
