# how to specify date format in django while defining models.
datetime.strptime(time_string, "%m/%d/%Y").strftime("%Y-%m-%d")
