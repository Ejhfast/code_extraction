# Python `YYYY-MM-DD`
year, month, day = cal.get_date()
return '{0:04d}-{1:02d}-{2:02d}'.format(year, month+1, day)
