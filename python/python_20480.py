# Python date.today shows the next day
datetime.utcnow().replace(tzinfo = pytz.utc).strftime('%Y-%m-%d')
