# Get Monday and Sunday and last year's Monday and Sunday, same week
NOW = datetime.now()
last_monday = NOW+relativedelta(years=-1, weekday=MO)
last_sunday = NOW+relativedelta(years=-1, weekday=SU)
