# python - how to find datetime 10 mins after current time?
now = datetime.datetime.now()
now_plus_10 = now + datetime.timedelta(minutes = 10)
